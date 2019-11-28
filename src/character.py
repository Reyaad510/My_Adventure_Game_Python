from room import room
import random
from item import rusty_sword
from item import dagger
from item import knife
from item import leather_shield
from item import knight_shield
from item import headband
from item import loaf_of_bread
from item import small_potion
from item import ether_stone
from item import blue_potion
from item import arcane_potion
import os


# Base class for any character
class Character:
    def __init__(self, name, description, maxhealth, health, attack, defense, maxmp, mp, gold):
        self.name = name
        self.description = description
        self.maxhealth = maxhealth
        self.health = self.maxhealth
        self.attack = attack
        self.defense = defense
        self.maxmp = mp
        self.mp = mp
        self.gold = gold

    def __str__(self):
        return f'{self.name}:{self.description}'

# Hero Classes


class Hero(Character):
    def __init__(self, name, description, maxhealth, health, attack, defense, maxmp, mp, gold, skills, ultimate, ulti_counter, weapon, armor, startRoom=None, inventory=None):
        super().__init__(name, description, maxhealth,
                         health, attack, defense, maxmp, mp, gold)
        self.skills = skills
        self.ultimate = ultimate
        self.ulti_counter = ulti_counter
        self.weapon = weapon
        self.armor = armor
        self.curRoom = startRoom
        self.inventory = inventory

    def __str__(self):
        return f'{self.curRoom}'

    # Code that links rooms together. Importing from room
    def tryDirection(self, d, curRoom):
        attrib = d + '_to'

        if hasattr(curRoom, attrib):
            return getattr(curRoom, attrib)
        else:
            print("You cant go that way")

        return curRoom

    # Code that allows user to equip a weapon so far(havent' implemented armor)
    def inven(self, hero):
        items = False
        while not items:
            for i, x in enumerate(hero.inventory):
                print(f'{i+1}.', x.name)
            print(f'b. Back')

            # Dynamically equips items
            user_input_one = input("\n> ").strip().lower().split()
            if len(user_input_one) != 1:
                print('Try a different number or type b to go back!')
                continue

            elif user_input_one[0] in str(list(range(len(hero.inventory) + 1))):
                os.system('cls')
                os.system('clear')
                items = True
                print(hero.inventory[int(user_input_one[0])-1].name)
                print(hero.inventory[int(user_input_one[0]) - 1].description)
                # Equipping Weapon
                if hasattr(hero.inventory[int(user_input_one[0])-1], 'attack'):
                    print('Attack: ', hero.inventory[int(
                        user_input_one[0])-1].attack)
                    print('Want to equip this weapon?')
                    print('1. Yes')
                    print('2. No')
                    print("Equipped Weapon: ", hero.weapon[0].name)
                    print("Attack: ", hero.weapon[0].attack)
                    user_input = input("\n> ").strip().lower().split()
                    # If click enter with no text
                    if len(user_input) != 1:
                        print('Type 1 or 2!')
                        self.inven(hero)
                    # Equipping Weapon
                    elif user_input[0] in ['Yes', '1']:
                        hero.attack -= hero.weapon[0].attack
                        hero.inventory.append(hero.weapon[0])
                        hero.weapon.remove(hero.weapon[0])
                        hero.weapon.append(
                            hero.inventory[int(user_input_one[0]) - 1])
                        hero.attack += hero.weapon[0].attack
                        hero.inventory.remove(
                            hero.inventory[int(user_input_one[0]) - 1])
                        print('Equipped', hero.weapon[0].name)
                        print('Total Attack: ', hero.attack)
                        # print('Inv 0', hero.inventory)
                        self.inven(hero)
                    else:
                        os.system('cls')
                        os.system('clear')
                        self.inven(hero)
                # Equipping Armor
                elif hasattr(hero.inventory[int(user_input_one[0])-1], 'defense'):
                    print('Armor: ', hero.inventory[int(
                        user_input_one[0])-1].defense)
                    print('Want to equip this armor?')
                    print('1. Yes')
                    print('2. No')
                    print("Equipped Armor: ", hero.armor[0].name)
                    print("Defense: ", hero.armor[0].defense)
                    user_input = input("\n> ").strip().lower().split()
                    # If click enter with no text
                    if len(user_input) != 1:
                        print('Type 1 or 2!')
                        self.inven(hero)

                    if user_input[0] in ['Yes', '1']:
                        hero.defense -= hero.armor[0].defense
                        hero.inventory.append(hero.armor[0])
                        hero.armor.remove(hero.armor[0])
                        hero.armor.append(
                            hero.inventory[int(user_input_one[0]) - 1])
                        hero.defense += hero.armor[0].defense
                        hero.inventory.remove(
                            hero.inventory[int(user_input_one[0]) - 1])
                        print('Equipped', hero.armor[0].name)
                        print("Total Defense: ", hero.defense)
                        # print('Inv 0', hero.inventory)
                        self.inven(hero)
                    else:
                        os.system('cls')
                        os.system('clear')
                        self.inven(hero)
                # Using a healing item from inventory
                elif hasattr(hero.inventory[int(user_input_one[0])-1], 'health'):
                    print('Want to use this to restore health?')
                    print('1. Yes')
                    print('2. No')
                    print(f'Current Health: {hero.health}/{hero.maxhealth} ')
                    user_input = input("\n> ").strip().lower().split()
                    # If click enter with no text
                    if len(user_input) != 1:
                        print('Type 1 or 2!')
                        self.inven(hero)

                    if user_input[0] in ['Yes', '1']:
                        if(hero.health == hero.maxhealth):
                            print(
                                'You are already all full HP! No need to waste that!')
                            self.inven(hero)
                        elif hero.health + hero.inventory[int(
                                user_input_one[0])-1].health > hero.maxhealth:
                            hero.health = hero.maxhealth
                            hero.inventory.remove(
                                hero.inventory[int(user_input_one[0]) - 1])
                            print(
                                f'Total Health: {hero.health}/{hero.maxhealth}')
                            # print('Inv 0', hero.inventory)
                            self.inven(hero)
                        else:
                            hero.health += hero.inventory[int(
                                user_input_one[0])-1].health
                            hero.inventory.remove(
                                hero.inventory[int(user_input_one[0]) - 1])
                            print(
                                f'Total Health:{hero.health}/{hero.maxhealth}')
                            # print('Inv 0', hero.inventory)
                            self.inven(hero)
                    else:
                        os.system('cls')
                        os.system('clear')
                        self.inven(hero)

                # Using MP item from inventory
                elif hasattr(hero.inventory[int(user_input_one[0])-1], 'mp'):
                    print('Want to use this to restore MP?')
                    print('1. Yes')
                    print('2. No')
                    print(f'Current MP: {hero.mp}/{hero.maxmp} ')
                    user_input = input("\n> ").strip().lower().split()
                    # If click enter with no text
                    if len(user_input) != 1:
                        print('Type 1 or 2!')
                        self.inven(hero)

                    if user_input[0] in ['Yes', '1']:
                        if(hero.mp == hero.maxmp):
                            print(
                                'You are already all full MP! No need to waste that!')
                            self.inven(hero)
                        elif hero.mp + hero.inventory[int(
                                user_input_one[0])-1].mp > hero.maxmp:
                            hero.mp = hero.maxmp
                            hero.inventory.remove(
                                hero.inventory[int(user_input_one[0]) - 1])
                            print(f'Total MP:{hero.mp}/{hero.maxmp}')
                            # print('Inv 0', hero.inventory)
                            self.inven(hero)
                        else:
                            hero.mp += hero.inventory[int(
                                user_input_one[0])-1].mp
                            hero.inventory.remove(
                                hero.inventory[int(user_input_one[0]) - 1])
                            print(f'Total MP:{hero.mp}/{hero.maxmp}')
                            # print('Inv 0', hero.inventory)
                            self.inven(hero)
                    else:
                        os.system('cls')
                        os.system('clear')
                        self.inven(hero)

            elif user_input_one[0] == 'b':
                print('Going back!')
                items = True

    def ultimate_counter(self, hero, num):
        counter = hero.ulti_counter
        counter += num
        hero.ulti_counter = counter

    # Code that allows user to use an item during combat)

    def use_item(self, hero):
        items = False
        while not items:
            for i, x in enumerate(hero.inventory):
                print(f'{i+1}.', x.name)
            print(f'b. Back')

            # Dynamically equips items
            user_input_one = input("\n> ").strip().lower().split()
            if len(user_input_one) != 1:
                print('Try a different number or type b to go back!')
                continue

            elif user_input_one[0] in str(list(range(len(hero.inventory) + 1))):
                os.system('cls')
                os.system('clear')
                items = True
                print(hero.inventory[int(user_input_one[0])-1].name)
                print(hero.inventory[int(user_input_one[0]) - 1].description)
                # Can't select weapon
                if hasattr(hero.inventory[int(user_input_one[0])-1], 'attack'):
                    print(
                        'There is no time to switch weapons during a fight! Choose an item instead!')
                    self.use_item(hero)

                # Can't select armor
                elif hasattr(hero.inventory[int(user_input_one[0])-1], 'defense'):
                    print(
                        'There is no time to switch armor during a fight! Choose an item instead!')
                    self.use_item(hero)

                # Using a healing item from inventory
                elif hasattr(hero.inventory[int(user_input_one[0])-1], 'health'):
                    print('Want to use this to restore health?')
                    print('1. Yes')
                    print('2. No')
                    print(f'Current Health: {hero.health}/{hero.maxhealth} ')
                    user_input = input("\n> ").strip().lower().split()
                    # If click enter with no text
                    if len(user_input) != 1:
                        print('Type 1 or 2!')
                        self.use_item(hero)

                    if user_input[0] in ['Yes', '1']:
                        if(hero.health == hero.maxhealth):
                            print(
                                'You are already all full HP! No need to waste that!')
                            self.use_item(hero)
                        elif hero.health + hero.inventory[int(
                                user_input_one[0])-1].health > hero.maxhealth:
                            hero.health = hero.maxhealth
                            hero.inventory.remove(
                                hero.inventory[int(user_input_one[0]) - 1])
                            print(
                                f'Total Health: {hero.health}/{hero.maxhealth}')
                            # print('Inv 0', hero.inventory)
                            self.use_item(hero)
                        else:
                            hero.health += hero.inventory[int(
                                user_input_one[0])-1].health
                            hero.inventory.remove(
                                hero.inventory[int(user_input_one[0]) - 1])
                            print(
                                f'Total Health:{hero.health}/{hero.maxhealth}')
                            # print('Inv 0', hero.inventory)
                            self.use_item(hero)
                    else:
                        os.system('cls')
                        os.system('clear')
                        self.use_item(hero)

                # Using MP item from inventory
                elif hasattr(hero.inventory[int(user_input_one[0])-1], 'mp'):
                    print('Want to use this to restore MP?')
                    print('1. Yes')
                    print('2. No')
                    print(f'Current MP: {hero.mp}/{hero.maxmp} ')
                    user_input = input("\n> ").strip().lower().split()
                    # If click enter with no text
                    if len(user_input) != 1:
                        print('Type 1 or 2!')
                        self.use_item(hero)

                    if user_input[0] in ['Yes', '1']:
                        if(hero.mp == hero.maxmp):
                            print(
                                'You are already all full MP! No need to waste that!')
                            self.use_item(hero)
                        elif hero.mp + hero.inventory[int(
                                user_input_one[0])-1].mp > hero.maxmp:
                            hero.mp = hero.maxmp
                            hero.inventory.remove(
                                hero.inventory[int(user_input_one[0]) - 1])
                            print(f'Total MP:{hero.mp}/{hero.maxmp}')
                            # print('Inv 0', hero.inventory)
                            self.use_item(hero)
                        else:
                            hero.mp += hero.inventory[int(
                                user_input_one[0])-1].mp
                            hero.inventory.remove(
                                hero.inventory[int(user_input_one[0]) - 1])
                            print(f'Total MP:{hero.mp}/{hero.maxmp}')
                            # print('Inv 0', hero.inventory)
                            self.use_item(hero)
                    else:
                        os.system('cls')
                        os.system('clear')
                        self.use_item(hero)

            elif user_input_one[0] == 'b':
                print('Going back!')
                items = True


