from random import randint

class DiceRoller():    
    """Class responsible for rolling dice for the attributes generation."""
    def _roll_dice(self, number_of_dice: int) -> list[int]:
        """Returns a list with random values from 1 to 6."""
        return [randint(1, 6) for _ in range(number_of_dice)]
    
    def _show_rolls(self, rolls: list) -> None:
        """Shows the rolled dice."""
        print("Rolled dice: ", end='')
        for roll in rolls:
            print(f"[{roll}] ", end='')
        
    def roll_3d6(self) -> int:
        """Rolls 3d6, shows each die and returns the sum of them."""
        rolls = self._roll_dice(3)
        self._show_rolls(rolls)  
        return sum(rolls)
    
    def roll_4d6_drop_lowest(self) -> int:
        """Rolls 4d6, shows each die and returns the sum of the 3 highest."""
        rolls = self._roll_dice(4)
        self._show_rolls(rolls)
        print(f"(One die [{min(rolls)}] will be discarded.)")
        rolls.remove(min(rolls))
        return sum(rolls)
    