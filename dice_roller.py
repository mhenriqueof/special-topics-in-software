from random import randint

class DiceRoller(): 
    """Class responsible for rolling dice for the attributes generation."""
    def __init__(self):
        self.__rolls = []
        
    @property
    def rolls(self) -> list[int]:
        return self.__rolls
    @rolls.setter
    def rolls(self, rolls: list[int]) -> None:
        self.__rolls = rolls
    
    def roll(self, notation: str) -> None:
        """Returns a list with random values according to the dice notation."""
        split = notation.split('d')
        number_of_dice = int(split[0])
        faces_each_die = int(split[1])
        self.rolls = [randint(1, faces_each_die) for _ in range(number_of_dice)]
    
    def show_rolls(self) -> None:
        """Shows the rolled dice."""
        print("\nRolled dice: ", end='')
        for roll in self.rolls:
            print(f"[{roll}] ", end='')
