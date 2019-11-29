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


# Dining Hall


def c_east():
    clear()
    print_location(thief)
    delay_print("\nZidane, Wedge, and Zanbar sprint through the east door of the castle main floor and find themselves in a grand dining hall.\n")
    delay_print("\nAs they run in they hide on the sides of the wall and peek back where they came from and see three guards running down the stairs.\n")
    delay_print(
        "\nThat's when they saw a knight following them and he let out a loud yell...\n")
    delay_print(
        "\nKnight: WHAAAA?! What is the meaning of this?! You four tell me what happened here?? \n")
    delay_print("\nGuard 1: Steiner Sir, I believe that some sort of fight happened because one of our guards is laying on the floor and looks badly injured SIR!\n")
    delay_print("\nGuard 2: Uhh...uhh...what he said SIR!\n")
    delay_print("\nSteiner: Sigh...you guards are useless. This was not a case of a battle. It's blatantly obvious this guard fell asleep on duty. The Queen and Princess will hear about this at once.\n")
    delay_print("\nGuard 3: Sir Steiner...no offense but the guard has injuries that definitely came from someone attacking him SIR!\n")
    delay_print(
        "\n At that moment the guard that was defeated in battle murmured some words\n")
    delay_print(
        "\nDefeated Guard: ...Three of them fought me....thieves....protect...princess.\n")
    delay_print("\nThe defeated guard then proceeded to faint.\n")
    delay_print("\nGuard 1: See just like i said SIR!\n")
    delay_print("\nSteiner: I cannot believe this! I must protect Princess Garnet at once! The poor Princess is all alone upstairs in her room. I must go to her at once before any harm comes to her.\n")
    delay_print(
        "\nSteiner: You three check everywhere down here and see where the thieves might be!.\n")
    delay_print("\nGuard 1,2,3: YES SIR!\n")
    delay_print("\nSteiner then proceeded to run up the stairs to the princess. The three guards were standing in front of the staircase talking about how they should proceed.\n")

    delay_print('\nWe go back to Zidane and the gang in the Dining Hall.\n')
    delay_print('\nZidane: Okay, while they are talking how about we search this dining hall to see if there is anything of use to us? \n')

    done = False
    while not done:
        delay_print('\nIn rooms you now have gained the ability to "examine" if there are any items in the room that could be of use to you. Lets try it!\n')
        user_input = input("\n> ").strip().lower().split()
        if len(user_input) != 1:
            print('Type "examine" to use your ability!')
            continue
        if user_input[0] == 'quit' or user_input[0] == 'q':
            done = True
        elif user_input[0] == 'examine':
            delay_print(f'\nYou found a {thief.curRoom.item.name}\n')
            delay_print(f'\n{thief.curRoom.item.description}\n')
            delay_print(
                f'\n{thief.curRoom.item.name} has been added to your inventory!\n')
            thief.inventory.append(thief.curRoom.item)
            done = True

            checkInventory = False
            while not checkInventory:
                delay_print('\n Now that we have some items why dont we check out our inventory? Type "inventory" to see what we have. I believe we got an item from the guard earlier. Why not try equipping it?\n')
                user_input = input("\n> ").strip().lower().split()
                if len(user_input) != 1:
                    print('Type "inventory" to see and equip your gear!')
                    continue
                if user_input[0] == 'quit' or user_input[0] == 'q':
                    done = True
                elif user_input[0] == 'inventory':
                    thief.inven(thief)

# Armory


def c_west():
    clear()
    print_location(thief)
    print("\nZidane, Wedge, and Zanbar sprint through the west door of the castle main floor and find themselves in a room filled with a multitude of swords and armor out in the open for the taking.\n")
    delay_print("\nAs they run in they hide on the sides of the wall and peek back where they came from and see three guards running down the stairs.\n")
    delay_print(
        "\nThat's when they saw a knight following them and he let out a loud yell...\n")
    delay_print(
        "\nKnight: WHAAAA?! What is the meaning of this?! You four tell me what happened here?? \n")
    delay_print("\nGuard 1: Steiner Sir, I believe that some sort of fight happened because one of our guards is laying on the floor and looks badly injured SIR!\n")
    delay_print("\nGuard 2: Uhh...uhh...what he said SIR!\n")
    delay_print("\nSteiner: Sigh...you guards are useless. This was not a case of a battle. It's blatantly obvious this guard fell asleep on duty. The Queen and Princess will hear about this at once.\n")
    delay_print("\nGuard 3: Sir Steiner...no offense but the guard has injuries that definitely came from someone attacking him SIR!\n")
    delay_print(
        "\n At that moment the guard that was defeated in battle murmured some words\n")
    delay_print(
        "\nDefeated Guard: ...Three of them fought me....thieves....protect...princess.\n")
    delay_print("\nThe defeated guard then proceeded to faint.\n")
    delay_print("\nGuard 1: See just like i said SIR!\n")
    delay_print("\nSteiner: I cannot believe this! I must protect Princess Garnet at once! The poor Princess is all alone upstairs in her room. I must go to her at once before any harm comes to her.\n")
    delay_print(
        "\nSteiner: You three check everywhere down here and see where the thieves might be!.\n")
    delay_print("\nGuard 1,2,3: YES SIR!\n")
    delay_print("\nSteiner then proceeded to run up the stairs to the princess. The three guards were standing in front of the staircase talking about how they should proceed.\n")

    delay_print('\nWe go back to Zidane and the gang\n')
    delay_print(
        '\nZidane: Okay, while they are talking how about we search this Armory to see if there is anything of use to us? \n')

    done = False
    while not done:
        delay_print('\nIn rooms you now have gained the ability to "examine" if there are any items in the room that could be of use to you. Lets try it!\n')
        user_input = input("\n> ").strip().lower().split()
        if len(user_input) != 1:
            print('Type "examine" to use your ability!')
            continue
        if user_input[0] == 'quit' or user_input[0] == 'q':
            done = True
        elif user_input[0] == 'examine':
            delay_print(f'\nYou found a {thief.curRoom.item.name}\n')
            delay_print(f'\n{thief.curRoom.item.description}\n')
            delay_print(
                f'\n{thief.curRoom.item} has been added to your inventory!\n')
            thief.inventory.append(thief.curRoom.item)
            done = True

            checkInventory = False
            while not checkInventory:
                delay_print('\n Now that we have some armor why dont we check out our inventory? Type "inventory" to see what we have. I believe we got an item from the guard earlier too. Why not try equipping the sword and the armor?\n')
                user_input = input("\n> ").strip().lower().split()
                if len(user_input) != 1:
                    print('Type "inventory" to see and equip your gear!')
                    continue
                if user_input[0] == 'quit' or user_input[0] == 'q':
                    done = True
                elif user_input[0] == 'inventory':
                    thief.inven(thief)
