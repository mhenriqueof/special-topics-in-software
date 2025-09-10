from time import sleep
from ...dice_roller import DiceRoller
from backend.handy_functions import HandyFunctions as hf

class AttributeGenerator():
    """Class for attribute generation styles."""
    def __init__(self):
        self.__dice = DiceRoller()
        self.__attributes = {
            "STR (Strength)": 0,
            "DEX (Dexterity)": 0,
            "CON (Constitution)": 0,
            "INT (Intelligence)": 0,
            "WIS (Wisdom)": 0,
            "CHA (Charisma)": 0
            }
        self.__attribute_names = [attribute for attribute in self.attributes]
        
    @property
    def dice(self) -> DiceRoller:
        return self.__dice
    @property
    def attributes(self) -> dict:
        return self.__attributes
    @property
    def attribute_names(self) -> list:
        return self.__attribute_names
            
    def attributes_distribution(self, dice_notation: str, choose: bool=False, drop_lowest: bool=False) -> dict:
        """Responsible for managing the distribution of the dice results to the attributes."""
        while True:
            for attribute in self.attributes:                
                # Roll dice and sum
                _ = input(f"Press [Enter] to roll the dice{f' for {attribute}.' if choose == False else '.'}")
                self.dice.roll(dice_notation)
                rolls = self.dice.rolls
                sum_rolls = sum(rolls)
                
                # Show rolls and sum
                self.dice.show_rolls()
                if drop_lowest == True:
                    self.dice.drop_lowest()
                    sum_rolls = sum(rolls)
                print(f"= {sum_rolls}")
                sleep(1)
                
                if choose:
                    self.__choose_attribute(sum_rolls)
                else:
                    self.attributes[attribute] = sum_rolls
                    
                hf.show_attributes(self.attributes)
            
            # Ask if they liked the distribution
            correct = bool(hf.input_int("Do you like the distribution? [0] No, I want to try again. | [1] Yes. "))
            if correct:
                return self.attributes
            else:
                print("Resetting attributes...")
                sleep(1)
                hf.reset_attributes(self.attributes)
                hf.show_attributes(self.attributes)

    def __choose_attribute(self, sum_rolls: int) -> None:
        """Ask which attribute to fill"""
        print(f"\nDistribute ({sum_rolls}) to:")
        for i, attribute in enumerate(self.attributes, start=1):
            print(f"[{i}] {self.attributes[attribute]} - {attribute}")
        while True:
            option = hf.input_int() - 1 # -1 for list indexes
            attribute_chosen = self.attribute_names[option]
            if self.attributes[attribute_chosen] == 0:
                self.attributes[attribute_chosen] = sum_rolls
                break
            else:
                print(f"Attribute '{attribute_chosen}' has already been chosen.")
                