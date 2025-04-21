# Imports
import csv
import os
from collections import namedtuple


class WeatherData:
    """
    Class representing a single weather record.

    Attributes:
        station_id (str): The ID of the weather station.
        date (str): The date of the record in YYYYMMDD format.
        latitude (float): The latitude of the station.
        longitude (float): The longitude of the station.
        max_temp (float): The maximum temperature for the day.
        min_temp (float): The minimum temperature for the day.
        avg_temp (float): The average temperature for the day.

    Methods:
        __init__(self, station_id, date, latitude, longitude, max_temp, min_temp, avg_temp): 
            Initializes WeatherData instance with station_id, date, latitude, longitude, max_temp, min_temp, avg_temp.
        __repr__(self): Provides a developer string representation of WeatherData.
        __str__(self): Returns a user string representation of WeatherData.
        __eq__(self, other): Compares WeatherData for equality.
        __lt__(self, other): Compares WeatherData for less-than.
        __hash__(self): Provides a hash value for WeatherData.
    """

    def __init__(self,
                 station_id,
                 date,
                 latitude,
                 longitude,
                 max_temp,
                 min_temp,
                 avg_temp):
        """
        Inits WeatherData instance.

        Args:
            station_id (str): The ID of the weather station.
            date (str): The date of the record in YYYYMMDD format.
            latitude (float): The latitude of the station.
            longitude (float): The longitude of the station.
            max_temp (float): The maximum temperature for the day.
            min_temp (float): The minimum temperature for the day.
            avg_temp (float): The average temperature for the day.
        """
        self.station_id = station_id
        self.date = date
        self.latitude = latitude
        self.longitude = longitude
        self.max_temp = max_temp
        self.min_temp = min_temp
        self.avg_temp = avg_temp

    def __repr__(self):
        """
        Returns developer string for WeatherData.

        Returns:
            str: A Developer string representation of WeatherData.
        """
        return f"WeatherData('{self.station_id}','{self.date}',{self.latitude},{self.longitude},{self.max_temp},{self.min_temp},{self.avg_temp})"

    def __str__(self):
        """
        Returns user string for WeatherData.

        Returns:
            str: A user string representation of WeatherData.
        """
        return f"WeatherData Station ID: '{self.station_id}', Date: '{self.date}', Latitude: {self.latitude}, Longitude: {self.longitude}, Max Temp: {self.max_temp}, Min Temp: {self.min_temp}, Avg Temp: {self.avg_temp}"

    def __eq__(self, other):
        """
        Checks if two WeatherData's are equal.

        Args:
            other (WeatherData): Another WeatherData instance to compare.

        Returns:
            bool: True if objects are equal, otherwise False.
        """
        if not isinstance(other, WeatherData):
            return NotImplemented

        return (self.station_id, self.date, self.latitude, self.longitude, self.max_temp, self.min_temp, self.avg_temp) == \
               (other.station_id, other.date, other.latitude, other.longitude, other.max_temp, other.min_temp, other.avg_temp)

    def __lt__(self, other):
        """
        Checks two WeatherData objects for less-than.

        Args:
            other (WeatherData): Another WeatherData instance to compare.

        Returns:
            bool: True if this object is less than the other, otherwise False.
        """
        if not isinstance(other, WeatherData):
            return NotImplemented

        if self.station_id != other.station_id:
            return self.station_id < other.station_id

        elif self.date != other.date:
            return self.date < other.date

        elif self.latitude != other.latitude:
            return self.latitude < other.latitude

        elif self.longitude != other.longitude:
            return self.longitude < other.longitude

        elif self.max_temp != other.max_temp:
            return self.max_temp < other.max_temp

        elif self.min_temp != other.min_temp:
            return self.min_temp < other.min_temp

        else:
            return self.avg_temp < other.avg_temp

    def __hash__(self):
        """
        Returns a hash for WeatherData.

        Returns:
            int: The hash value of WeatherData.
        """
        return hash((self.station_id, self.date, self.latitude, self.longitude, self.max_temp, self.min_temp, self.avg_temp))


class WeatherDataCollection:
    """
    Class to hold weather data.

    Arguments:
        None

    Methods:
        __init__(self): Initializes WeatherDataCollection instance and loads data.
        __iter__(self): Iterates though WeatherDataCollection.
        _load_data(self): Loads dataset, parses it, and creates WeatherData objects.
    """

    def __init__(self):
        """
        Inits WeatherDataCollection instance.
        """
        self.data = []
        self._load_data()

    def __iter__(self):
        """
        Iterates through WeatherDataCollection.

        Args:
            None

        Return:
            An iterator over WeatherDataCollection.
        """
        return iter(self.data)

    def _load_data(self):
        """
        Loads the dataset, parses it, and creates WeatherData objects.
        """
        data_file = "Data.txt"

        if not os.path.exists(data_file):
            raise FileNotFoundError(f"Data file '{data_file}' not found.")

        with open(data_file, "r") as file:
            for line in file:
                # Split the line by whitespace
                fields = line.strip().split()

                if len(fields) < 8:
                    continue

                # Extract the relevant fields
                station_id = fields[0]
                date = fields[1]
                # fields[2] is elevation, which we don't use
                longitude = float(fields[3])
                latitude = float(fields[4])
                max_temp = float(fields[5])
                min_temp = float(fields[6])
                avg_temp = float(fields[7])

                # Create a WeatherData object and add it to the collection
                self.data.append(WeatherData(station_id, date, latitude, longitude, max_temp, min_temp, avg_temp))


def main():
    """
    Main function for WeatherDataCollection.

    Prints:
        Each WeatherData instance.
    """
    weather_data = WeatherDataCollection()
    for record in weather_data:
        print(record)


if __name__ == '__main__':
    # Test the WeatherData class
    record1 = WeatherData('94075', '20180101', 40.04, -105.54, -0.8, -6.9, -3.9)
    record2 = WeatherData('94075', '20180101', 40.04, -105.54, -0.8, -6.9, -3.9)
    record3 = WeatherData('94075', '20180102', 40.04, -105.54, 1.8, -12.2, -5.2)
    record4 = WeatherData('94075', '20180103', 40.04, -105.54, 3.2, -7.0, -1.9)

    assert hash(record1) == hash(record2)
    assert record1 == record2
    assert record1 < record3
    assert record3 < record4

    # Run the main function
    main()
