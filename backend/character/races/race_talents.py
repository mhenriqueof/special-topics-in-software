from enum import Enum

class Talent(Enum):
    ADAPTABILITY = {"Adaptability": "Humans are highly adaptable and diverse, allowing them to choose where to allocate a bonus to their Saving Throws. Humans receive a +1 bonus to a single Saving Throw of their choice."}
    FEARLESS = {"Fearless": "Halflings are highly resistant to effects that affect their willpower, receiving a +1 bonus on any Wisdom Saving Throw."}
    GOOD_AIM = {"Good Aim": "Due to their racial tradition of throwing games, for halflings any ranged attack with a thrown weapon is considered an easy attack."}
    GRACEFUL = {"Graceful": "Elves control their movements in the space around their bodies with precision, receiving a +1 bonus on any Dexterity Saving Throw."}
    IMMUNITIES = {"Immunities": "Elves are immune to effects or spells involving sleep and also to paralysis caused by a Ghoul."}
    LEARNING = {"Learning": "Humans learn everything they set out to do much faster than other races. A human receives a 10% bonus on all experience (XP) gained."}
    NATURAL_PERCEPTION = {"Natural Perception": "The way elven houses are built, respecting the natural form of trees and shelters, grants elves a special perception regarding unconventional and even secret doors and passages."}
    RACIAL_WEAPON = {"Racial Weapon": "Elves are familiar with archery, which they consider a martial art, receiving a +1 bonus to damage dealt with ranged attacks using bows."}
    RESTRICTIONS = {"Restrictions": "As they have no tradition in armor forging, halflings only use leather armor, unless it is specially crafted for them."}
    SMALL = {"Small": "Due to their short stature and agility, all attacks from large or larger creatures are considered difficult attacks to hit a halfling."}
    STEALTHY = {"Stealthy": "Experts at hiding and going unnoticed, halflings can hide with a 1-2 chance on a 1d6 roll. If the halfling adopts the Thief class, they also gain a +1 bonus to their Stealth skill."}
    