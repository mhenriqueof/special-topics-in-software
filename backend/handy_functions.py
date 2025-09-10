class HandyFunctions:
    """Class with methods that are used in many files."""
    
    # General methods
    @staticmethod
    def input_int(string: str = '') -> int:
        while True:
            value = input(string)
            if value.isdigit():
                return int(value)
            else:
                print("Type a number.")

    # Character methods
    @staticmethod
    def show_attributes(attributes: dict) -> None:
        """Shows the character's attributes, their values and the modifier."""
        def attribute_modifier(value: int) -> str:
            """Returns a modifier value for the attributes."""
            if value >= 19: return '+4'
            elif value >= 17: return '+3'
            elif value >= 15: return '+2'
            elif value >= 13: return '+1'
            elif value >= 9: return ' 0'
            elif value >= 6: return '-1'
            elif value >= 4: return '-2'
            elif value >= 2: return '-3'
            return ' 0'
        print()
        print("-" * 25)
        for attribute, value in attributes.items():
            print(f"{value:>2} <> {attribute_modifier(value)} <> {attribute}")
        print("-" * 22)
        print()
    
    @staticmethod
    def reset_attributes(attributes: dict) -> None:
        """Changes all attributes values to 0."""
        for attribute in attributes:
            attributes[attribute] = 0
            