from abc import ABC, abstractmethod
from enum import Enum

class Alignment(Enum):
    ANY = 'Any'
    NEUTRAL = 'Neutral'
    ORDER = 'Order'

class Race(ABC):
    """Abstract class for all races."""
    def __init__(self, movement: int, infravision: int, alignment: Alignment):
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
    def alignment(self) -> Alignment:
        return self.__alignment
    

    @abstractmethod
    def overview(self) -> str:
        """Returns a brief description of the race (origins, personality and adventures)."""
        pass
    
    @abstractmethod
    def talents(self) -> list[str]:
        """Returns a list with all talents of the race (passive skills)."""
        pass


    def __repr__(self) -> str:
        return (f"{self.__class__.__name__}: "
                f"movement={self.movement}, "
                f"infravision={self.infravision}, "
                f"alignment={self.alignment.value}")
        