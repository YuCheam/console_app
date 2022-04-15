import argparse

from helpers import setup_arg_parser
from csv_parser import CsvParser
from models.value_filter import Sorter

if __name__ == "__main__":
    parser = setup_arg_parser(argparse.ArgumentParser())
    args = vars(parser.parse_args())

    values_to_process = CsvParser(args['csv_path']).get_data()

    sorter = Sorter(values_to_process, args['value_type'])

    if args['sort_order'] == 'ascending':
        sorter.print_ascending()
    else:
        sorter.print_descending()
    