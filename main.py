import random
from time import sleep

from handy_functions import HandyFunctions as hf
from character import Character
from attribute_generator import AttributeGenerator
from races import dwarf, elf, halfling, human
from classes.mage import mage, illusionist, necromancer
from classes.thief import thief, bard, ranger
from classes.warrior import warrior, barbarian, paladin

print("- OldDragon -\n")
sleep(1)

# Character creation style
creation_styles = ['Classic', 'Adventure', 'Heroic']
style_chosen = ''
random_style = False

print(f"What 'Style' of character creation will be applied?")
for i, style in enumerate(creation_styles, 1): print(f"[{i}] {style}")
print("[4] Surprise me (random choice)")

while True:
    option = hf.input_int("Type the number of the chosen 'Style': ") - 1 # -1 for list indexes
    if option >= 0 and option <= len(creation_styles):
        if option == 3:
            option = random.choice(range(0, 3))
            random_style = True
        
        style_chosen = creation_styles[option]
        print(f"Style '{style_chosen}' chosen{' randomly.' if random_style == True else '.'}\n")
        sleep(1)
        break
    else:
        print(f"Invalid option. [Type: ", end='')
        for i in range(len(creation_styles) + 1):
            print(f'{i+1}, ' if i != (len(creation_styles)) else f'or {i+1}]', end='')
        print('\n')
        sleep(1)

character_1 = Character('Player')

print("-- Character Creation --\n")
sleep(1)

# Character - attributes
print("--- Character Attributes ---\n")
sleep(1)
ag = AttributeGenerator(character_1)
ag.generate_style(style_chosen)

# Character - race
print("\n--- Character Race ---\n")
sleep(1)
races = ['Dwarf', 'Elf', 'Halfling', 'Human']
race_chosen = None
random_race = False

print(f"What 'Race' do you want to play?")
for i, race in enumerate(races, 1): print(f"[{i}] {race}")


r = None
while True:
    option = hf.input_int("Type the number of the chosen 'Race': ") - 1 # -1 for list indexes
    if option >= 0 and option <= len(races): 
        race_chosen = races[option]
        print(f"Style '{race_chosen}' chosen.\n")
        if race_chosen == 'Dwarf':
            r = dwarf.Dwarf()
        elif race_chosen == 'Elf':
            r = elf.Elf()
        elif race_chosen == 'Halfling':
            r = halfling.Halfling()
        elif race_chosen == 'Human':
            r = human.Human()
        sleep(1)
        break
    else:
        print(f"Invalid option. [Type: ", end='')
        for i in range(len(races) + 1):
            print(f'{i+1}, ' if i != (len(races)) else f'or {i+1}]', end='')
        print('\n')
        sleep(1)
character_1.race = r


# Character - class
print("\n--- Character Class ---\n")
sleep(1)
classes = ['Mage', 'Thief', 'Warrior']
class_chosen = None
random_class = False

print(f"What 'Class' do you want to play?")
for i, classs in enumerate(classes, 1): print(f"[{i}] {classs}")

c = None
while True:
    option = hf.input_int("Type the number of the chosen 'Class': ") - 1 # -1 for list indexes
    if option >= 0 and option <= len(classes):      
        class_chosen = classes[option]
        print(f"Style '{class_chosen}' chosen.\n")
        if class_chosen == 'Mage':
            c = mage.Mage()
        elif class_chosen == 'Thief':
            c = thief.Thief()
        elif class_chosen == 'Warrior':
            c = warrior.Warrior()
        sleep(1)
        break
    else:
        print(f"Invalid option. [Type: ", end='')
        for i in range(len(classes) + 1):
            print(f'{i+1}, ' if i != (len(classes)) else f'or {i+1}]', end='')
        print('\n')
        sleep(1)
character_1.classs = c

# Character - subclass
print("\n--- Character Subclass ---\n")
sleep(1)
subclasses = []
if class_chosen == 'Mage':
    subclasses = ['Illusionist', 'Necromancer']
elif class_chosen == 'Thief':
    subclasses = ['Bard', 'Thieft']
elif class_chosen == 'Warrior':
    subclasses = ['Barbarian', 'Paladin']
subclass_chosen = None
random_subclasses = False

print(f"What 'Subclass' do you want to play?")
for i, subclass in enumerate(subclasses, 1): print(f"[{i}] {subclass}")
    

s = None
while True:
    option = hf.input_int("Type the number of the chosen 'Subclass': ") - 1 # -1 for list indexes
    if option >= 0 and option <= len(subclasses):      
        subclasses_chosen = subclasses[option]
        print(f"Style '{subclasses_chosen}' chosen.\n")
        if subclasses_chosen == 'Illusionist':
            s = illusionist.Illusionist()
        elif subclasses_chosen == 'Necromancer':
            s = necromancer.Necromancer()
        elif subclasses_chosen == 'Bard':
            s = bard.Bard()
        elif subclasses_chosen == 'Ranger':
            s = ranger.Ranger()
        elif subclasses_chosen == 'Paladin':
            s = paladin.Paladin()
        elif subclasses_chosen == 'Barbarian':
            s = barbarian.Barbarian()
        sleep(1)
        break
    else:
        print(f"Invalid option. [Type: ", end='')
        for i in range(len(classes) + 1):
            print(f'{i+1}, ' if i != (len(classes)) else f'or {i+1}]', end='')
        print('\n')
        sleep(1)
character_1.subclass = s

# Character - name
name = input("\nCharacter name: ")
character_1.name = name
print(f"Character '{character_1.name}' created.\n")

# Main menu
while True:
    sleep(1)
    print(f"-- Main Menu | {character_1.name} | {character_1.race} | {character_1.classs} | {character_1.subclass} --")
    print("[1] Change name")
    print("[2] Show attributes")
    print("[0] Exit")
    option = input()
    
    if option == '0':
        break
    elif option == '1':
        new_name = input("\nNew name: ")
        print(f"Name changed from '{character_1.name}' ", end='')
        character_1.name = new_name
        print(f"to '{character_1.name}'. \n")
    elif option == '2':
        character_1.show_attributes()
    else:
        break

print("\nThanks for playing OldDragon.")
sleep(1)
