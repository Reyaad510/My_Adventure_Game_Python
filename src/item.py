class Item:
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return f'{self.name}:{self.description}, {self.value}'


class Weapon(Item):
    def __init__(self, name, description, value, attack):
        super().__init__(name, description, value)
        self.attack = attack


class Armor(Item):
    def __init__(self, name, description, value, defense):
        super().__init__(name, description, value)
        self.defense = defense


class Health(Item):
    def __init__(self, name, description, value, health):
        super().__init__(name, description, value)
        self.health = health


class MP(Item):
    def __init__(self, name, description, value, mp):
        super().__init__(name, description, value)
        self.mp = mp


rusty_sword = Weapon(
    'Rusty Sword', 'This sword looks like it has taken a lot of beating. Not the best but will do for now', 5, 7)

dagger = Weapon(
    'Dagger', 'The dagger that has been given to all beginner thieves. Beaten up after alot of use, Zidane still uses it.', 8, 5)

knife = Weapon(
    'Knife', 'This is a knife', 2, 4
)
