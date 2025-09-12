from models.character.races import Race
from models.character.classes import Klass

class Character:
    """Represents a character with their name, attributes, race and class."""
    def __init__(self, name: str, attributes: dict[str, int], race: Race, klass: Klass):
        self.__name = name
        self.__attributes = attributes
        self.__race = race
        self.__klass = klass # "K" to avoid 'class' of Python
        
    @property
    def name(self) -> str:
        return self.__name
    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @property
    def attributes(self) -> dict[str, int]:
        return self.__attributes
    @attributes.setter
    def attributes(self, attributes: dict[str, int]) -> None:
        self.__attributes = attributes

    @property
    def race(self):
        return self.__race
    @race.setter
    def race(self, race) -> None:
        self.__race = race

    @property
    def klass(self):
        return self.__klass
    @klass.setter
    def klass(self, klass) -> None:
        self.__klass = klass
        
    def attribute_value_modifier(self, value: int) -> str:
        """Returns a modifier value for the attributes."""
        if value >= 19: return '+4'
        elif value >= 17: return '+3'
        elif value >= 15: return '+2'
        elif value >= 13: return '+1'
        elif value >= 9: return '0'
        elif value >= 6: return '-1'
        elif value >= 4: return '-2'
        elif value >= 2: return '-3'
        return '0'

    # Magic method 
    def __repr__(self) -> str:
        return f"Character(name='{self.name}',attributes={self.attributes},race={self.race},class={self.klass})"
    