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


# Weapons
rusty_sword = Weapon(
    'Rusty Sword', 'This sword looks like it has taken a lot of beating. Not the best but will do for now', 5, 7)

dagger = Weapon(
    'Dagger', 'The dagger that has been given to all beginner thieves. Beaten up after alot of use, Zidane still uses it.', 8, 5)

knife = Weapon(
    'Knife', 'This is a knife', 2,  4
)


# Armor

leather_shield = Armor(
    'Leather Shield', 'A regular leather shield', 5,  7
)

knight_shield = Armor(
    'Knight Shield', 'A shield from an Alexandria Knight', 5,  9
)

headband = Armor(
    'Ordinary Headband', 'A headband found in Alexandria', 2, 3
)

# Healing

loaf_of_bread = Health(
    'Loaf of Bread', 'Just some loaf of bread. Restores 5 health.', 1, 5
)

small_potion = Health(
    'Small Potion', 'A potion that restores 10 health.', 5, 10
)

medical_herb = Health(
    'Medical Herb', 'A medical herb found in the monastery. Heals for 20 health.', 3, 20
)

# MP

ether_stone = MP(
    'Ether Stone', 'A common stone found around the mage academy in Alexandria. Restores 5 MP', 2, 5
)

blue_potion = MP(
    'Blue Potion', 'A potion that is always recommended by high mages. Restores 10 MP', 5, 10
)

arcane_potion = MP(
    'Arcane Potion', 'A potion made by the High Black Mage himself. Very rare and expensive to purchase. Restores 20 MP', 10, 20
)
