def calculate_payments(amount, int_rate, duration):
    """
    Calculate monthly payment needed to amortize a loan over a specified duration.

    Args:
        amount (float): Initial loan principal (amount borrowed).
        int_rate (float): Annual interest rate, expressed as percentage.
        duration (int): Total number of monthly payments to repay the loan.

    Returns:
        float: Fixed monthly payment required to settle the loan in the given number of months.
    """
    monthly_rate = (int_rate / 100) / 12
    if monthly_rate == 0:
        return amount / duration
    M = amount * (monthly_rate * (1 + monthly_rate) ** duration) / ((1 + monthly_rate) ** duration - 1)
    return M


def calculate_total_paid(amount, int_rate, duration):
    """
    Compute the total amount paid over the full term of the loan.

    Args:
        amount (float): Initial loan principal (amount borrowed).
        int_rate (float): Annual interest rate, expressed as percentage.
        duration (int): Total number of monthly payments to repay the loan.

    Returns:
        float: Total amount of money paid by the time the loan is fully satisfied.
    """
    monthly_payment = calculate_payments(amount, int_rate, duration)
    return monthly_payment * duration


def calculate_total_interest(amount, int_rate, duration):
    """
    Determine the total interest paid over the life of the loan.

    This is calculated by subtracting the initial amount (principal)
    from the total paid over the entire term.

    Args:
        amount (float): Initial loan principal (amount borrowed).
        int_rate (float): Annual interest rate, expressed as percentage.
        duration (int): Total number of monthly payments to repay the loan.
    Returns:
        float: Total interest paid once all payments have been made.
    """
    total_paid = calculate_total_paid(amount, int_rate, duration)
    return total_paid - amount
