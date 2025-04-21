import pandas as pd
import matplotlib.pyplot as plt
from .helper_functions.hf import retrieve_files, record_loader_gen

class BabyNames:
    """
    Manages and processes baby name data retrieved from text files.

    List of Methods:
        __init__: Inits the BabyNames class.

        sort_data: Sorts self.names_df in ascending order by 'year'.

        m_f_names: Calculates total births for each gender within the specified year range
            and plots a line chart comparing male vs. female births.

        most_popular_ever: Finds the top three most popular names by total births across all years
            and plots each name's yearly birth counts in a line chart.

        unisex: Finds names used by both genders in the same year, sums their births,
            and displays a bar plot by year.

        unisex_evolution: Find every name that appears at least once for both men and women.
    """

    def __init__(self):
        """
        Inits the BabyNames class.

        Loads all '.txt' data files from the 'baby_names' folder
        into a DataFrame with columns: ['name', 'gender', 'births', 'year'].
        Then calls self.sort_data().
        """

        txt_files = retrieve_files(".txt")
        records = list(record_loader_gen(txt_files))
        self.names_df = pd.DataFrame(records, columns=["name", "gender", "births", "year"])
        self.sort_data()

    def sort_data(self):
        """
        Sorts self.names_df in ascending order by 'year'.
        """

        self.names_df.sort_values(by="year", inplace=True)

    def m_f_names(self, start_year=1880, end_year=2022):
        """
        Calculates total births for each gender within the specified year range
        and plots a line chart comparing male vs. female births.

        Args:
            start_year (int, optional): The earliest year to include. Defaults to 1880.
            end_year (int, optional): The latest year to include. Defaults to 2022.
        """

        df_filtered = self.names_df[(self.names_df["year"] >= start_year) &
                                    (self.names_df["year"] <= end_year)]

        grouped = df_filtered.groupby(["year", "gender"])["births"].sum().reset_index()
        pivoted = grouped.pivot(index="year", columns="gender", values="births").fillna(0)

        plt.figure()
        plt.plot(pivoted.index, pivoted["F"], label="Female")
        plt.plot(pivoted.index, pivoted["M"], label="Male")
        plt.title("Total Male & Female Births by Year")
        plt.xlabel("Year")
        plt.ylabel("Number of Births")
        plt.legend()
        plt.show()

    def most_popular_ever(self):
        """
        Finds the top three most popular names by total births across all years
        and plots each name's yearly birth counts in a line chart.
        """

        total_by_name = self.names_df.groupby("name")["births"].sum().reset_index()
        total_by_name.sort_values(by="births", ascending=False, inplace=True)
        top3 = total_by_name.head(3)["name"].tolist()

        plt.figure()
        for nm in top3:
            df_name = self.names_df[self.names_df["name"] == nm]
            yearly_sum = df_name.groupby("year")["births"].sum().reset_index()
            plt.plot(yearly_sum["year"], yearly_sum["births"], label=nm)

        plt.title("Evolution of Top 3 Most Popular Names")
        plt.xlabel("Year")
        plt.ylabel("Number of Births")
        plt.legend()
        plt.show()

    def unisex(self):
        """
        Finds names used by both genders in the same year, sums their births,
        and displays a bar plot by year.
        """

        grouped = self.names_df.groupby(["year", "name"])["gender"].agg(set).reset_index()
        unisex_names_df = grouped[grouped["gender"].apply(lambda g: len(g) == 2)]

        merged = pd.merge(
            unisex_names_df[["year", "name"]],
            self.names_df,
            on=["year", "name"],
            how="inner"
        )
        unisex_by_year = merged.groupby("year")["births"].sum().reset_index()

        plt.figure()
        plt.bar(unisex_by_year["year"], unisex_by_year["births"])
        plt.title("Sum of Unisex Births Over the Years")
        plt.xlabel("Year")
        plt.ylabel("Number of Unisex Births")
        plt.tick_params(axis="x", which="major", labelsize=7)
        plt.show()

    def unisex_evolution(self):
        """
        Find every name that appears at least once for both men and women.
        """

        grouped = self.names_df.groupby("name")["gender"].agg(set).reset_index()
        unisex_name_records = grouped[grouped["gender"].apply(lambda g: len(g) == 2)]
        unisex_names_set = set(unisex_name_records["name"].tolist())

        print("All unisex names across all time:")
        print(unisex_names_set)
        print("\nEnter as many names (from above) as you'd like. Type 'q' to finish.\n")

        chosen_names = []
        while True:
            user_input = input("Name (or 'q'): ").strip()
            if user_input.lower() == 'q':
                break
            if user_input in unisex_names_set:
                chosen_names.append(user_input)
            else:
                print("Not a valid unisex name. Try again.")

        if not chosen_names:
            print("No valid names were chosen. Exiting method.")
            return

        plt.figure()
        for nm in chosen_names:
            df_nm = self.names_df[self.names_df["name"] == nm]
            by_year = df_nm.groupby("year")["births"].sum().reset_index()
            plt.plot(by_year["year"], by_year["births"], label=nm)

        plt.title("Unisex Name Evolution Over the Years")
        plt.xlabel("Year")
        plt.ylabel("Number of Births")
        plt.legend()
        plt.show()