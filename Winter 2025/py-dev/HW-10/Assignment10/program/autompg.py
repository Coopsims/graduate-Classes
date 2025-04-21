# Imports
import csv
import os
from collections import namedtuple
from program.custom_logger import my_logger


class AutoMPG:

    """
    Class representing a single car's fuel efficiency.

    Attributes:
        make (str): The manufacturer of a car.
        model (str): The model of a car.
        year (int): The manufacturing year of a car.
        mpg (float): The fuel efficiency (miles per gallon).

    Methods:
        __init__(self, make, model, year, mpg): Initializes  AutoMPG instance with make, model, year, and mpg.
        __repr__(self):Provides a developer string representation of AutoMPG.
        __str__(self): Returns a user string representation of AutoMPG.
        __eq__(self, other):Compares AutoMPG for equality.
        __lt__(self, other):Compares AutoMPG for less-than.
        __hash__(self): Provides a hash value for AutoMPG.
    """

    def __init__(self,
                 make,
                 model,
                 year,
                 mpg):

        """
        Inits AutoMPG instance.

        Args:
            make (str): Manufacturer of the car.
            model (str): Model of the car.
            year (int): Manufacturing year of the car.
            mpg (float): Fuel efficiency in miles per gallon.
        """

        self.make = make
        self.model = model
        self.year = year
        self.mpg = mpg

    def __repr__(self):

        """
        Returns developer string for AutoMPG.

        Returns:
            str: A Developer string representation of AutoMPG.
        """

        return f"AutoMPG('{self.make}','{self.model}',{self.year},{self.mpg})"


    def __str__(self):

        """
        Returns user string for AutoMPG.

        Returns:
            str: A user string representation of AutoMPG.
        """

        return f"AutoMPG Car Make: '{self.make}', Model: '{self.model}', Year: {self.year}, MPG: {self.mpg}"


    def __eq__(self, other):

        """
        Checks if two AutoMPG's are equal.

        Args:
            other (AutoMPG): Another AutoMPG instance to compare.

        Returns:
            bool: True if objects are equal, otherwise False.
        """

        if not isinstance(other, AutoMPG):
            return NotImplemented

        return (self.make, self.model, self.year, self.mpg) == (other.make, other.model, other.year, other.mpg)

    def __lt__(self, other):

        """
        Checks two AutoMPG objects for less-than.

        Args:
            other (AutoMPG): Another AutoMPG instance to compare.

        Returns:
            bool: True if this object is less than the other, otherwise False.
        """

        if not isinstance(other, AutoMPG):
            return NotImplemented

        if self.make != other.make:
            return self.make < other.make

        elif self.model != other.model:
            return self.model < other.model

        elif self.year != other.year:
            return self.year < other.year

        else:
            return self.mpg < other.mpg

    def __hash__(self):

        """
        Returns a hash for AutoMPG.

        Returns:
            int: The hash value of AutoMPG.
        """

        return hash((self.make, self.model, self.year, self.mpg))


