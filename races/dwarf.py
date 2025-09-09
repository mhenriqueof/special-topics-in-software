from races.race import Race, Alignment, Talent, Profile

class Dwarf(Race):
    def __init__(self):
        super().__init__(
            movement = 6,
            infravision = 18,
            alignment = Alignment.ORDER.value,
        )
    
    def talents(self) -> list[dict]:
        return [
            Talent.MINERS.value,
            Talent.STURDY.value,
            Talent.LARGE_WEAPONS.value,
            Talent.ENEMIES.value
        ]

    def profile(self) -> dict:
        return {
            Profile.LORE.value: "Honorable, perfectionist, and reserved, dwarves are known not only for their distinctive appearance but also for their deep connection to their history and traditions. Stocky and rugged, with unmistakably large beards, they live in mountain halls alongside their clans, mining, forging, honoring their ancestors, and celebrating with beer and strong spirits. Their underground halls are sacred, and their lives are disciplined and work-focused, punctuated by songs and frequent festivities. Guided by honor and gratitude toward those who built their proud heritage, dwarves place family, clan, and race above personal desires. They strive to prove themselves worthy of belonging to what they call the \"perfect people\". Master smiths, they can forge anything in metal to flawless quality, and they excel in engineering, construction, and heavy labor, though they have little affinity for arcane arts. Outside their lands, they remain proud defenders of their origins, often comparing the world around them to the superior craftsmanship of their own people.",
            
            Profile.PERS.value: "Pride, tradition, and obsession define dwarven character. They constantly remind others of their people's greatness, victories, and unmatched quality. Bound to the deeds of their ancestors, they see dwarven heroes as the ultimate standard to emulate. Tradition is not just custom but a way of life and a code of honor. Dwarves are obsessive in defending their ideals, their people, and the perfection of their craft-whether in battle, smithing, brewing, or composing songs mocking their enemies. For them, perfection borders on a spiritual pursuit.",
            
            Profile.ADVE.value: "For some dwarves, adventuring is more than a choice-it is a way to honor their traditions. Inspired by epic deeds of the past, they seek to prove their skill, resilience, and worthiness to bear their clan's name. Dwarven adventurers are driven by pride and the desire to leave behind feats that will inspire future generations."
        }
