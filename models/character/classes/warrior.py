from .klass import Klass, Weapon, Armor, MagicItem

class Warrior(Klass):
    def __init__(self):
        super().__init__(
            weapon = [Weapon.ALL.value],
            armor = [Armor.ALL.value],
            magic_items = [MagicItem.PROTECTION_SCROLL.value]
        )
        
    @property
    def arc(self) -> str:
        return "The low-level Warrior is an ordinary man with some skill in weapons who chooses the path of adventure. Over time, he becomes the hero of his village, gaining experience, wealth, and fame that reaches far beyond his homeland. His journey is focused on building a reputation as a fearless military leader, surviving increasingly dangerous missions, and forging strategic—sometimes personal—bonds with powerful nobles. By presenting himself as a bold and capable combatant, he lays the foundation for a future of greatness. The nobility awaits him, and all it represents—power, wealth, and comfort—depends entirely on his ability to fight and stand out."
    
    @property
    def abilities(self) -> dict:
        return {
            "Block": "A Warrior may, after being hit by a physical attack and before the damage roll is made, choose to sacrifice their shield or a weapon they are wielding to absorb all the damage from that attack.",
            "Extra Attack": "At 6th level, a Warrior gains a second attack, either melee or ranged, using the same weapon with which they have mastery.",
            "Weapon Mastery": "The Warrior becomes a master with one weapon of their choice, gaining a +1 bonus to damage rolls made with that weapon."
        }
        