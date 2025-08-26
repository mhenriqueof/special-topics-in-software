from classes.thief.thief import Thief

class Ranger(Thief):
    def rangers(self) -> str:
        def __init__(self):
            super().__init__()
            
        text = "A Ranger is a character from the wilderness who patrols and protects a natural or wild area from beasts and monsters. They often have a close bond with animals and possess talents for survival that make them an expert hunter, tracker, and a very competent spy."
        return text
    
    
    def sneak_attack(self) -> str:
        text = ""
        return text

    def hear_noises(self) -> str:
        text = ""
        return text

    def mortal_enemy(self) -> str:
        text = "Assuming their role as a guardian of a wilderness region, they choose an enemy that plagues their territory to combat."
        return text

    def combative(self) -> str:
        text = "The Ranger can now wield large weapons and shields without penalties, but remains limited to wearing Light Armor."
        return text

    def foresight(self) -> str:
        text = "The Ranger is always alert and prepared when in the wilderness. Under these conditions, a Ranger can only be surprised on a roll of 1 on 1d6, and any camp set up by a Ranger in the wilderness will always be of the safe type."
        return text

    def animal_companion(self) -> str:
        text = "A creature from the wilderness adopts the Ranger as an ally and performs favors such as attacking, keeping watch, delivering messages, or similar tasks that are not harmful to itself (for example, not something like killing itself)."
        return text


    def __repr__(self) -> str:
        return f"Ranger"
    