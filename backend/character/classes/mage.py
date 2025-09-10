from classes.klass import Klass, Weapon, Armor, MagicItem, Ability

class Mage(Klass):
    def __init__(self):
        super().__init__(
            weapon = [Weapon.SMALL_WEAPONS.value],
            armor = [Armor.NO_ARMOR.value],
            magic_items = [MagicItem.ALL.value]
        )
        
    def abilities(self) -> list[dict]:
        return [
            Ability.ARCANE_SPELLS.value,
            Ability.READ_MAGIC.value,
            Ability.DETECT_MAGIC.value
        ]
    
    def arc(self) -> str:
        return "A low-level Wizard is a fanatic when it comes to arcane knowledge. The road, discomfort, cold, dark dungeons, and even the tedious company of their adventuring party are all a small price to pay for access to knowledge, in a career where power is measured by what one knows. Beneath the glimmer of precious metals, you know there is ancestral knowledge to be acquired. Each desecrated ancient tomb hides long-lost secrets, and that is why you chose to adventure. In time, your knowledge will be converted into power, and this will make you feared. After all, it's natural to be afraid of what you don't understand, and that's when you will have enough knowledge to settle somewhere and spend your days studying all you have collected throughout your life."    
