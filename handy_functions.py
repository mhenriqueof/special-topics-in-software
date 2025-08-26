class HandyFunctions:
    """Class with methods for repetitive actions."""
    @staticmethod
    def input_int(string: str = '') -> int:
        while True:
            value = input(string)
            if value.isdigit():
                return int(value)
            else:
                print("Type a number.")
