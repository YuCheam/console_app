import argparse
from pathlib import Path

def str_to_path(path_arg):
    path = Path(path_arg)
    if path.suffix != '.csv':
        raise argparse.ArgumentTypeError('Not a .csv file')
    elif not path.is_file():
        raise argparse.ArgumentTypeError('File not found')
    
    return path

def setup_arg_parser(parser: argparse.ArgumentParser):
    parser.description = 'Console application that reads the contents of a csv file from disk and prints the numeric and/or alphabetic values within the file depending on the sorting filter request'
    parser.add_argument('csv_path', type=str_to_path, help='Path to .csv file')
    parser.add_argument('value_type', choices=['alpha', 'numeric', 'both'])
    parser.add_argument('sort_order', choices=['ascending', 'descending'])

    return parser