from typing import List
from src.models.value import AlphaValue, NumericValue

class Sorter():
    """ Class to sort values based on set filter and sort order """

    def __init__(self, values: List, filter_type="both", sort_order="ascending"):
        """
        Initializes Sorter class

        Arguments:
            values -- list of values to sort; generated from csv parser

        Keyword Arguments:
            filter_type --  value type to filter by (default: {"both"})
            sort_order -- order to sort values (default: {"ascending"})
        """
        self.values = values
        self.filter_type = filter_type
        self.sort_order = sort_order
    
    @property
    def values(self):
        return self._values
    
    @values.setter
    def values(self, values_list):
        self._values = []
        for value in values_list:
            if NumericValue.is_valid_value(value):
                self._values.append(NumericValue(value))
            elif AlphaValue.is_valid_value(value):
                self._values.append(AlphaValue(value))
            else:
                raise ValueError(f'{value} not recognized')
    
    def set_filter(self, filter_type):
        """
        Sets filter of sorter by value type

        Arguments:
            filter_type -- value type to filter by
        """
        self.filter_type = filter_type
    
    def set_sort_order(self, sort_order):
        """
        Sets sort order

        Arguments:
            sort_order -- order to sort values by
        """
        self.sort_order = sort_order
    
    def _filter_values(self):
        if self.filter_type == 'both':
            self._filtered_values = self.values
        else:
            self._filtered_values = list(filter(lambda value: value.type_str == self.filter_type, self.values))
    
    def execute(self):
        """
        Executes sorting on given values list with by filter and sort order

        Returns:
            list of sorted values
        """
        self._filter_values()

        if self.sort_order == 'ascending':
            sorted_values = sorted(self._filtered_values)
            
        elif self.sort_order == 'descending':
            sorted_values = sorted(self._filtered_values, reverse=True)
        
        return list(map(lambda x: x.given_form, sorted_values))