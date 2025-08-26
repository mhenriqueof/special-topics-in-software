from abc import ABC, abstractmethod

class Race(ABC):
    def __init__(self, movement: int, infravision: int, alignment: str, skills: dict[str, str]):
        self.movement = movement
        self.infravision = infravision
        self.alignment = alignment
        self.skills = skills
        
    @abstractmethod
    def story(self) -> str:
        pass
    
    @abstractmethod
    def personality(self) -> str:
        pass
    
    @abstractmethod
    def adventures(self) -> str:
        pass
