class Character:
    """Represents a character with their name and attributes."""
    def __init__(self, name: str):
        self.__name: str = name
        self.__attributes = {
            "STR (Strength)": 0,
            "DEX (Dexterity)": 0,
            "CON (Constitution)": 0,
            "INT (Intelligence)": 0,
            "WIS (Wisdom)": 0,
            "CHA (Charisma)": 0
            }
        
    # __name
    @property
    def name(self) -> str:
        return self.__name
    @name.setter
    def name(self, name: str) -> None:
        self.__name = name
        
    # __attributes
    @property
    def attributes(self) -> dict[str, int]:
        return self.__attributes
    @attributes.setter
    def attributes(self, attributes: dict[str, int]) -> None:
        self.__attributes = attributes
    
    # General methods
    def show_attributes(self) -> None:
        """Shows the character's attributes and their values."""
        print()
        print("-" * 25)
        for attribute, value in self.attributes.items():
            print(f"{value:>2} <> {attribute}")
        print("-" * 22)
        print()
    
    def reset_attributes(self) -> None:
        for attribute in self.attributes:
            self.attributes[attribute] = 0

    # Magic methods
    def __str__(self) -> str: # "Readable" representation
        return f"- {self.name} -\nStats: {self.attributes}"
    
    def __repr__(self) -> str: # "Debug" representation
        return f"Character(name='{self.name}', stats={self.attributes})"
    