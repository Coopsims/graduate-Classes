import os
import pandas as pd
import numpy as np

def check_column_exists(df, col):
    """
    Check if column exists in pd.

    Args:
        df (pd.DataFrame): DataFrame to check.
        col (str): Column name to verify.

    Returns:
        bool: True if the column exists, False otherwise.
    """
    if col not in df.columns:
        print(f"Error: Column '{col}' does not exist in the DataFrame.")
        return False
    return True


def above_median(series):
    """
    Calculate percentage of non-null values in Series which are above its median.

    Args:
        series (pd.Series): Pandas Series to analyze.

    Returns:
        float: Percentage (0-100) of values above the median.
               Returns NaN if median is NaN
    """
    median_val = series.median()
    if pd.isna(median_val):
        return np.nan
    total = series.count()
    if total == 0:
        return np.nan
    count_above = (series > median_val).sum()
    return (count_above / total) * 100


def mode_func(series):
    """
    Compute mode of pandas Series.

    Args:
        series (pd.Series): Series for which to calculate the mode.

    Returns:
        Mode of the Series if exists; otherwise, returns NaN.
    """
    modes = series.mode()
    if not modes.empty:
        return modes.iloc[0]
    else:
        return np.nan


class RealEstate2:
    """
    Class to manage and analyze real estate data from a CSV file.

    Methods:
        __init__: Initialize RealEstate2 object and load data from a CSV file.
        load_data: Load real estate data from a CSV file into properties DataFrame.
        _col_2_numeric: Convert specified columns in DataFrame to numeric data types.
        check_type: Retrieve data types of each column in properties DataFrame.
        num_nulls: Count number of null values in a specified column.
        get_unique_vals: Retrieve count and list of unique values in a specified column.
        filth_be_gone: Remove rows from DataFrame where a specified column has a given value.
        col_val_count: Count frequency of each unique value in a specified column.
        summary_table: Generate summary table by grouping data and applying aggregation operations.
    """

    def __init__(self, file_name, file_path):
        """
        Initialize RealEstate2 object and load data from a CSV file.

        Args:
            file_name (str): Name of the CSV file to load.
            file_path (str): Directory path where the CSV file is located.
        """
        self.properties_df = pd.DataFrame()
        self.load_data(file_name, file_path)

    def load_data(self, file_name, file_path):
        """
        Load real estate data from a CSV file into the properties DataFrame.

        Args:
            file_name (str): Name of the CSV file to load.
            file_path (str): Directory path where the CSV file is located.
        """
        full_path = os.path.join(file_path, file_name)
        while True:
            try:
                self.properties_df = pd.read_csv(full_path, low_memory=False)
                self._col_2_numeric()
                self.properties_df.drop_duplicates(inplace=True)
                break
            except FileNotFoundError:
                user_input = input(f"File {full_path} not found. Enter a valid file name (or 'q' to quit): ")
                if user_input.lower() == 'q':
                    print("Quitting load_data.")
                    break
                else:
                    file_name = user_input
                    full_path = os.path.join(file_path, file_name)

    def _col_2_numeric(self):
        """
        Convert specified columns in the DataFrame to numeric data types.

        """
        while True:
            col = input("Enter column name to convert to numeric (or 'q' to quit): ")
            if col.lower() == 'q':
                break
            if not check_column_exists(self.properties_df, col):
                continue
            self.properties_df[col] = pd.to_numeric(self.properties_df[col], errors='coerce')

    def check_type(self):
        """
        Retrieve data types of each column in properties DataFrame.

        Returns:
            pd.Series: Series containing the data types of DataFrame's columns.
        """
        return self.properties_df.dtypes

    def num_nulls(self, column_name):
        """
        Count number of null values in specified column.

        Args:
            column_name (str): Name of the column to check.

        Returns:
            int or None: Number of null values in the column, or None if the column does not exist.
        """
        if not check_column_exists(self.properties_df, column_name):
            return None
        return self.properties_df[column_name].isnull().sum()

    def get_unique_vals(self, column_name):
        """
        Retrieve count and list of unique values in specified column.

        Args:
            column_name (str): Name of the column.

        Returns:
            tuple or None: Tuple containing the number of unique values and an array of the unique values,
                           or None if the column does not exist.
        """
        if not check_column_exists(self.properties_df, column_name):
            return None
        uniques = self.properties_df[column_name].unique()
        return len(uniques), uniques

    def filth_be_gone(self, column_name, value):
        """
        Remove rows from DataFrame where a specified column has a given value.

        Args:
            column_name (str): Column to filter.
            value: Value in the column that should be removed.
        """
        if not check_column_exists(self.properties_df, column_name):
            return
        self.properties_df = self.properties_df[self.properties_df[column_name] != value]

    def col_val_count(self, column_name):
        """
        Count frequency of each unique val in a specified column.

        Args:
            column_name (str): Name of the column.

        Returns:
            pd.Series or None: Series with the counts of each unique value in the column,
                               or None if the column does not exist.
        """
        if not check_column_exists(self.properties_df, column_name):
            return None
        return self.properties_df[column_name].value_counts()

    def summary_table(self, index_cols, summary_cols, ops):
        """
        Generate summary table by grouping data and applying aggregation operations.

        Args:
            index_cols (list): List of column names to group by.
            summary_cols (list): List of column names to aggregate.
            ops (list): List of aggregation operations to apply. Supported custom operations include:
                        - "above_median": Calculates the percentage of non-null values above the median.
                        - "mode": Returns the mode of the column.

        Returns:
            pd.DataFrame or None: DataFrame representing the summary table, or None if any specified column does not exist.
        """
        for col in index_cols + summary_cols:
            if not check_column_exists(self.properties_df, col):
                return None
        agg_dict = {}
        for col in summary_cols:
            func_list = []
            for op in ops:
                if op == "above_median":
                    func_list.append(above_median)
                elif op == "mode":
                    func_list.append(mode_func)
                else:
                    func_list.append(op)
            agg_dict[col] = func_list
        summary_df = self.properties_df.groupby(index_cols).agg(agg_dict)
        return summary_df


if __name__ == "__main__":
    file_name = "realtor-data.csv"
    file_path = os.path.join(os.getcwd(), "data")
    real_estate = RealEstate2(file_name, file_path)

    print("Data types:")
    print(real_estate.check_type())

    print("\nNumber of nulls in 'bed':")
    print(real_estate.num_nulls("bed"))

    print("\nUnique values in 'state':")
    print(real_estate.get_unique_vals("state"))

    print("\nValue counts for 'city':")
    print(real_estate.col_val_count("city"))

    summary = real_estate.summary_table(["state", "city"], ["house_size", "price"], ["mean"])
    print("\nSummary table (mean and percentage above median):")
    print(summary)