from classes.mage.mage import Mage

class Illusionist(Mage):
    def __init__(self):
            super().__init__()
            
    def illusionists(self) -> str:
        text = "An Illusionist is a character linked to the art of illusions, which means they specialize in concealment, sleight of hand, and manipulating reality. They use mystical energy to create visual effects that are not real. Although any Wizard can create some illusory effects with their spells, an illusion created by an Illusionist has a superior finish compared to one created by a non-Illusionist Wizard."
        return text
    

    def exclusive_spells(self) -> str:
        text = "The Illusionist writes Illusion and Phantasmal Sound in their grimoire, spells that are exclusive to Illusionists."
        return text

    def improved_illusion(self) -> str:
        text = "The Illusionist writes this exclusive spell in their grimoire."
        return text

    def mirage(self) -> str:
        text = "The Illusionist writes this exclusive spell in their grimoire."
        return text

    def permanent_illusion(self) -> str:
        text = "The Illusionist writes this exclusive spell in their grimoire."
        return text


    def __repr__(self) -> str:
        return f"Illusionist"
    