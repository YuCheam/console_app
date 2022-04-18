from abc import ABC, abstractmethod
from functools import total_ordering

@total_ordering
class Value(ABC):
    """ Abstract Base Class to represent data given in csv """
    def __init__(self, value: str):
        self.given_form = value
        self.evaluated_form = value
        
    @property
    @abstractmethod
    def evaluated_form(self, value):
        """
        Python evaluable data type representation of value

        Arguments:
            value -- str value
        """
        pass

    @property
    @abstractmethod
    def type_str(self):
        """
        String representation of type
        """
        pass
    
    @staticmethod
    def _is_instance(other):
        """
        Checks if given object is a Value instance

        Arguments:
            other -- object to verify

        Returns:
            boolean
        """
        return (hasattr(other, 'given_form') and hasattr(other, 'evaluated_form')
            and hasattr(other, 'type_str'))
    
    @abstractmethod
    def is_valid_value(value: str):
        """
        Checks if given string value can be used to initialize Value type

        Arguments:
            value -- string value
        """
        pass

    # Override for custom sorting of type
    def __eq__(self, other):
        if not self._is_instance(other):
            return False
        return ((self.given_form, self.evaluated_form) == 
                (other.given_form, other.evaluated_form))
    
    def __lt__(self, other):
        if not self._is_instance(other):
            raise TypeError(f'Incomparible types')

        if self.type_str != other.type_str:
            if self.type_str == 'alpha':
                return False
            else:
                return True
        else:
            return self.evaluated_form < other.evaluated_form

class AlphaValue(Value):
    """ Values of that are wrapped in '' or are of alpha type """
    type_str = "alpha"

    def __init__(self, value: str):
        super().__init__(value)

    @property
    def evaluated_form(self):
        return self._evaluated_form

    @evaluated_form.setter
    def evaluated_form(self, value):
        self._evaluated_form = eval(value) if value.find("'") != -1 else value
    
    @staticmethod
    def is_valid_value(value: str):
        return value.find("'") != -1 or value.isalpha()

class NumericValue(Value):
    """ Values that are numeric """
    type_str = "numeric"

    def __init__(self, value: str):
        super().__init__(value)

    @property
    def evaluated_form(self):
        return self._evaluated_form
    
    @evaluated_form.setter
    def evaluated_form(self, value):
        self._evaluated_form = float(value)

    @staticmethod
    def is_valid_value(value: str):
        try:
            float(value)
            return value.find("'") == -1 and True 
        except ValueError:
            return False