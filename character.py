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
        self.__race = None
        self.__classs = None # "classs" to avoid class of Python
        self.__subclasss = None
        
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
        
    # __race
    @property
    def race(self):
        return self.__race
    @race.setter
    def race(self, race) -> None:
        self.__race = race
        
    # __classs
    @property
    def classs(self):
        return self.__classs
    @classs.setter
    def classs(self, classs) -> None:
        self.__classs = classs

    # __subclasss
    @property
    def subclass(self):
        return self.__subclass
    @subclass.setter
    def subclass(self, classs) -> None:
        self.__subclass = classs
    
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
        """Changes all attributes values to 0"""
        for attribute in self.attributes:
            self.attributes[attribute] = 0

    # Magic methods
    def __str__(self) -> str: # "Readable" representation
        return f"- {self.name} -\nStats: {self.attributes}"
    
    def __repr__(self) -> str: # "Debug" representation
        return f"Character(name='{self.name}', stats={self.attributes})"
    