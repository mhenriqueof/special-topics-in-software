from ..classs import Classs

class Warrior(Classs):
    def __init__(self):
        super().__init__(
            weapon = ['All'],
            armor = ['All'],
            magic_items = ['Only Protection Scroll']
        )
    
    def lore(self) -> str:
        text = "The low-level Warrior is an ordinary man with some skill in weapons who chooses the path of adventure. Over time, he becomes the hero of his village, gaining experience, wealth, and fame that reaches far beyond his homeland. His journey is focused on building a reputation as a fearless military leader, surviving increasingly dangerous missions, and forging strategic—sometimes personal—bonds with powerful nobles. By presenting himself as a bold and capable combatant, he lays the foundation for a future of greatness. The nobility awaits him, and all it represents—power, wealth, and comfort—depends entirely on his ability to fight and stand out."
        return text
    
    
    def block(self) -> str:
        text = "A Warrior may, after being hit by a physical attack and before the damage roll is made, choose to sacrifice their shield or a weapon they are wielding to absorb all the damage from that attack."
        return text
    
    def weapon_mastery(self) -> str:
        text = "The Warrior becomes a master with one weapon of their choice, gaining a +1 bonus to damage rolls made with that weapon."
        return text
    
    def extra_attack(self) -> str:
        text = "At 6th level, a Warrior gains a second attack, either melee or ranged, using the same weapon with which they have mastery."
        return text
    
    
    def __repr__(self) -> str:
        return f"Warrior"
    