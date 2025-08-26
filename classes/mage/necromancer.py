from classes.mage.mage import Mage

class Necromancer(Mage):  
    def __init__(self):
            super().__init__()
            
    def necromancers(self) -> str:
        text = "A Necromancer is a scholar of the dark facts surrounding life and death, studying the mystical energies that influence these concepts in both living and non-living beings. The knowledge of this most morbid of arcane arts is superstitiously seen as evil, even though the cycle of life is one of nature's most neutral forces. Living and dying are part of a Necromancer's studies, and this doesn't necessarily make them evil, but rather someone who seeks a precise understanding of these concepts. Although any Wizard can create necrotic effects, a Necromancer's study of death allows them to reach a level of perfection beyond what a common Wizard can achieve."
        return text
    

    def exclusive_spells(self) -> str:
        text = "The Necromancer writes Dark Touch and Terrorize in their grimoire, spells that are exclusive to Necromancers."
        return text
    
    def create_undead(self) -> str:
        text = "The Necromancer writes the spell Create Undead in their grimoire, a magic exclusive to Necromancers."
        return text

    def drain_life(self) -> str:
        text = "The Necromancer writes the spell Drain Life in their grimoire, a magic exclusive to Necromancers."
        return text

    def death_magic(self) -> str:
        text = "The Necromancer writes the spell Death Magic in their grimoire, a magic exclusive to Necromancers."
        return text


    def __repr__(self) -> str:
        return f"Necromancer"
    