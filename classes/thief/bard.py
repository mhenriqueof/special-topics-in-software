from classes.thief.thief import Thief

class Bard(Thief):
    def __init__(self):
        super().__init__()
        self.weapon = ['Medium Weapons', 'Small Weapons']
        self.armor = ['Only Light Armor']
        self.magic_items = ['Only Protection Scroll']
    
    def bards(self) -> str:
        text = "A Bard is a character tied to the arts and performance. They are travelers, reporters of daily life, and spreaders of epic deeds. They roam the roads singing, acting, and inspiring emotions in their audience. They are always seeking out opportunities to be close to the action, using their personal magnetism and cunning as their tools for survival."
        return text
    
    
    def sneak_attack(self) -> str:
        text = ""
        return text

    def influence(self) -> str:
        text = "Through music, speeches, and heroic ballads, the Bard can affect the reactions of monsters or the Game Master's characters with a 1-2 in 1d6 chance."
        return text
    
    def inspire(self) -> str:
        text = "If the Bard is able to spend at least one round performing, and continues to maintain the performance, their allies become more confident in their success."
        return text

    def fascinate(self) -> str:
        text = "Through music, speeches, and heroic ballads, the Bard can captivate a non-hostile audience of monsters or the Game Master's characters with up to 2 Hit Dice for every 3 Bard levels, provided they understand the language used by the Bard, keeping them engaged and focused on the performance."
        return text

    def use_scrolls(self) -> str:
        text = "The Bard gains the ability to use scrolls as if they were a Mage with half their current levels."
        return text


    def __repr__(self) -> str:
        return f"Bard"
    