from time import sleep
from character import Character
from dice_roller import DiceRoller
from handy_functions import HandyFunctions as hf

class AttributeGenerator():
    """Class for attribute generation styles."""
    def __init__(self, character: Character):
        self.character = character
        self.__dice = DiceRoller()
        
    @property
    def dice(self) -> DiceRoller:
        return self.__dice

    def generate_style(self, style: str) -> None:
        if style == 'Classic':
            self.__attributes_distribution('3d6')
        elif style == 'Adventure':
            self.__attributes_distribution('3d6', choose=True)
        elif style == 'Heroic':
            self.__attributes_distribution('4d6', choose=True, drop_lowest=True)
            
    def __attributes_distribution(self, dice_notation: str, choose: bool = False, drop_lowest: bool=False) -> None:
        """Responsible for managing the distribution of the dice results to the attributes chosen by the player."""
        while True:
            attribute_names = [attribute for attribute in self.character.attributes]
            for attribute in self.character.attributes:                
                # Roll dice
                _ = input(f"Press [Enter] to roll the dice{f' for {attribute}.' if choose == False else '.'}")
                self.dice.roll(dice_notation)
                rolls = self.dice.rolls
                sum_rolls = sum(rolls)
                
                # Show rolls and sum
                self.dice.show_rolls()
                if drop_lowest == True:
                    self.__drop_lowest(rolls)
                    sum_rolls = sum(rolls)
                print(f"= {sum_rolls}")
                sleep(1)
                
                if choose:
                    # Ask which attribute to fill
                    print(f"\nDistribute ({sum_rolls}) to:")
                    for i, attribute in enumerate(self.character.attributes, start=1):
                        print(f"[{i}] {self.character.attributes[attribute]} - {attribute}")
                    while True:
                        option = hf.input_int() - 1 # -1 for list indexes
                        attribute_chosen = attribute_names[option]
                        if self.character.attributes[attribute_chosen] == 0:
                            self.character.attributes[attribute_chosen] = sum_rolls
                            break
                        else:
                            print(f"Attribute '{attribute_chosen}' has already been chosen.")
                else:
                    self.character.attributes[attribute] = sum_rolls
                self.character.show_attributes()
            
            # Ask if they liked the distribution
            correct = bool(hf.input_int("Do you like the distribution? [0] No, I want to try again. | [1] Yes. "))
            if correct:
                break
            else:
                print("Resetting attributes...")
                sleep(1)
                self.character.reset_attributes()
                self.character.show_attributes()

    def __drop_lowest(self, rolls: list[int]) -> None:
        """Remove a lowest value in the list."""
        lowest = min(rolls)
        print(f"(One die [{lowest}] will be discarded) ", end='')
        rolls.remove(lowest)
