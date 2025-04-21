# Imports
import csv
import os
from collections import namedtuple


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

        return f"AutoMPG('{self.make}','{self.model}',{self.year},{self.mpg})"


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
        None

    Methods:
        __init__(self): Initializes AutoMPGData instance and loads data.
        __iter__(self): Iterates though AutoMPGData.
        _load_data(self): Loads cleaned dataset, parses it, and creates AutoMPG objects.
        _clean_data(self): Cleans the original dataset and saves cleaned data to a new file.
    """

    def __init__(self):

        """
        Inits AutoMPG instance.

        """

        self.data = []
        self._load_data()

    def __iter__(self):

        """
        Iterates through AutoMPGData.

        Args:
            None

        Return:
            An iterator over AutoMPGData.
        """

        return iter(self.data)

    def _load_data(self):

        """
        Loads the cleaned dataset, parses it, and creates AutoMPG objects.

        If cleaned file doesn't exist, generate one using `_clean_data`.
        """

        clean_file = "auto-mpg.clean.txt"

        if not os.path.exists(clean_file):
            self._clean_data()

        Record = namedtuple("Record", ["mpg", "cylinders", "displacement", "horsepower", "weight",
                                                           "acceleration", "model_year", "origin", "car_name"])

        with open(clean_file, "r") as file:
            reader = csv.reader(file, delimiter=" ", skipinitialspace=True)

            for row in reader:

                if len(row) < 9:

                    continue

                record = Record(*row[:9])
                car_name = record.car_name.strip('"').split(" ", 1)

                make = car_name[0]
                model = car_name[1] if len(car_name) > 1 else ""

                self.data.append(AutoMPG(make, model, int("19" + record.model_year), float(record.mpg)))

    def _clean_data(self):

        """
        Cleans the original dataset and saves cleaned data to a new file.

        Args:
            None

        Returns:
            None
        """

        input_file = "auto-mpg.data.txt"
        output_file = "auto-mpg.clean.txt"

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
