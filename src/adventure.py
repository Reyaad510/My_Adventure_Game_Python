import item
import narratives
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
        time.sleep(0.04)
        # time.sleep(0.01)


def delay_print_fast(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.02)
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


def print_location_description(hero):
    delay_print('\n -- ' + hero.curRoom.description + ' --\n')

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
    count = 0
    clear()
    h_attack = round(
        (hero.attack * (random.randint(100, 125)/100)) - enemy.defense)
    delay_print_fast(
        f'{hero.name} attacked the {enemy.name} for {h_attack} damage!\n')
    enemy.health -= h_attack
    count += 1
    hero.ultimate_counter(hero, count)
    count = 0
    if enemy.health <= 0:
        win(hero, enemy)
        # Using if statements to say where to go next since won't have random battles
        if hero.curRoom == room['castleDoors']:
            after_first_guard(hero)

    else:
        e_attack = round(
            (enemy.attack * (random.randint(100, 125)/100)) - hero.defense)
        delay_print_fast(
            f'\n{enemy.name} attacked {hero.name} for {e_attack} damage\n')
        hero.health -= e_attack
        count += 1
        hero.ultimate_counter(hero, count)
    if hero.health <= 0:
        lose()
    else:
        combat(hero, enemy)

# If user chooses to use a skill


def skills(hero, enemy):
    count = 0
    skill_done = False
    clear()

    while not skill_done:
        delay_print_fast('\nChoose a Skill: \n')
        for i, skill in enumerate(d for d in hero.skills):
            print(f'{i+1}.', skill['name'], '-', skill['mp_cost'], 'MP')
        delay_print_fast(f'\nb. back')

        user_input = input("\n> ").strip().lower().split()

        if len(user_input) != 1:
            print('\nPress a number to use a skill!')
            continue

        # Whatever number user presses will dynamically find the description for that move
        if user_input[0] in ['1', '2']:
            clear()
            if hero.skills[int(user_input[0]) - 1]['mp_cost'] <= hero.mp:
                delay_print_fast(
                    hero.skills[int(user_input[0]) - 1]['description'])
                print('\n')

                skill_damage = round((hero.attack * (random.randint(hero.skills[int(
                    user_input[0]) - 1]['dmg'][0], hero.skills[int(user_input[0]) - 1]['dmg'][1])/100)) - enemy.defense)

                delay_print_fast(
                    f'{hero.name} did {skill_damage} damage to {enemy.name}!')

                enemy.health -= skill_damage
                count += 2
                hero.ultimate_counter(hero, count)
                count = 0
                hero.mp -= hero.skills[int(user_input[0]) - 1]['mp_cost']
            else:
                delay_print_fast(
                    'You dont have enough mp to use that skill!' + '\n')
                continue
        elif user_input[0] in ['back', 'b']:
            clear()
            combat(hero, enemy)
        else:
            delay_print_fast(
                'Choose a number or type b, back, or 9 to go back!')
            continue

        # won battle
        if enemy.health <= 0:
            win(hero, enemy)
            skill_done = True
            # Using if statements to say where to go next since won't have random battles
            if hero.curRoom == room['castleDoors']:
                after_first_guard(hero)

        else:
            e_attack = round(
                (enemy.attack * (random.randint(100, 125)/100)) - hero.defense)
        delay_print_fast(
            f'\n{enemy.name} attacked {hero.name} for {e_attack} damage\n')
        hero.health -= e_attack
        count += 1
        hero.ultimate_counter(hero, count)

        if hero.health <= 0:
            lose()
        else:
            skill_done = True
            combat(hero, enemy)

# Using ultimate


