import csv
from pathlib import Path

class CsvParser():

    def __init__(self, csv_file: Path):
        self.file = csv_file
    
    # TODO: ask about double quotation marks
    def get_data(self):
        values = []
        with open(self.file) as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                values.extend(row)
        return values
