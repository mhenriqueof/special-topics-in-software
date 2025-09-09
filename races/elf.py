from races.race import Race, Alignment, Talent, Profile

class Elf(Race):
    def __init__(self):
        super().__init__(
            movement = 9,
            infravision = 18,
            alignment = Alignment.NEUTRAL.value
        )
        
    def talents(self) -> list[dict]:
        return [
            Talent.NATURAL_PERCEPTION.value,
            Talent.GRACEFUL.value,
            Talent.RACIAL_WEAPON.value,
            Talent.IMMUNITIES.value
        ]
        
    def profile(self) -> dict:
        return {
            Profile.LORE.value: "Elves are among the longest-lived races in fantasy worlds, often reaching a thousand years of age. Their unique relationship with time shapes their personality, values, and how other races perceive them. Physically, they are slender, slightly shorter than humans, with long, well-kept hair in many colors, almond-shaped eyes, and their most distinctive feature-long, pointed ears. They devote their lives to what they value most, such as dance, music, swordplay, archery, and arcane magic. To outsiders, they may seem distant, cold, or even arrogant, especially when away from their homelands. However, once an elf forms a friendship, it is deep and enduring, often lasting beyond the lifetimes of many other beings.",
            
            Profile.PERS.value: "Elves value quality over quantity, preferring to spend years perfecting a single masterpiece rather than producing many average works. They appreciate well-crafted, lasting things, reflecting their own longevity. Their perception of time makes them patient, meticulous, and focused on perfection. This mindset influences all aspects of their culture and personal behavior.",
            
            Profile.ADVE.value: "Though rarer than human adventurers, elves are driven by curiosity, the desire to travel, self-improvement, and the wish to prove themselves. Their long lives give them the freedom to explore and witness the world's changes firsthand. They are observant travelers, seeking to understand the world and refine their skills while leaving their mark on history."
        }