def ulitmate(hero, enemy):
    clear()
    ulti_done = False

    while not ulti_done:

        delay_print_fast('\nChoose A Limit Break: \n')
        for i, ulti in enumerate(d for d in hero.ultimate):
            print(f'{i+1}.', ulti['name'])
        delay_print_fast(f'\nb. back')

        user_input = input("\n> ").strip().lower().split()

        if len(user_input) != 1:
            print('\nPress a number to use a Limit Break!')
            continue

        # Whatever number user presses will dynamically find the description for that move
        if user_input[0] in ['1', 'one']:
            clear()
            delay_print_fast(
                hero.ultimate[int(user_input[0]) - 1]['description'])

            ulti_damage = round((hero.attack * (random.randint(hero.ultimate[int(
                user_input[0]) - 1]['dmg'][0], hero.ultimate[int(user_input[0]) - 1]['dmg'][1])/100)) - enemy.defense)

            delay_print_fast(
                f'\n{hero.name} did {ulti_damage} damage to {enemy.name}!')

            enemy.health -= ulti_damage
            # Resetting ulti counter
            hero.ulti_counter = 0
        elif user_input[0] in ['back', 'b', '9']:
            clear()
            combat(hero, enemy)
        else:
            delay_print_fast(
                'Choose a number or type b, back, or 9 to go back!')
            continue

        # won battle
        if enemy.health <= 0:
            win(hero, enemy)
            ulti_done = True
            # Using if statements to say where to go next since won't have random battles
            if hero.curRoom == room['castleDoors']:
                after_first_guard(hero)

        else:
            e_attack = round(
                (enemy.attack * (random.randint(100, 125)/100)) - hero.defense)
        delay_print_fast(
            f'\n{enemy.name} attacked {hero.name} for {e_attack} damage\n')
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
        delay_print_fast(
            f'{hero.name} HP: {hero.health}     {enemy.name} HP: {enemy.health}\n')
        delay_print_fast(
            f'{hero.name} MP: {hero.mp}      {enemy.name} MP: {enemy.mp}\n')
        print("\n1. Attack")
        print("2. Skills")
        print("3. Items")
        if hero.ulti_counter >= 10:
            print("4. Limit Break")

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

        elif user_input[0] == '4' and hero.ulti_counter >= 10:
            ulitmate(hero, enemy)


def after_first_guard(hero):
    clear()
    print_location(hero)

    delay_print(
        f'\n Dumb Guard: I...will....get you scoun...drels...uhh\n')
    delay_print(
        f'\n Zidane: Looks like he is knocked out cold. Wedge and Zanbar lets hurry north through the castle doors. Lets go!\n')

    command = False
    while not command:

        user_input = input("\n> ").strip().lower().split()

        if len(user_input) != 1:
            print('There is no time! Lets go north through the castle doors!')
            continue

        if user_input[0] == 'quit' or user_input[0] == 'q':
            command = True
        elif user_input[0] in ["n", "north"]:
            thief.curRoom = thief.tryDirection(
                user_input[0], thief.curRoom)
            command = True
            clear()
            print_location(hero)
            delay_print(
                f'\n The three hurry along into the castle main floor. It is gorgeously decorated with red and purple carpets and a chandelier hangs in the middle of the room about 30 feet high. There is one staircase that leads to the second floor. There is a door to the east and west that leads to other rooms. With the festival going on in the town the castle floor is currently empty.\n')
            delay_print(
                f'\n Wedge: Wooahhhhh!! This place is beautiful! Also, Zidane you beat that guard to a pulp. I promise i was helping! How cool was it that I tricked him with the chocolate guys!?\n')
            delay_print(
                f'\n Zanbar: ARGGG...WHY YOU IDIOT. THIS ISNT FUN AND PLAY. WE ARE ON A VERY DANGEROUS SERIOUS MISSION! AND THIS IS THE ONLY TIME WE WILL BE ABLE TO GET THE PRINCESS WITHOUT THERE BEING NUMEROUS KNIGHTS HERE!  \n')
            delay_print(
                f'\n Wedge: Hey I said im sorry rude butt. Plus, the Royal Guards are with Queen Brahman at the fesitval. We only have to deal with these easy guards.\n')
            delay_print(
                f'\n Zanbar: Really? Seemed like you were crying just seeing one guard in front of the castle doors. And if you call me that again i promise in my family name i will stab you with my dagger imbecille. \n')
            delay_print(
                f'\n Zidane: Zanbar and Wedge! Stop this now! The Royal Guards may be protecting the Queen but there are still tough guards and knights here with the Princess. We need to stay on our guard. \n')
            delay_print(
                f'\n Zidane: Do you hear that? \n')
            delay_print(
                f'\n Zanbar: Up the stairs. They are coming from up there. Thats where the Princess has to be. What do we do Zidane? \n')
            delay_print(
                f'\n Wedge: Oh nooooo...we have to leave or else we will die!  \n')
            delay_print(
                f'\n Zanbar: You stupid imbec... \n')
            delay_print(
                f'\n Zidane: Hurry, follow me! \n')
            delay_print(
                f'\n "East". Run into the room to the east. \n')
            delay_print(
                f'\n "West". Run into the room to the west. \n')

            done = False
            while not done:

                user_input = input("\n> ").strip().lower().split()
                if len(user_input) != 1:
                    print(
                        'This isnt the time! Type the word "East", or "West"!')
                    continue
                if user_input[0] == 'quit' or user_input[0] == 'q':
                    done = True

                elif user_input[0] in ["e", "east"]:
                    thief.curRoom = thief.tryDirection(
                        user_input[0], thief.curRoom)
                    done = True
                    clear()
                    narratives.c_east()

                elif user_input[0] in ["w", "west"]:
                    thief.curRoom = thief.tryDirection(
                        user_input[0], thief.curRoom)
                    done = True
                    clear()
                    narratives.c_west()

        else:
            print('Lets go north to fight those guards! Type n or north!')


