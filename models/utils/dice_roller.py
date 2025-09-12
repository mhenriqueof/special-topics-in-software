from random import randint

class DiceRoller(): 
    """Class responsible for managing the dice of the game."""
    @staticmethod  
    def roll(notation: str) -> list[int]:
        """Returns a list with random values according to the dice notation."""
        split = notation.split('d')
        number_of_dice = int(split[0])
        faces_each_die = int(split[1])
        return [randint(1, faces_each_die) for _ in range(number_of_dice)]
        