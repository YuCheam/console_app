import argparse

from src.arg_parser import setup_arg_parser
from src.csv_parser import CsvParser
from src.models.sorter import Sorter

if __name__ == "__main__":
    parser = setup_arg_parser(argparse.ArgumentParser())
    args = vars(parser.parse_args())

    data_to_process = CsvParser(args['csv_path']).get_data()

    sorter = Sorter(data_to_process)
    sorter.set_filter(args['value_type'])
    sorter.set_sort_order(args['sort_order'])

    sorted_values = sorter.execute()
    print(', '.join(sorted_values))
    