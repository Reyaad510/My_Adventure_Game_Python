from character import heroes
from character import boss
from character import normal_enemy
from room import room
import time
import os
import sys
import random


thief = heroes['thief']
guard = normal_enemy['normal_guard']


# Used to show letter by letter in terminal
# Comment out time.sleep for testing
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        # time.sleep(0.04)


def win():
    delay_print('\nYou won the battle!\n')


def lose():
    delay_print("You died. Game over!")


def attack(hero, enemy, done):
    os.system('cls')
    os.system('clear')
    delay_print(
        f'{hero.name} attacks the {enemy.name} for {hero.attack} damage!\n')
    enemy.health -= hero.attack

    if enemy.health <= 0:
        win()
        done = True
        opening()

    else:
        delay_print(
            f'\n{enemy.name} attack {hero.name} for {enemy.attack} damage\n')
        hero.health -= enemy.attack
    if hero.health <= 0:
        lose()
        done = True
    else:
        combat(hero, enemy)


def skills(hero, enemey):
    os.system('cls')
    os.system('clear')
    print('I use my skill')


def combat(hero, enemy):

    combat_done = False

    while not combat_done:
        delay_print(f'\n{hero.name} vs {enemy.name}\n')
        delay_print(
            f'Zidane HP: {hero.health}     Normal Guard: {enemy.health}')
        print("\n1. Attack")
        print("2. Skills")

        user_input = input("\nCommannd: ").strip().lower().split()

        if len(user_input) != 1:
            print('Press 1 or 2 to attack or us a skill!')
            continue

        if user_input[0] == '1':
            attack(hero, enemy, done=combat_done)

        elif user_input[0] == '2':
            skills(hero, enemy)


def opening():

    done = False

    while not done:
        delay_print(f'\nLocation: {thief.curRoom.name}\n')
        delay_print(f'\n{thief.curRoom.description}')

        user_input = input("\nCommannd: ").strip().lower().split()

        if len(user_input) != 1:
            print('I dont understand that. Type n,s,w, or e')
            continue

        if user_input[0] == 'quit' or user_input[0] == 'q':
            done = True

        elif user_input[0] in ["n", "north", "s", "south", "w", "west", "e", "east"]:
            thief.curRoom = thief.tryDirection(user_input[0], thief.curRoom)

        elif user_input[0] == 'fight':
            done = True
            os.system('cls')
            os.system('clear')
            combat(thief, guard)


def opening_dialogue():

    done = False

    while not done:
        delay_print(f'\nLocation: {thief.curRoom.name}\n')
        delay_print(f'\n{thief.curRoom.description}\n')

        delay_print(
            f'\nWedge: Crap! Crap! There is a guard right there! There is no way we can kidnap the princess!\n')
        delay_print(
            f'\nZanbar: WEDGE if you dont stop this at once i will take out my dagger and end you myself!\n')
        delay_print(
            f'\n{thief.name}: Haha! Wedge there is no need to worry. Think about it. There are 3 of us and only one guard So what does that mean for us?\n')
        delay_print(f'\nWedge: Oh god no! That means we are triple dead??\n')
        delay_print(
            f'\nZanbar: WEDGE you imbeccile. Taste the fury of my Dagger Of A Thousand Stabs!\n')
        delay_print(f'\n{thief.name}: No need for that Zanbar. Wedge will grow out of it i assure you. For now follow my lead and trust me when I say this mission will be a success! Lets go take out that guard!\n')

        done = True

        command = False

        while not command:

            user_input = input("\nCommannd: ").strip().lower().split()

            if len(user_input) != 1:
                print('Lets go north to fight those guards! Type n or north!')
                continue

            if user_input[0] == 'quit' or user_input[0] == 'q':
                command = True
            elif user_input[0] in ["n", "north"]:
                thief.curRoom = thief.tryDirection(
                    user_input[0], thief.curRoom)
                command = True
                os.system('cls')
                os.system('clear')
                opening()

            else:
                print('Lets go north to fight those guards! Type n or north!')


start = False

while not start:
    delay_print('\nWelcome you are playing as Zidane, part of a thieves guild. You are currently with two other members, Wedge and Zanbar, outside of the castle of Alexandria. You are on a dangerous mission...I wont spoil much more. Have fun! Press enter in the terminal to begin your adventure!')
    user_input = input("\nCommannd: ").strip().lower().split()

    if len(user_input):
        time.sleep(0.1)
        os.system('cls')
        os.system('clear')
        opening_dialogue()
        start = True

    else:
        time.sleep(0.1)
        os.system('cls')
        os.system('clear')
        opening_dialogue()
        start = True
