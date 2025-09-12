from abc import ABC, abstractmethod
from .utils.alignments import Alignment
from .utils.profiles import Profile

class Race(ABC):
    """Abstract class for all races."""
    def __init__(self, movement: int, infravision: int, alignment: str):
        self.__movement = movement
        self.__infravision = infravision
        self.__alignment = alignment
        
    @property
    def movement(self) -> int:
        return self.__movement
    @property
    def infravision(self) -> int:
        return self.__infravision
    @property
    def alignment(self) -> str:
        return self.__alignment
    
    @property
    @abstractmethod
    def profile(self) -> dict:
        """Returns a dictionary with lore, personality and adventures of the race."""
        pass
    
    @property
    @abstractmethod
    def talents(self) -> dict:
        """Returns a dictionary with all talents of the race (passive skills)."""
        pass
    
    def __repr__(self) -> str:
        return self.__class__.__name__