def opening():
    clear()
    # done = False

    print_location(thief)
    print_location_description
    # while not done:
    delay_print(
        f'\n Dumb Guard: HALT! You three! State your names right now and tell my why you are running so hurriedly to the castle?\n')
    delay_print(
        f'\n Zidane: Salutations my friend! We are merchants from Artherian. We were traveling here and we have wares that Queen Brahman and Princess Garnet would absolutely fall in love with! \n')
    delay_print(f'\n Dumb Guard: Merchants you say...I see, I see. The Princess has been down lately after her father passing, I am sure she would be delighted with gifts from another land. \n')
    delay_print(
        f'\n Zidane: I am sorry to hear that...such a sad occasion. I do hope that we can help and lift up their spirits in such a time.  \n')
    delay_print(f'\n Dumb Guard: No need to worry but I do appreciate your kind gestures. Unforntuately, the Queen is out for our yearly Alexandrian celebration in the city. The Princess is here though since she decided not to go...actually I dont think I should even be telling you this information in the first place. For all I know you three could be thieves. Plus, where exactly is all of your merchandise? You all look empty handed. \n')
    delay_print(
        f'\n Wedge: Ohh...haha...thieves? Us? What? Umm...umm..we arent empty handed just uhh... *sweat pouring down*  \n')
    delay_print(
        f'\n *Wedge reaches into his pocket and pulls out a melted chocolate bar*  \n')
    delay_print(
        f'\n Wedge: See...haha...this is Atherian finest chocolate...\n')
    delay_print(
        f'\n Wedge: *The guard stares at the chocolated with the most puzzled face and then proceeded to grab the chocolate*  \n')
    delay_print(
        f'\n Dumb Guard: .......Wow this is amazing! I have never seen chocolate like this in my entire life here in the castle. What a masterpiece of the Atherian people indeed.  \n')
    delay_print(f'\n *As Wedge went from being nervous to start smiling and laughing with Zidane and the guard, Zanbar was absolutely dumbfounded at how much of an idiot this guard is and how much of an idiot Wedge is for doing that.* \n')
    delay_print(f'\n Dumb Guard: AHAHA! You all seem trustworthy. I will take you to the Princess. She will be delighted to see what you all have brought.  \n')
    delay_print(
        f'\n Zidane: Thank you my good sir. Anything to help the Princess in her time of need. \n')
    delay_print(
        f'\n Dumb Guard: Right you are. Follow me! To the Princess we go. \n')
    delay_print(f'\n Wedge: Woohoo! I cant believe we fooled him guys! \n')
    delay_print(f'\n Dumb Guard: Wait...!! Why...you...you scoundrels!! \n')
    delay_print(
        f'\n Zanbar: WEDGE! YOU IMBECCILEEEE! DONT YOU KNOW TO KEEP YOUR FAT MOUTH SHUT! \n')
    delay_print(f'\n Wedge: AHHHHHH! Im sorry! Forgive me!! \n')
    delay_print(f'\n Zidane: Calm yourself you two! This is no time for bickering! Prepare yourselves for battle!! Lets make this quick and stay focused on the mission! \n')

    input("\n> ").strip().lower().split()
    # done = True
    clear()
    combat(thief, guard)

# Dialogue that occurs when starting the game


def opening_dialogue():
    clear()
    done = False

    print_location(thief)
    print_location_description(thief)
    while not done:
        delay_print(
            f'\nWedge: Crap! Crap! There is a guard right there blocking the entrance! There is no way we can kidnap the princess!\n')
        delay_print(
            f'\nZanbar: WEDGE if you dont stop this at once i will take out my dagger and end you myself!\n')
        delay_print(
            f'\n{thief.name}: Haha! Wedge there is no need to worry. Think about it. There are three of us and only one guard So what does that mean for us?\n')
        delay_print(f'\nWedge: Oh god no! That means we are triple dead??\n')
        delay_print(
            f'\nZanbar: WEDGE you imbeccile. Taste the fury of my Dagger Of A Thousand Stabs!\n')
        delay_print(f'\n{thief.name}: No need for that Zanbar. Wedge will grow out of it i assure you. For now follow my lead and trust me when I say this mission will be a success! Lets head north to the guard. Follow my lead!\n')
        delay_print(f'\nIn this game you will be able to choose directions to go in the terminal by typing the direction. For now we can only go north to the guard. Type n or north and continue forth!\n')

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
