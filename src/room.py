

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        output = f'{self.name}: {self.description}'
        return output


room = {
    'outside':  Room("Outside of Alexandria Castle",
                     "North are the doors to the Castle protected by a guard."),
    'castleDoors': Room("Caste Door", "At the castle door is one guard who is lazily standing there about to fall asleep...That is until he notices three figures moving towards him rapidly"),

    'cfloor1':    Room("Castle Main Floor", """Very vast and big area filled with a multitude of light flowing from lamps. """),

    'cfloor2': Room("Castle Second Floor", """Second floor bustling with multiple rooms. North is the throne room"""),

    'throneRoom':   Room("Queen Braham Throne Room", """Huge room where the throne chairs reside."""),

    'secretPassage': Room("Secret Passage", """A secret passage that connects the throneroom and the castle main floor."""),
}


room['outside'].north_to = room['castleDoors']
room['outside'].n_to = room['castleDoors']

room['cfloor1'].south_to = room['outside']
room['cfloor1'].s_to = room['outside']
room['cfloor1'].north_to = room['cfloor2']
room['cfloor1'].n_to = room['cfloor2']
room['cfloor1'].east_to = room['throneRoom']
room['cfloor1'].e_to = room['throneRoom']
room['cfloor2'].south_to = room['cfloor1']
room['cfloor2'].s_to = room['cfloor1']
room['throneRoom'].west_to = room['cfloor1']
room['throneRoom'].w_to = room['cfloor1']
room['throneRoom'].north_to = room['secretPassage']
room['throneRoom'].n_to = room['secretPassage']
room['secretPassage'].south_to = room['throneRoom']
room['secretPassage'].s_to = room['throneRoom']
