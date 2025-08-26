from classes.warrior.warrior import Warrior

class Paladin(Warrior):
    def __init__(self):
        super().__init__()
        
    def paladins(self) -> str:
        text = "The Paladin is a chivalrous, wandering hero, fearless and of unquestionable character, who follows the path of truth and law, always willing to protect the weak and fight for the eradication of chaos."
        return text
    
    
    def disease_immunity(self) -> str:
        text = "Disease Immunity: The Paladin gains immunity to any type of disease, whether mundane or magical. Damage and other effects have no impact, as if they were never infected."
        return text

    def lay_on_hands(self) -> str:
        text = "Lay on Hands: The Paladin gains the ability to heal through the simple act of laying on hands, once per day."
        return text

    def aura_of_protection(self) -> str:
        text = "Aura of Protection: The Paladin gains the ability to create a permanent protective barrier around themselves, identical to the effect of the Protection from Alignment spell, which protects them against chaotic creatures."
        return text

    def holy_sword(self) -> str:
        text = "Holy Sword: When the Paladin defeats a powerful chaotic enemy, they acquire a magical sword which, once consecrated to their cause, becomes a Holy Sword imbued with zeal and powers against chaos."
        return text


    def __repr__(self) -> str:
        return f"Paladin"
    