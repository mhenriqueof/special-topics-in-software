from abc import ABC, abstractmethod

class Classs(ABC):
    def __init__(self, weapon: list[str], armor: list[str], magic_items: list[str]):
        self.weapon = weapon
        self.armor = armor
        self.magic_items = magic_items
    
    @abstractmethod
    def lore(self) -> str:
        pass
    