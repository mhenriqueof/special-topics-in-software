from ..classs import Classs

class Thief(Classs):
    def __init__(self):
        super().__init__(
            weapon = ['Medium Weapons', 'Small Weapons'],
            armor = ['Only Light Armor'],
            magic_items = ['Only Protection Scroll']
        )
    
    def lore(self) -> str:
        text = "A low-level Thief is, above all, a survivor. They've overcome challenges through cunning and dexterity, and while they have a long way to go, their skills will let them evolve from a barefoot pickpocket to a feared and respected master thief. To achieve this, they must practice constantly, becoming more efficient, faster, and deadlier. This is how they climb the dangerous hierarchy of the criminal underworld, where the most influential and powerful, rather than the most skilled, are the ones who succeed."
        return text
    
    
    def sneak_attack(self) -> str:
        text = "Sneak Attack: When the Thief attacks after approaching the enemy stealthily, they can make a very easy attack, dealing double damage."
        return text

    def hear_noises(self) -> str:
        text = "Hear Noises: The Thief can detect sounds such as a conversation on the other side of a door or the approach of monsters. To do so, they must be in a quiet environment, such as a dungeon, and outside of combat."
        return text

    def thief_talents(self) -> str:
        text = "Thief Talents: Thieves possess certain abilities that represent their main fields of expertise. They start with 2 points in each of the five talents and receive 2 additional points to distribute as they wish."
        return text


    def __repr__(self) -> str:
        return f"Thief"
    