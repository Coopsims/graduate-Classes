import pandas as pd
import os
from debt_repayment.tools.my_logger import get_logger


class AmortizationTable:


    def __init__(self, loan_type, loan_balance, interest_rate, num_months, monthly_payment):
        """
        Initialize an AmortizationTable instance.

        Args:
            loan_type (str): A label indicating the type of loan.
            loan_balance (float): The initial loan balance.
            interest_rate (float): The annual interest rate (in percent).
            num_months (int): The number of months over which the loan is repaid.
            monthly_payment (float): The fixed monthly payment amount.
        """
        self.loan_type = loan_type
        self.loan_balance = float(loan_balance)
        self.interest_rate = float(interest_rate)
        self.num_months = int(num_months)
        self.monthly_payment = float(monthly_payment)
        self.amortization_df = pd.DataFrame()

        self.logger = get_logger()
        self.logger.debug("Instantiating AmortizedTable Class")

        self.create_table()


    def create_table(self):
        """
        Build the amortization schedule and save it to the class attribute.

        Args:
            None

        Returns:
            None
        """

        self.logger.info("Creating the amortized table")
        start_date = pd.Timestamp.today() + pd.offsets.MonthBegin(1)
        dates = pd.date_range(start=start_date, periods=self.num_months, freq='MS')

        monthly_rate = (self.interest_rate / 100) / 12
        balance = self.loan_balance
        table_data = []

        for i, due_date in enumerate(dates, start=1):
            interest_paid = balance * monthly_rate
            principal_paid = self.monthly_payment - interest_paid

            if principal_paid > balance:
                principal_paid = balance
                payment_amount = principal_paid + interest_paid
                balance = 0
            else:
                payment_amount = self.monthly_payment
                balance -= principal_paid

            table_data.append({
                "Pmt #": i,
                "Due date": due_date,
                "Payment amount": round(payment_amount, 2),
                "Principal paid": round(principal_paid, 2),
                "Interest paid": round(interest_paid, 2),
                "Remaining balance": round(balance, 2)
            })

            if balance <= 0:
                break

        self.amortization_df = pd.DataFrame(table_data)
        self.save_table(self.amortization_df)

        # Assign this instance to the global variable 'data'
        global data
        data = self


    def save_table(self, df):
        """
        Save the amortization table to a CSV file.

        Args:
            df (pandas.DataFrame): DataFrame containing the amortization schedule.

        Returns:
            None
        """

        base_dir = os.path.join(os.path.dirname(__file__), "..", "files", "tables")
        if not os.path.exists(base_dir):
            os.makedirs(base_dir)
        filename = f"{self.loan_type}-{self.loan_balance}-{self.monthly_payment}.csv"
        filepath = os.path.join(base_dir, filename)
        df.to_csv(filepath, index=False)


    def more_principal(self):
        """
        Finds first month where principal paid exceeds the interest paid.

        Returns:
            int or None:  Payment number for which the principal
            paid is greater than the interest paid. Returns None if this never occurs.
        """

        df = self.amortization_df
        condition = df["Principal paid"] > df["Interest paid"]
        if condition.any():
            month = df[condition].iloc[0]["Pmt #"]
            return int(month)
        else:
            return None


    def halfway(self):
        """
        Determine when the cumulative principal paid reaches at least half the original balance.

        Returns:
            int or None: Payment number for which the cumulative
            principal paid is at least half of the initial loan balance.
            Returns None if this point is never reached.
        """

        df = self.amortization_df.copy()
        df["Cumulative Principal"] = df["Principal paid"].cumsum()
        half = self.loan_balance / 2.0
        condition = df["Cumulative Principal"] >= half
        if condition.any():
            month = df[condition].iloc[0]["Pmt #"]
            return int(month)
        else:
            return None

    def update_payments(self, lump_sum=0.0, extra_payment=0.0):
        """
        Updates loan balance or monthly payment and rebuild the amortization table.

        Args:
            lump_sum (float, optional): Amount to reduce the loan balance right away.
            extra_payment (float, optional): Additional amount to be added to the
                                             monthly payment.

        Returns:
            None
        """
        self.logger.info("Updating the loan repayment: monthly_payment, loan_balance")
        # Apply a lump sum payment to reduce the balance
        if lump_sum:
            self.loan_balance = max(0, self.loan_balance - lump_sum)
        # Increase the monthly payment by the extra amount
        if extra_payment:
            self.monthly_payment += extra_payment

        self.create_table()
