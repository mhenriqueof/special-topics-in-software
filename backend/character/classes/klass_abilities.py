from enum import Enum

class Ability(Enum):
    ARCANE_SPELLS = {"Arcane Spells": "A Mage is able to cast arcane spells daily. To memorize them, the Mage must study their spellbook, the grimoire, and decide which spells will be memorized for that day. [Grimoire, Initial Spells, New Spells, Upper Circles]"}
    BLOCK = {"Block": "A Warrior may, after being hit by a physical attack and before the damage roll is made, choose to sacrifice their shield or a weapon they are wielding to absorb all the damage from that attack."}
    DETECT_MAGIC = {"Detect Magic": "Once per day per level, the Mage can sense the presence of magic in places, people, or objects within an area of up to 9 meters plus 3 meters per level, provided they are focused and actively searching for it."}
    EXTRA_ATTACK = {"Extra Attack": "At 6th level, a Warrior gains a second attack, either melee or ranged, using the same weapon with which they have mastery."}
    HEAR_NOISES = {"Hear Noises": "The Thief can detect sounds such as a conversation on the other side of a door or the approach of monsters. To do so, they must be in a quiet environment, such as a dungeon, and outside of combat."}
    READ_MAGIC = {"Read Magic": "Once per day per level, the Mage can decipher and read magical inscriptions anywhere, even if they do not understand the message they convey."}
    SNEAK_ATTACK = {"Sneak Attack": "When the Thief attacks after approaching the enemy stealthily, they can make a very easy attack, dealing double damage."}
    THIEF_TALENTS = {"Thief Talents": "Thieves possess certain abilities that represent their main fields of expertise. They start with 2 points in each of the five talents and receive 2 additional points to distribute as they wish."}
    WEAPON_MASTERY = {"Weapon Mastery": "The Warrior becomes a master with one weapon of their choice, gaining a +1 bonus to damage rolls made with that weapon."}
    