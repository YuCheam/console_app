from abc import ABC, abstractmethod
from typing import List

from models.value import ValueType, Value

def is_float(obj) -> bool:
        try:
            float(obj)
            return True
        except ValueError:
            return False

class ValueFilter(ABC):
    @abstractmethod
    def execute(self, values: List) -> List:
        pass

class NumericFilter(ValueFilter):

    def execute(self, values: List):
        filtered_values = filter(lambda x: (x.find("'") == -1 and is_float(x)), values)
        converted_values = map(lambda x: Value(x, ValueType.NUMERIC), filtered_values)
        return list(converted_values)

class AlphaFilter(ValueFilter):
    def execute(self, values: List):
        filtered_values = filter(lambda x: (x.find("'") != -1 or x.isalpha()), values)
        converted_values = map(lambda x: Value(x, ValueType.ALPHA), filtered_values)
        return list(converted_values)

class BothFilter(ValueFilter):
    def execute(self, values: List):
        return_values = []
        filtered_values = filter(lambda x: (x.find("'") == -1 and is_float(x)), values)
        converted_values = map(lambda x: Value(x, ValueType.NUMERIC), filtered_values)
        return_values.extend(list(converted_values))

        filtered_values = filter(lambda x: (x.find("'") != -1 or x.isalpha()), values)
        converted_values = map(lambda x: Value(x, ValueType.ALPHA), filtered_values)
        return_values.extend(list(converted_values))

        return return_values


class Sorter():

    def __init__(self, values: List, filter: str):
        self.values = values
        self.value_filter = filter
        self._filtered_values = self._value_filter.execute(self.values)

    @property
    def value_filter(self):
        return self._value_filter
    
    @value_filter.setter
    def value_filter(self, filter: str):
        if filter == 'alpha':
            self._value_filter = AlphaFilter()
        elif filter == 'numeric':
            self._value_filter = NumericFilter()
        elif filter == 'both':
            self._value_filter = BothFilter()
        else:
            raise ValueError(f'Value type {filter} not supported')

    def print_ascending(self):
        sorted_values = sorted(self._filtered_values, key=lambda x: x.evaluated_form)
        given_values = map(lambda x: x.given_form, sorted_values)
        print(','.join(given_values))

    def print_descending(self):
        sorted_values = sorted(self._filtered_values, key=lambda x: x.evaluated_form, reverse=True)
        given_values = map(lambda x: x.given_form, sorted_values)
        print(','.join(given_values))