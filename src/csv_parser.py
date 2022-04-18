import csv
from pathlib import Path

class CsvParser():
    """
    Class to parse csv files
    ...
    
    Attributes
    ----------
    file: Path
        path to csv file
    
    Methods
    -------
    get_data():
        parse csv and get data in python list format
    """

    def __init__(self, csv_file: Path):
        self.file = csv_file
    

    def get_data(self):
        """
        Parse csv and get data in python list format

        Returns:
            list of values from csv
        """
        values = []
        with open(self.file) as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                values.extend(row)
        return values
