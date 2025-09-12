from .race import Race, Alignment, Profile

class Human(Race):
    def __init__(self):
        super().__init__(
            movement = 9, 
            infravision = 0, 
            alignment = Alignment.ANY.value
        )
        
    @property
    def profile(self) -> dict:
        return {
            Profile.LORE.value: "Humans are culturally diverse and present in every corner of the world, thriving in all climates and adapting quickly to any environment. They display a wide range of physical traits and, despite their short lifespan and lack of innate magical abilities, excel through organization, expansion, and adaptability. In the time it takes an elf to reach adolescence, a human empire can rise, flourish, and vanish. Their true strength lies not in individual power, but in their ability to adapt, assimilate, and occupy new territories.",
            Profile.PERS.value: "Humans are versatile and unpredictable, embracing all philosophies and ways of life. They learn and innovate rapidly, often mastering new techniques within a single generation. When they expand, they establish dominance and permanence rather than retreat. They value productivity and quantity, and are generally accepting of other races, integrating them into their societies as long as they do not hinder human growth and survival.", 
            Profile.ADVE.value: "Human adventurers embody adaptability, imagination, determination, and ambition. They set out for survival, wealth, glory, or fame, driven by a desire to leave a legacy. Their ambition pushes them into dangerous places, seeking to make their names legendary and leave a lasting mark on the world."          
        }
        
    @property
    def talents(self) -> dict:
        return {
            "Learning": "Humans learn everything they set out to do much faster than other races. A human receives a 10% bonus on all experience (XP) gained.",
            "Adaptability": "Humans are highly adaptable and diverse, allowing them to choose where to allocate a bonus to their Saving Throws. Humans receive a +1 bonus to a single Saving Throw of their choice."
        }
