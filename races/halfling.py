from races.race import Race

class Halfling(Race):
    def __init__(self):
        super().__init__(
            movement = 6,
            infravision = 0,
            alignment = 'Neutral',
            skills = {
                "Stealthy": "Experts at hiding and going unnoticed, halflings can hide with a 1-2 chance on a 1d6 roll. If the halfling adopts the Thief class, they also gain a +1 bonus to their Stealth skill.",
                "Fearless": "Halflings are highly resistant to effects that affect their willpower, receiving a +1 bonus on any Wisdom Saving Throw.",
                "Good Aim": "Due to their racial tradition of throwing games, for halflings any ranged attack with a thrown weapon is considered an easy attack.",
                "Small": "Due to their short stature and agility, all attacks from large or larger creatures are considered difficult attacks to hit a halfling.",
                "Restrictions": "As they have no tradition in armor forging, halflings only use leather armor, unless it is specially crafted for them."
            }
        )

    def story(self) -> str:
        text = "Small, round, methodical, and brave, halflings are a peaceful, rural people living in green hills, farming and raising livestock in small, idyllic communities—often near human lands. They resemble miniature humans, with slightly pointed ears, large hairy feet, and cheerful, round faces with rosy cheeks. Their thick, curly hair and barefoot lifestyle are trademarks. Hardworking and disciplined, they complete their tasks with care so they can enjoy what they love most: leisure and comfort. Halflings delight in good food (preferably six meals a day), long-winded stories, and questionable jokes. They value peace, calm, and a life free from haste or worry. Yet, alongside their love of comfort, they are driven by curiosity—drawn to the unknown, eager to explore and investigate. Friendly, tolerant, and sociable, they are among the easiest companions to befriend."
        return text
    
    def personality(self) -> str:
        text = "Halflings live in a constant balance between comfort and curiosity. While they care about money, it is not for power but for the comfort and security it brings. A soft, cushioned chair for an afternoon nap is far more appealing than a jewel-encrusted throne. They have little interest in hoarding wealth or political ambition, preferring community, belonging, friendship, and the occasional journey into the unknown. Their desires are practical, grounded, and always seasoned with courage."
        return text
    
    def adventures(self) -> str:
        text = "Halflings need little reason to set out on adventures—curiosity and bravery are often enough. Their quests may be for excitement, to cure boredom, or simply to gather a good story to tell. Halfling literature is filled with tales of heroes and daring deeds, often exaggerated for effect. They venture forth to broaden their horizons, unafraid of the unknown, eager to learn, experience, and take part in the wider world."
        return text
    
    
    def __repr__(self) -> str:
        return f"Halfling"
    