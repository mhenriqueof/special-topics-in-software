from character.attributes.attribute_generator import AttributeGenerator
from character.races import Elf, Halfling, Human
from character.classes import Mage, Thief, Warrior

class CharacterGenerator:
    """Class responsible for creating the attributes, race and class of the character."""
    
    def generate_attributes(self, style: str) -> dict:
        ag = AttributeGenerator()
        if style == 'Classic':
            return ag.attributes_distribution('3d6')
        elif style == 'Adventure':
            return ag.attributes_distribution('3d6', choose=True)
        elif style == 'Heroic':
            return ag.attributes_distribution('4d6', choose=True, drop_lowest=True)
        return {}
    
    def generate_race(self, race: str):
        if race == 'Elf': return Elf()
        elif race == 'Halfling': return Halfling()
        elif race == 'Human': return Human()
    
    def generate_class(self, klass: str):
        if klass == 'Mage': return Mage()
        elif klass == 'Thief': return Thief()
        elif klass == 'Warrior': return Warrior()
        