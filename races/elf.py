from races.race import Race

class Elf(Race):
    def __init__(self):
        super().__init__(
            movement = 9,
            infravision = 18,
            alignment = 'Neutral',
            skills = {
                "Natural Perception": "The way elven houses are built, respecting the natural form of trees and shelters, grants elves a special perception regarding unconventional and even secret doors and passages.",
                "Graceful": "Elves control their movements in the space around their bodies with precision, receiving a +1 bonus on any Dexterity Saving Throw.",
                "Racial Training": "Elves are familiar with archery, which they consider a martial art, receiving a +1 bonus to damage dealt with ranged attacks using bows.",
                "Immunities": "Elves are immune to effects or spells involving sleep and also to paralysis caused by a Ghoul."
            }
        )
        
    def story(self) -> str:
        text = "Elves are among the longest-lived races in fantasy worlds, often reaching a thousand years of age. Their unique relationship with time shapes their personality, values, and how other races perceive them. Physically, they are slender, slightly shorter than humans, with long, well-kept hair in many colors, almond-shaped eyes, and their most distinctive feature—long, pointed ears. They devote their lives to what they value most, such as dance, music, swordplay, archery, and arcane magic. To outsiders, they may seem distant, cold, or even arrogant, especially when away from their homelands. However, once an elf forms a friendship, it is deep and enduring, often lasting beyond the lifetimes of many other beings."
        return text
    
    def personality(self) -> str:
        text = "Elves value quality over quantity, preferring to spend years perfecting a single masterpiece rather than producing many average works. They appreciate well-crafted, lasting things, reflecting their own longevity. Their perception of time makes them patient, meticulous, and focused on perfection. This mindset influences all aspects of their culture and personal behavior."
        return text
    
    def adventures(self) -> str:
        text = "Though rarer than human adventurers, elves are driven by curiosity, the desire to travel, self-improvement, and the wish to prove themselves. Their long lives give them the freedom to explore and witness the world's changes firsthand. They are observant travelers, seeking to understand the world and refine their skills while leaving their mark on history."
        return text
    
    
    def __repr__(self) -> str:
        return f"Elf"
    