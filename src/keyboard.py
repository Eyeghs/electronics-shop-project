import sys
sys.path.insert(0, '..')
from src.item import Item
from src.Mixin import ChangeLan

class Keyboard(Item,ChangeLan):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        self._language = 'EN'
        
    def __repr__(self):
        return f"Keyboard('{self.name}', {self.price}, {self.quantity})"
        
    @property
    def language(self):
        return self._language
    
    @language.setter
    def language(self, value):
        if value not in ['EN', 'RU']:
            raise AttributeError
        self._language = value
        