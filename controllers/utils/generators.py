from models.utils.dice_roller import DiceRoller
from models.character.races import Elf, Halfling, Human
from models.character.classes import Mage, Thief, Warrior
from models.character.character import Character

class Generator:
    """Class with methods to instantiate classes."""
    
    @staticmethod
    def generate_dice_rolls(style: str) -> list[int]:
        if style == 'Classic' or style == 'Adventure':
            return DiceRoller.roll('3d6')
        else: 
            return DiceRoller.roll('4d6')
    
    def generate_character(self, name: str, attributes: dict, race: str, klass: str):  
        return Character(
            name,
            attributes,
            self.generate_race(race),
            self.generate_class(klass)
        )
    
    def generate_race(self, race: str):
        if race == 'Elf': return Elf()
        elif race == 'Halfling': return Halfling()
        else: return Human()
        
    def generate_class(self, klass: str):
        if klass == 'Mage': return Mage()
        elif klass == 'Thief': return Thief()
        else: return Warrior()
        