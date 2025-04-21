from collections import defaultdict, Counter, namedtuple
import csv


class InvalidColumnNames(Exception):
    """
    Raised when column names are not alphanumeric.
    List of Methods:
        __init__: Initializes the exception with the problematic column names.
    """

    def __init__(self, col_names):
        """
        Raised when col names are not alphanumeric.
        Args:
            col_names (list): A list of col names that caused the exception.
        """
        self.col_names = col_names
        self.msg = f"The names of the columns are invalid. Column names can only be letters and numbers : {col_names}"
        print(self.msg)
        super().__init__(self.msg)


class NoRecordStatsFound(Exception):
    """
    Raised when statistics for a specified column name do not exist.
    List of Methods:
        __init__: Initializes the exception with the missing column name.
    """

    def __init__(self, column_name):
        """
        Raised when statistics for a col don't exist.
        Args:
            column_name (str): The name of the col where stats were not found.
        """
        self.column_name = column_name
        self.msg = f"The column stats you’re trying to access doesn’t exist. You entered {column_name}."
        print(self.msg)
        super().__init__(self.msg)


class Records:
    """
    Manages and processes records from a CSV file.
    List of Methods:
        __init__: Initializes the Records instance by creating a defaultdict and loading data.
        load_data: Attempts to open and read the CSV file, then loads the data into a namedtuple-based structure.
        _create_container: Creates a namedtuple class based on the CSV header.
        _standardize_col_names: Removes special characters and ensures column names are alphanumeric.
        record_stats: Computes and stores statistical counts for a specified column using a provided function.
        extract_top_n: Retrieves the top N most common entries for a specified data set and stats column.
    """

    def __init__(self, file_name, file_title):
        """
        Inits the Records class.
        Args:
            file_name (str): The path to the CSV file.
            file_title (str): A title or identifier for the file's record set.
        """
        self.record_dict = defaultdict(lambda: defaultdict(list))
        self.load_data(file_name, file_title)

    def load_data(self, file_name, file_title):
        """
        Loads data from CSV file into record dictionary.
        Args:
            file_name (str): Path to CSV.
            file_title (str): Title for the file's record set.
        """
        while True:
            try:
                with open(file_name, 'r', newline='', encoding='utf-8') as csvfile:
                    reader = csv.reader(csvfile)
                    header = next(reader)
                    container = self._create_container(header)
                    for row in reader:
                        entry = container(*row)
                        self.record_dict[file_title]['data'].append(entry)
            except FileNotFoundError:
                new_file = input(f"File {file_name} not found. Please enter a valid file name or 'q' to quit: ")
                if new_file.lower() == 'q':
                    return
                else:
                    file_name = new_file
                    continue
            else:
                print(f"File {file_name} loaded successfully.")
                break

    def _create_container(self, header):
        """
        Creates namedtuple structure based on provided header list.
        Args:
            header (list): List of col names from CSV file.

        Returns:
            namedtuple: A namedtuple tailored to the standardized col names.
        """
        while True:
            try:
                std_header = self._standardize_col_names(header)
                Entry = namedtuple("Entry", std_header)
                return Entry
            except InvalidColumnNames as e:
                new_names = input("Invalid column names. Please enter the column names separated by commas: ")
                header = [name.strip() for name in new_names.split(",")]

    def _standardize_col_names(self, col_names):
        """
        Standardizes column names by removing underscores, dashes, and spaces.
        Args:
            col_names (list): Original column names from the CSV.
        Returns:
            list: A list of standardized column names that are alphanumeric.
        """
        standardized = [col.replace("_", "").replace("-", "").replace(" ", "") for col in col_names]
        for col in standardized:
            if not col.isalnum():
                raise InvalidColumnNames(standardized)
        return standardized

    def record_stats(self, file_title, column_name, lambda_func):
        """
        Computes and stores statistical counts of specified column using a provided function.
        Args:
            file_title (str): Title or identifier corresponding to record set.
            col_name (str): Name of the column on which to compute statistics.
            func (callable): Function or lambda used to extract the column's value from each record.
        """
        values = list(map(lambda_func, self.record_dict[file_title]['data']))
        counter_obj = Counter(values)
        stats_key = f"stats_{column_name}"
        self.record_dict[file_title][stats_key] = counter_obj

    def extract_top_n(self, n, file_title, stats_column_name):
        """
        Retrieves top N most common entries for specified data set and col.
        Args:
            n (int): Number of common entries to retrieve.
            file_title (str): Title or identifier corresponding to the record set.
            stats_column_name (str): Name of the stats column to query.

        Returns:
            list or None: List of tuples containing the top N entries and their counts,
                          or None if specified stats column does not exist.
        """
        while True:
            try:
                counter_obj = self.record_dict[file_title][stats_column_name]
                return counter_obj.most_common(n)
            except KeyError:
                try:
                    raise NoRecordStatsFound(stats_column_name)
                except NoRecordStatsFound as e:
                    new_col = input("Enter a different stats_column_name or 'q' to quit: ")
                    if new_col.lower() == 'q':
                        return None
                    else:
                        stats_column_name = new_col
