from abc import ABC, abstractmethod
from classes.klass_armors import Armor
from classes.klass_magic_items import MagicItem
from classes.klass_weapons import Weapon
from classes.klass_abilities import Ability

class Klass(ABC): # "K" to avoid 'class' of Python
    def __init__(self, weapon: list[str], armor: list[str], magic_items: list[str]):
        self.__weapon = weapon
        self.__armor = armor
        self.__magic_items = magic_items
    
    @property
    def weapon(self) -> list[str]:
        return self.__weapon
    @property
    def armor(self) -> list[str]:
        return self.__armor
    @property
    def magic_items(self) -> list[str]:
        return self.__magic_items
    
    @abstractmethod
    def abilities(self) -> list[dict]:
        """Returns a list of dictionaries with all abilities of the class (active skills)."""
        pass
    
    @abstractmethod
    def arc(self) -> str:
        """Returns a description of the class."""
        pass
    
    def __repr__(self) -> str:
        return self.__class__.__name__
