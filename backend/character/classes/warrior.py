from classes.klass import Klass, Weapon, Armor, MagicItem, Ability

class Warrior(Klass):
    def __init__(self):
        super().__init__(
            weapon = [Weapon.ALL.value],
            armor = [Armor.ALL.value],
            magic_items = [MagicItem.PROTECTION_SCROLL.value]
        )

    def abilities(self) -> list[dict]:
        return [
            Ability.BLOCK.value,
            Ability.EXTRA_ATTACK.value,
            Ability.WEAPON_MASTERY.value
        ]
    
    def arc(self) -> str:
        return "The low-level Warrior is an ordinary man with some skill in weapons who chooses the path of adventure. Over time, he becomes the hero of his village, gaining experience, wealth, and fame that reaches far beyond his homeland. His journey is focused on building a reputation as a fearless military leader, surviving increasingly dangerous missions, and forging strategic—sometimes personal—bonds with powerful nobles. By presenting himself as a bold and capable combatant, he lays the foundation for a future of greatness. The nobility awaits him, and all it represents—power, wealth, and comfort—depends entirely on his ability to fight and stand out."
    