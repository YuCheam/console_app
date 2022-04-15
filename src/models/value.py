from enum import Enum

class ValueType(Enum):
    ALPHA = 'alpha'
    NUMERIC = 'numeric'

class Value():
    def __init__(self, value: str, type: ValueType):
        self.given_form = value
        self.type = type
        self.evaluated_form = value
        

    @property
    def evaluated_form(self):
        return self._evaluated_form
    
    @evaluated_form.setter
    def evaluated_form(self, value):
        if self.type == ValueType.ALPHA:
            self._evaluated_form = eval(value) if value.find("'") != -1 else value
        elif self.type == ValueType.NUMERIC:
            self._evaluated_form = float(value)
