from ..classs import Classs

class Mage(Classs):
    def __init__(self):
        super().__init__(
            weapon = ['Small Weapons'],
            armor = ['No Armor'],
            magic_items = ['Any']
        )
    
    def lore(self) -> str:
        text = "A low-level Wizard is a fanatic when it comes to arcane knowledge. The road, discomfort, cold, dark dungeons, and even the tedious company of their adventuring party are all a small price to pay for access to knowledge, in a career where power is measured by what one knows. Beneath the glimmer of precious metals, you know there is ancestral knowledge to be acquired. Each desecrated ancient tomb hides long-lost secrets, and that is why you chose to adventure. In time, your knowledge will be converted into power, and this will make you feared. After all, it's natural to be afraid of what you don't understand, and that's when you will have enough knowledge to settle somewhere and spend your days studying all you have collected throughout your life."
        return text
    

    def arcane_spells(self) -> str:
        text = "A Mage is able to cast arcane spells daily. To memorize them, the Mage must study their spellbook, the grimoire, and decide which spells will be memorized for that day. [Grimoire, Initial Spells, New Spells, Upper Circles]"
        return text

    def read_magic(self) -> str:
        text = "Once per day per level, the Mage can decipher and read magical inscriptions anywhere, even if they do not understand the message they convey."
        return text

    def detect_magic(self) -> str:
        text = "Once per day per level, the Mage can sense the presence of magic in places, people, or objects within an area of up to 9 meters plus 3 meters per level, provided they are focused and actively searching for it."
        return text


    def __repr__(self) -> str:
        return f"Mage"
    