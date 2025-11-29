class Hero:
    def __init__(self):
        self.name = None
        self.role = None
        self.weapon = None
        self.armor = None

    def __str__(self):
        return f"Herói [{self.name}] | Classe: {self.role} | Arma: {self.weapon} | Armadura: {self.armor}"


class HeroBuilder:
    def __init__(self):
        self.hero = Hero()

    def set_name(self, name: str):
        self.hero.name = name
        return self

    def set_role(self, role: str):
        self.hero.role = role
        return self

    def equip_weapon(self, weapon: str):
        self.hero.weapon = weapon
        return self

    def equip_armor(self, armor: str):
        self.hero.armor = armor
        return self

    def build(self) -> Hero:
        result = self.hero
        self.hero = Hero() 
        return result
