from classes.klass import Klass, Weapon, Armor, MagicItem, Ability

class Thief(Klass):
    def __init__(self):
        super().__init__(
            weapon = [Weapon.MEDIUM_WEAPONS.value, Weapon.SMALL_WEAPONS.value],
            armor = [Armor.LIGHT_ARMOR.value],
            magic_items = [MagicItem.PROTECTION_SCROLL.value]
        )

    def abilities(self) -> list[dict]:
        return [
            Ability.SNEAK_ATTACK.value,
            Ability.HEAR_NOISES.value,
            Ability.THIEF_TALENTS.value
        ]
    
    def arc(self) -> str:
        return "A low-level Thief is, above all, a survivor. They've overcome challenges through cunning and dexterity, and while they have a long way to go, their skills will let them evolve from a barefoot pickpocket to a feared and respected master thief. To achieve this, they must practice constantly, becoming more efficient, faster, and deadlier. This is how they climb the dangerous hierarchy of the criminal underworld, where the most influential and powerful, rather than the most skilled, are the ones who succeed."
