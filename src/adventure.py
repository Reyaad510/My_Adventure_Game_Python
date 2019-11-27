import item
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
steiner = heroes['knight']


# Used to show letter by letter in terminal
# Comment out time.sleep for testing
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        # time.sleep(0.04)
        # time.sleep(0.01)

# Clearing the user terminal


def clear():
    os.system('cls')
    os.system('clear')

# Prints the player location and description of room


def print_location(thief):
    print('\n' + ('#' * (4 + len(thief.curRoom.name))))
    print('# ' + thief.curRoom.name.upper() + ' #')
    print(('#' * (4 + len(thief.curRoom.name)) + '\n'))
    delay_print('\n -- ' + thief.curRoom.description + ' --\n')

# This decorates the 'vs' with '=' when you get into a fight


def combat_vs(hero, enemy):
    print(('=' * (4 + len(hero.name) + len(enemy.name))))
    print(f'{hero.name} vs {enemy.name}')
    print(('=' * (4 + len(hero.name) + len(enemy.name))))

# win screen


def win(hero, enemy):
    delay_print(f'\n{hero.name} won the battle against {enemy.name}!\n')
    delay_print(f'{hero.name} got {enemy.gold} gold!')
    if hasattr(enemy, 'items'):
        for x in enemy.items:
            delay_print(f'\n{hero.name} obtained a {x.name}')
        hero.gold += enemy.gold
        hero.inventory.extend(enemy.items)
    input("\n> ").strip().lower().split()

# lose screen


def lose():
    delay_print("You died. Game over!")
    input("\n> ").strip().lower().split()
    sys.exit()

# If user chooses to attack


def attack(hero, enemy):
    clear()
    h_attack = round(
        (hero.attack * (random.randint(100, 125)/100)) - enemy.defense)
    delay_print(
        f'{hero.name} attacks the {enemy.name} for {h_attack} damage!\n')
    enemy.health -= h_attack

    if enemy.health <= 0:
        win(hero, enemy)
        # Using if statements to say where to go next since won't have random battles
        if hero.curRoom == room['castleDoors']:
            after_first_guard()

    else:
        e_attack = round(
            (enemy.attack * (random.randint(100, 125)/100)) - hero.defense)
        delay_print(
            f'\n{enemy.name} attack {hero.name} for {e_attack} damage\n')
        hero.health -= e_attack
    if hero.health <= 0:
        lose()
    else:
        combat(hero, enemy)

# If user chooses to use a skill


def skills(hero, enemy):

    skill_done = False

    while not skill_done:
        delay_print('\nChoose a Skill: \n')
        for i, skill in enumerate(d for d in hero.skills):
            print(f'{i+1}.', skill['name'], '-', skill['mp_cost'], 'MP')
        delay_print(f'9. Back')

        user_input = input("\n> ").strip().lower().split()

        if len(user_input) != 1:
            print('\nPress a number to use a skill!')
            continue

        # Whatever number user presses will dynamically find the description for that move
        if user_input[0] in ['1', '2']:
            clear()
            if hero.skills[int(user_input[0]) - 1]['mp_cost'] <= hero.mp:
                delay_print(hero.skills[int(user_input[0]) - 1]['description'])
                print('\n')

                skill_damage = round((hero.attack * (random.randint(hero.skills[int(
                    user_input[0]) - 1]['dmg'][0], hero.skills[int(user_input[0]) - 1]['dmg'][1])/100)) - enemy.defense)

                delay_print(
                    f'{hero.name} did {skill_damage} damage to {enemy.name}!\n')

                print('\n')
                enemy.health -= skill_damage
                hero.mp -= hero.skills[int(user_input[0]) - 1]['mp_cost']
            else:
                delay_print(
                    'You dont have enough mp to use that skill!' + '\n')
                continue
        elif user_input[0] in ['back', 'b', '9']:
            clear()
            combat(hero, enemy)
        else:
            delay_print('Choose a number or type b, back, or 9 to go back!')
            continue

        # won battle
        if enemy.health <= 0:
            win(hero, enemy)
            skill_done = True
            # Using if statements to say where to go next since won't have random battles
            if hero.curRoom == room['castleDoors']:
                after_first_guard()

        else:
            e_attack = round(
                (enemy.attack * (random.randint(100, 125)/100)) - hero.defense)
        delay_print(
            f'\n{enemy.name} attack {hero.name} for {e_attack} damage\n')
        hero.health -= e_attack

        if hero.health <= 0:
            lose()
        else:
            combat(hero, enemy)


# Fuction that loops during combat


def combat(hero, enemy):

    combat_done = False

    while not combat_done:
        combat_vs(hero, enemy)
        delay_print(
            f'{hero.name} HP: {hero.health}     {enemy.name} HP: {enemy.health}\n')
        delay_print(
            f'{hero.name} MP: {hero.mp}      {enemy.name} MP: {enemy.mp}\n')
        print("\n1. Attack")
        print("2. Skills")
        print("3. Items")

        user_input = input("\n> ").strip().lower().split()

        if len(user_input) != 1:
            print('Enter 1, 2, or 3!')
            continue

        if user_input[0] == '1':
            attack(hero, enemy)

        elif user_input[0] == '2':
            combat_done = True
            skills(hero, enemy)

        elif user_input[0] == '3':
            hero.use_item(hero)


def after_first_guard():
    clear()
    done = False
    while not done:
        print('What the beep just happened to me?!?')
        user_input = input("\n> ").strip().lower().split()
        if len(user_input) != 1:
            print('type one word gosh darnit!')
            # done = True
            # combat(thief, steiner)
        elif user_input[0] == 'inven':
            # done = True
            clear()
            thief.inven(thief)


def opening():
    clear()
    done = False

    print_location(thief)
    while not done:

        user_input = input("\n> ").strip().lower().split()

        if len(user_input) != 1:
            print('I dont understand that. Type n,s,w, or e')
            continue

        if user_input[0] == 'quit' or user_input[0] == 'q':
            done = True

        elif user_input[0] in ["n", "north", "s", "south", "w", "west", "e", "east"]:
            thief.curRoom = thief.tryDirection(user_input[0], thief.curRoom)

        elif user_input[0] == 'fight':
            done = True
            clear()
            combat(thief, guard)

# Dialogue that occurs when starting the game


def opening_dialogue():
    clear()
    done = False

    while not done:
        print_location(thief)
        delay_print(
            f'\nWedge: Crap! Crap! There is a guard right there blocking the entrance! There is no way we can kidnap the princess!\n')
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

        user_input = input("\n> ").strip().lower().split()

        if len(user_input) != 1:
            print('Lets go north to fight those guards! Type n or north!')
            continue

        if user_input[0] == 'quit' or user_input[0] == 'q':
            command = True
        elif user_input[0] in ["n", "north"]:
            thief.curRoom = thief.tryDirection(
                user_input[0], thief.curRoom)
            command = True
            clear()
            opening()

        else:
            print('Lets go north to fight those guards! Type n or north!')


# Intro of game
start = False
while not start:
    delay_print('\nWelcome you are playing as Zidane, part of a thieves guild. You are currently with two other members, Wedge and Zanbar, outside of the castle of Alexandria. You are on a dangerous mission to kidnap the princess of Alexandria, Garnet. Have fun! Press enter in the terminal to begin your adventure!')
    user_input = input("\n> ").strip().lower().split()
    # start = True
    opening_dialogue()
