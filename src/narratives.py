from character import heroes
import os
import sys
import time


thief = heroes['thief']


def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        # time.sleep(0.04)
        # time.sleep(0.01)


def delay_print_fast(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        # time.sleep(0.02)
        # time.sleep(0.01)

# Clearing the user terminal


def clear():
    os.system('cls')
    os.system('clear')

# Prints the player location and description of room


def print_location(hero):
    print('\n' + ('#' * (4 + len(hero.curRoom.name))))
    print('# ' + hero.curRoom.name.upper() + ' #')
    print(('#' * (4 + len(hero.curRoom.name)) + '\n'))


def hide():
    clear()
    print(" I am indeed hiding")
    input("\n> ").strip().lower().split()


def c_east():
    clear()
    print_location(thief)
    delay_print("\nZidane, Wedge, and Zanbar sprint through the east door of the castle main floor and find themselves in a grand dining hall.\n")
    delay_print("\nAs they run in they hide on the sides of the wall and peek back where they came from and see 4 guards running down the stairs.\n")
    delay_print(
        "\nThat's when they saw a knight following them and he let out a loud yell...\n")
    delay_print(
        "\nKnight: WHAAAA?! What is the meaning of this?! You four tell me what happened here?? \n")
    delay_print("\nGuard 1: Umm...Stenier Sir, we all literally just came down the same exact time as you did so how are we supposed to know?\n")
    delay_print("\nGuard 2: Steiner Sir, I believe that some sort of fight happened because one of our guards is laying on the floor and looks badly injured SIR!\n")
    delay_print("\nSteiner: No no no! I was behind you because it is my duty to protect Princess Garnet at all cost. Her life is all that matters to me.\n")
    delay_print('\nWant to grab this loaf of bread?\n')

    done = False
    while not done:
        delay_print('\nWant to grab this loaf of bread?\n')
        user_input = input("\n> ").strip().lower().split()
        if len(user_input) != 1:
            print('Type something!')
            continue
        if user_input[0] == 'quit' or user_input[0] == 'q':
            done = True
        elif user_input[0] == 'yes':
            thief.inventory.append(thief.curRoom.item)
            print(thief.inventory)
        elif user_input[0] == 'inventory':
            thief.inven(thief)


def c_west():
    clear()
    print_location(thief)
    print("\nZidane, Wedge, and Zanbar sprint through the west door of the castle main floor and find themselves in a room filled with a multitude of swords and armor out in the open for the taking.\n")
    delay_print("\nAs they run in they hide on the sides of the wall and peek back where they came from and see 4 guards running down the stairs.\n")
    delay_print(
        "\nThat's when they saw a knight following them and he let out a loud yell...\n")
    input("\n> ").strip().lower().split()
