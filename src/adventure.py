from character import heroes
from character import boss
from character import normal_enemy
from room import room


thief = heroes['thief']

done = False

while not done:
    print(f'\n{thief.curRoom.name}\n')
    print(f'{thief.curRoom.description}')

    user_input = input("\nCommannd: ").strip().lower().split()

    if len(user_input) != 1:
        print('I dont understand that. Type n,s,w, or e')
        continue

    if user_input[0] == 'quit' or user_input[0] == 'q':
        done = True

    elif user_input[0] in ["n", "north", "s", "south", "w", "west", "e", "east"]:
        thief.curRoom = thief.tryDirection(user_input[0], thief.curRoom)
