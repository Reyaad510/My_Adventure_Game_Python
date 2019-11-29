from item import loaf_of_bread


class Room:
    def __init__(self, name, description, item):
        self.name = name
        self.description = description
        self.item = item

    def __str__(self):
        output = f'{self.name}: {self.description}'
        return output


room = {
    'outside':  Room("Outside of Alexandria Castle",
                     "North are the doors to the Alexandrian Castle protected by a single guard.", loaf_of_bread),

    'castleDoors': Room("Castle Door", "At the castle door is one guard who is lazily standing there about to fall asleep...That is until he notices three figures moving towards him rapidly", loaf_of_bread),

    'cfloor1':    Room("Castle Main Floor", "Very vast and big area filled with a multitude of light flowing from lamps.", loaf_of_bread),

    'cfloor1e':    Room("Castle Dining Hall", "Dining Hall.", loaf_of_bread),

    'cfloor1w':    Room("Castle Armory", "Armory", loaf_of_bread),

    'cfloor2': Room("Castle Second Floor", "Second floor bustling with multiple rooms. North is the throne room", loaf_of_bread),

    #     'throneRoom':   Room("Queen Braham Throne Room", "Huge room where the throne chairs reside.", loaf_of_bread),

    #     'secretPassage': Room("Secret Passage", """A secret passage that connects the throneroom and the castle main floor."""),
}


room['outside'].north_to = room['castleDoors']
room['outside'].n_to = room['castleDoors']
room['castleDoors'].n_to = room['cfloor1']
room['castleDoors'].north_to = room['cfloor1']
room['cfloor1'].e_to = room['cfloor1e']
room['cfloor1'].east_to = room['cfloor1e']
room['cfloor1'].w_to = room['cfloor1w']
room['cfloor1'].west_to = room['cfloor1w']
