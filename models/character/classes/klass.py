from abc import ABC, abstractmethod
from .utils.weapons import Weapon
from .utils.armors import Armor
from .utils.magic_items import MagicItem

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
    
    @property
    @abstractmethod
    def arc(self) -> str:
        """Returns a description of the class."""
        pass
    
    @property
    @abstractmethod
    def abilities(self) -> dict:
        """Returns a dictionary with all abilities of the class (active skills)."""
        pass
    
    def __repr__(self) -> str:
        return self.__class__.__name__
