# load.py
import os
import csv
from collections import defaultdict, namedtuple
from real_estate.helper_functions import context_manager
from real_estate.helper_functions import calculate_stats

# Define known US States and Territories
US_STATES = ['Massachusetts', 'Connecticut', 'New Hampshire', 'Vermont', 'New Jersey',
             'New York', 'South Carolina', 'Tennessee', 'Rhode Island', 'Virginia',
             'Wyoming', 'Maine', 'Georgia', 'Pennsylvania', 'West Virginia', 'Delaware', 'Louisiana']
TERRITORIES = ['Puerto Rico', 'Virgin Islands']


class RealEstate:
    """
    Manages and processes real estate properties from a CSV file.

    List of Methods:
        __init__: Inits the RealEstate class.
        load_data: Attempts to open and read the CSV file, then populate data into a namedtuple.
        _create_container: Creates a namedtuple class based on the CSV header.
        compute_stats: Dynamically calls a function from the calculate_stats module using the class’s data.
    """


    def __init__(self, file_name, location):
        """
        Inits the RealEstate class.

        Args:
            file_name (str): Name of the CSV to load.
            location (str): The directory path where the CSV file is located.
        """
        self.properties_dict = {
            "US States": defaultdict(list),
            "Territories": defaultdict(list)
        }
        self.load_data(file_name, location)

    def load_data(self, file_name, location):
        """
        Attempts to open and read the CSV file, then populate data into a namedtuple.

        Args:
            file_name (str): The name of the CSV file to load.
            location (str): The directory path where the CSV file is located.

        Raises:
            SystemExit: Enter correct file path or exit code.
        """
        file_loaded = False
        while not file_loaded:
            try:
                with context_manager.custom_open(file_name, "r", location) as f:
                    csv_reader = csv.reader(f)
                    header = next(csv_reader)

                    Property = self._create_container(header)

                    for row in csv_reader:
                        if not row or any(field.strip() == "" or "?" in field for field in row):
                            continue
                        try:
                            status = row[0]
                            bed = int(float(row[1]))
                            bath = float(row[2])
                            acre_lot = float(row[3])
                            city = row[4]
                            state = row[5]
                            zip_code = row[6]
                            house_size = int(float(row[7]))
                            prev_sold_date = row[8]
                            price = float(row[9])

                        except Exception:
                            continue

                        property_instance = Property(
                            status, bed, bath, acre_lot, city, state, zip_code,
                            house_size, prev_sold_date, price
                        )

                        if state in US_STATES:
                            self.properties_dict["US States"][state].append(property_instance)
                        elif state in TERRITORIES:
                            self.properties_dict["Territories"][state].append(property_instance)

                    file_loaded = True
            except FileNotFoundError:
                user_input = input(
                    f"File {file_name} not found in {location}. "
                    f"Please enter a valid file name or 'q' to quit: ")
                if user_input.lower() == 'q':
                    print("Exiting program.")
                    exit()
                else:
                    file_name = user_input

    def _create_container(self, header):
        """
        Creates a namedtuple class based on the CSV header.

        Args:
            header (list): A list of column names from the CSV file.

        Returns:
            namedtuple: A namedtuple class named "Property" with fields from the header.
        """
        fields = [field.strip() for field in header]
        Property = namedtuple("Property", fields)
        return Property

    def compute_stats(self, func_name, *args, **kwargs):
        """
        Call a function from the calculate_stats module using class’s data.

        Args:
            func_name (str): The function name in calculate_stats to call.
            *args: Additional positional arguments for the stats function.
            **kwargs: Additional keyword arguments for the stats function.

        Returns:
            Any: The result of the called stats function.

        Raises:
            ValueError: Returns if specified function name doesn't exist in calculate_stats module.
        """
        func = getattr(calculate_stats, func_name, None)
        if not func:
            raise ValueError(f"Function {func_name} not found in calculate_stats module.")
        return func(self.properties_dict, *args, **kwargs)


if __name__ == "__main__":

    file_name = "realtor-data.csv"
    location = os.path.join(os.path.dirname(__file__), "data")
    re_instance = RealEstate(file_name, location)
    print("Loaded data for testing:")
    for group, states in re_instance.properties_dict.items():
        for state, props in states.items():
            print(f"{state}: {len(props)} properties")