class AutoMPGData:
    """
    Class to hold car data.

    Arguments:
        sort_year (bool): Whether to sort by year.
        sort_mpg (bool): Whether to sort by MPG.
        log_path (str): Folder path where the log file will be written.

    Methods:
        __init__: Initializes AutoMPGData instance and loads data.
        __iter__: Iterates though AutoMPGData.
        sort_data: Sorts data by year, mpg, or both.
        save_data: Saves data to file with appropriate name, logging status.
        _load_data: Loads cleaned dataset or calls _clean_data if missing.
        _clean_data: Cleans the original dataset, saves cleaned data.
    """

    def __init__(self, sort_year=False, sort_mpg=False, log_path=None):
        """
        Modified constructor now takes sort_year and sort_mpg booleans,
        and an optional log_path for logging.
        """
        self.sort_year = sort_year
        self.sort_mpg = sort_mpg
        self.logger = None

        if log_path:
            self.logger = my_logger(log_path)

        self.data = []
        self._load_data()

        if self.logger:
            self.logger.debug("Data loaded.")

        self.working = False

    def __iter__(self):
        """
        Iterates through AutoMPGData.
        Returns:
            An iterator over AutoMPGData.
        """
        return iter(self.data)

    def sort_data(self):
        """
        Sorts self.data by year, mpg, or both, based on self.sort_year / self.sort_mpg.
        Sets self.working = True if a sort actually occurs.
        """
        if self.sort_year and self.sort_mpg:
            self.data.sort(key=lambda car: (car.year, car.mpg))
            self.working = True
        elif self.sort_year:
            self.data.sort(key=lambda car: car.year)
            self.working = True
        elif self.sort_mpg:
            self.data.sort(key=lambda car: car.mpg)
            self.working = True

        return self.data

    def save_data(self, save_path):
        """
        Saves the data to the given folder path with the requested filename
        (auto.data.txt, auto.data.year.txt, auto.data.mpg.txt, or auto.data.year.mpg.txt).
        Logs a message describing how it was sorted.
        """
        if self.sort_year and self.sort_mpg:
            filename = "auto.data.year.mpg.txt"
            sort_text = "year.mpg"
        elif self.sort_year:
            filename = "auto.data.year.txt"
            sort_text = "year"
        elif self.sort_mpg:
            filename = "auto.data.mpg.txt"
            sort_text = "mpg"
        else:
            filename = "auto.data.txt"
            sort_text = "not sorted"

        full_path = os.path.join(save_path, filename)
        with open(full_path, "w") as f:
            for car in self.data:
                # Year's last two digits for column #7
                f.write(f"{car.mpg} N/A N/A N/A N/A N/A {str(car.year)[-2:]} N/A \"{car.make} {car.model}\"\n")

        if self.logger:
            if sort_text == "not sorted":
                self.logger.debug("Data saved, not sorted.")
            else:
                self.logger.debug(f"Data saved, sorted by {sort_text}")

    def _load_data(self):
        """
        Loads the cleaned dataset, parses it, and creates AutoMPG objects.
        If cleaned file doesn't exist, generate one using _clean_data().
        """
        base_dir = os.path.dirname(__file__)  # autompg.py's directory
        clean_file = os.path.join(base_dir, "data", "auto-mpg.clean.txt")

        if not os.path.exists(clean_file):
            self._clean_data()

        Record = namedtuple("Record", [
            "mpg", "cylinders", "displacement", "horsepower",
            "weight", "acceleration", "model_year", "origin", "car_name"
        ])

        with open(clean_file, "r") as file:
            reader = csv.reader(file, delimiter=" ", skipinitialspace=True)
            for row in reader:
                # skip incomplete lines
                if len(row) < 9:
                    continue

                record = Record(*row[:9])
                car_name = record.car_name.strip('"').split(" ", 1)
                make = car_name[0]
                model = car_name[1] if len(car_name) > 1 else ""

                # Convert '79' to 1979
                full_year = int("19" + record.model_year)

                self.data.append(AutoMPG(
                    make=make,
                    model=model,
                    year=full_year,
                    mpg=float(record.mpg)
                ))

    def _clean_data(self):
        """
        Cleans the original dataset and saves it to auto-mpg.clean.txt.
        """
        base_dir = os.path.dirname(__file__)  # directory containing autompg.py
        input_file = os.path.join(base_dir, "data", "auto-mpg.data.txt")
        output_file = os.path.join(base_dir, "data", "auto-mpg.clean.txt")

        with open(input_file, "r") as infile, open(output_file, "w") as outfile:
            for line in infile:
                outfile.write(line.expandtabs(1))


def main():
    """
    Main function for AutoMPGData.

    Prints:
        Each AutoMPG instance.
    """
    auto_data = AutoMPGData()
    for car in auto_data:
        print(car)


if __name__ == '__main__':



    car1 = AutoMPG(make="Toyota", model="Corolla", year=2020, mpg=30.5)
    car2 = AutoMPG(make="Toyota", model="Corolla", year=2020, mpg=30.5)
    car3 = AutoMPG(make="Ferrari", model="488 Pista", year=2014, mpg=24)
    car4 = AutoMPG(make="Ferrari", model="F90", year=2019, mpg=28)

    assert hash(car1) == hash(car2)
    assert car1 == car2
    assert car3 < car1
    assert car3 < car4

    car1 = AutoMPG("Toyota", "Corolla", 2015, mpg=30.5)
    car2 = AutoMPG("Honda", "Civic", 2018, mpg=30.5)
    car3 = AutoMPG("Ford", "Focus", 2012, mpg=30.5)

    assert car1 > car2
    assert car3 < car1

    main()