class Character:
    """Represents a character with their name and attributes."""
    def __init__(self, name: str, attributes: dict[str, int]):
        self._name: str = name
        self._attributes: dict[str, int] = attributes
        
    # _name
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, name: str) -> None:
        self._name = name
        
    # _attributes
    @property
    def attributes(self) -> dict[str, int]:
        return self._attributes
    
    @attributes.setter
    def attributes(self, attributes: dict[str, int]) -> None:
        self._attributes = attributes
    
    # General methods
    def show_attributes(self) -> None:
        """Shows the character's attributes and their values."""
        print(f"{self.name} <> Attributes")
        for attribute, value in self.attributes.items():
            print(f"{value:>2} - {attribute}")

    # Magic methods
    def __str__(self) -> str: # "Readable" representation
        return f"- {self.name} -\nStats: {self.attributes}"
    
    def __repr__(self) -> str: # "Debug" representation
        return f"Character(name='{self.name}', stats={self.attributes})"
    