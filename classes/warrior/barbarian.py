from classes.warrior.warrior import Warrior

class Barbarian(Warrior):
    def __init__(self):
        super().__init__()
        self.armor = ["Only Leather Armor"],
        self.magic_items = ["None"]
        
    def barbarians(self) -> str:
        text = "Unlike those who live in civilization, the Barbarians’ exposure to harsh elements has honed their instincts, athletic prowess, and resilience beyond the ordinary. However, the price has been paid in superstition, lack of formal education, and a constant distrust of arcane magic."
        return text
    
    
    def barbarian_vigor(self) -> str:
        text = "Barbarian Vigor: At each level, the Barbarian gains +2 bonus hit points (in addition to the Warrior hit point table) and a +2 bonus to their JPC."
        return text

    def wild_talents(self) -> str:
        text = "Wild Talents: The Barbarian gains certain abilities tied to their life in the untamed wilderness. [Climb and Natural Camouflage]"
        return text

    def wild_surprise(self) -> str:
        text = "Wild Surprise: The Barbarian can surprise enemies in natural environments with a 1-4 chance on a 1d6 roll, even when ambushing with non-Barbarian allies."
        return text

    def totem_strength(self) -> str:
        text = "Totem Strength: The Barbarian can strike any creature that requires a +1 or better magical weapon to be harmed."
        return text


    def __repr__(self) -> str:
        return f"Barbarian"
    