class Villain(Character):
    def __init__(self, name, description, maxhealth, health, attack, defense, maxmp, mp, gold, skills, ultimate, laugh):
        super().__init__(name, description, maxhealth,
                         health, attack, defense, maxmp, mp, gold)
        self.skills = skills
        self.ultimate = ultimate
        self.laugh = laugh


class NormalEnemy(Character):
    def __init__(self, name, description, maxhealth, health, attack, defense, maxmp,  mp, gold, items=None):
        super().__init__(name, description, maxhealth,
                         health, attack, defense, maxmp, mp, gold)
        self.items = items


heroes = {
    'knight': Hero(
        'Sir Steiner', 'Protector of the Queen Brahman and Princess Garnet of Alexandria, Sir Steiner has sworn his life to them.', 100, 100, 10, 8, 12, 12, 25, ['SwordSlash', 'FireStrike'], 'Knights of The Round Table', 0, 'Bronze Sword', 'Knight Armor'),

    'mage': Hero(
        'Vivi', 'A young mage that lives in Alexandria with his grandfather. He is humble, but his training in magic makes him a deadly opponent', 100, 100, 10, 8, 20, 20, 25, ['Fire', 'Ice'], 'Meteor', 0, 'Old Staff', 'Apprentice Robes'),

    'thief': Hero('Zidane', 'A smart mouth thief that has the duty of kidnapping Princess Garnet along with his crew of bandit. His wits and charm saves him in the most unexpected situations', 100, 100, 8, 8, 15, 15, 25, [{
        'name': 'Sneak Attack',
        'description': 'While the others disctract the enemy, Zidane flanks them from the side with a surprise attack!',
        'dmg': [200, 250],
        'mp_cost': 5
    },
        {'name': 'Charmer',
            'description': 'Using his wits and ability to converse with people. Zidane makes the enemy feel comfortable around him.',
            'dmg': [150, 175],
            'mp_cost': 3
         }],
        [{
            'name': 'BackStab',
            'description': 'A fatal blow to the back of the enemys back. Hurt as much as a betrayal from someone you thought was a true friend.',
            'dmg': [300, 400]}], 0, [dagger], [headband], room['outside'], [small_potion]),

    'healer': Hero('Garnet', 'The daughter of Queen Brahman, Garnet is the princess of Alexandria. She does not see eye to eye with her mother after her father passed after unusual circumstances and she wishes for more than anything to leave the life she has now for something more simple.', 100, 100, 10, 8, 25, 25, 25, ['Cure', 'Barrier'], 'Healing Wind', 0, 'Royal Staff', 'Silky Dress')
}
boss = {
    'obelisk': Villain('Obelisk', 'A royal knight that protects Queen Brahman and Princess Garnet. Ever since the infamous Battle of Alexandria, his armor was stained with the blood of many civilians. He is known as the Blood Knight to everyone in the city', 100,  100, 10, 8, 20, 20, 25, ['Sanguine Strike', 'No Mercy'], 'Blood Explosion', 'HMPH!'),

    'queen': Villain("Queen Brahman", 'The Queen of Alexandria who is also a widow. Her husband passed away leaving her to rule the kingdom along with her daughter Princess Garnet. Garnet and her do not see eye to eye after the father passed and she wants Garnet to take over the Kingdom', 100, 100, 10, 8, 40, 40, 25, ['Summon Guard', 'Summon Chef'], 'Summon Royal Knight', 'Ahahahahah!'),
}

normal_enemy = {
    'normal_guard': NormalEnemy('Normal Guard', 'Just a normal guard of the queen. Nothing amazing here', 100, 100, 10, 3, 5, 5, 100, [rusty_sword, knife, leather_shield, knight_shield, loaf_of_bread, small_potion, ether_stone, arcane_potion, blue_potion])
}
