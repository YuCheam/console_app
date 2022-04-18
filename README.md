# Console_App
Console application that reads the contents of a csv (comma separated value) file from disk and prints the numeric and/or alphabetic values within the file depending on what the user requests.

## Usage
To use the console application you must make sure that you are in the same directory as *console_app.py* file. Run the following command in the shell (depending on python version one of them should be valid):

`python console_app.py <path/to/csv_file> <value_type> <sort_order>`

`py console_app.py <path/to/csv_file> <value_type> <sort_order>`

Where valid inputs for *value_type* are [alpha, numeric, both] and *sort_order* are [ascending, descending]

## Limitations
Non base-10 types of numeric data not supported e.g binary, hexadecimal, octal
- Python considers 'A' and '0xA' to be valid hexadecimal inputs. However 'A' can also be considered a valid alpha type
- To implement this functionality we would need to ensure non base-10 inputs are prefixed with '0b', '0x' and/or' '0o'

Symbols that are wrapped in quotations are valid alpha types and can be sorted however *symbols that are not wrapped in quotations* will cause an ValueTypeError
- Valid Input: "'a','@',b,1"
- Invalid Input: "'a',@,b,1"
