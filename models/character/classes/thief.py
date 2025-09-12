from .klass import Klass, Weapon, Armor, MagicItem

class Thief(Klass):
    def __init__(self):
        super().__init__(
            weapon = [Weapon.MEDIUM_WEAPONS.value, Weapon.SMALL_WEAPONS.value],
            armor = [Armor.LIGHT_ARMOR.value],
            magic_items = [MagicItem.PROTECTION_SCROLL.value]
        )
        
    @property
    def arc(self) -> str:
        return "A low-level Thief is, above all, a survivor. They've overcome challenges through cunning and dexterity, and while they have a long way to go, their skills will let them evolve from a barefoot pickpocket to a feared and respected master thief. To achieve this, they must practice constantly, becoming more efficient, faster, and deadlier. This is how they climb the dangerous hierarchy of the criminal underworld, where the most influential and powerful, rather than the most skilled, are the ones who succeed."
    
    @property
    def abilities(self) -> dict:
        return {
            "Sneak Attack": "When the Thief attacks after approaching the enemy stealthily, they can make a very easy attack, dealing double damage.",
            "Hear Noises": "The Thief can detect sounds such as a conversation on the other side of a door or the approach of monsters. To do so, they must be in a quiet environment, such as a dungeon, and outside of combat.",
            "Thief Talents": "Thieves possess certain abilities that represent their main fields of expertise. They start with 2 points in each of the five talents and receive 2 additional points to distribute as they wish."
        }
        