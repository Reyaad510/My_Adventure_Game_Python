from room import room
from item import rusty_sword
from item import dagger
from item import knife
import os


# Base class for any character
class Character:
    def __init__(self, name, description, maxhealth, health, attack, defense, mp, gold):
        self.name = name
        self.description = description
        self.maxhealth = maxhealth
        self.health = self.maxhealth
        self.attack = attack
        self.defense = defense
        self.mp = mp
        self.gold = gold

    def __str__(self):
        return f'{self.name}:{self.description}'

# Hero Classes


class Hero(Character):
    def __init__(self, name, description, maxhealth, health, attack, defense, mp, gold, skills, ultimate, weapon, startRoom=None, inventory=None):
        super().__init__(name, description, maxhealth, health, attack, defense, mp, gold)
        self.skills = skills
        self.ultimate = ultimate
        self.weapon = weapon
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
                print(f'\n{i+1}.', x.name)
            print(f'9. Back')

            # Dynamically equips items
            user_input_one = input("\n> ").strip().lower().split()
            if user_input_one[0] in ['1', '2', '3', '4']:
                os.system('cls')
                os.system('clear')
                items = True
                print(hero.inventory[int(user_input_one[0])-1].name)
                print(hero.inventory[int(user_input_one[0]) - 1].description)
                print('Damage: ', hero.inventory[int(
                    user_input_one[0])-1].attack)
                print('Want to equip this weapon?')
                print('1. Yes')
                print('2. No')
                print("Equipped Weapon: ", hero.weapon[0].name)
                print("Damage: ", hero.weapon[0].attack)
                user_input = input("\n> ").strip().lower().split()
                if user_input[0] in ['Yes', '1']:
                    hero.attack -= hero.weapon[0].attack
                    hero.inventory.append(hero.weapon[0])
                    hero.weapon.remove(hero.weapon[0])
                    hero.weapon.append(
                        hero.inventory[int(user_input_one[0]) - 1])
                    hero.attack += hero.weapon[0].attack
                    hero.inventory.remove(
                        hero.inventory[int(user_input_one[0]) - 1])
                    print('Equipped', hero.weapon[0].name)
                    print(hero.attack)
                    print('Inv 0', hero.inventory)
                    self.inven(hero)
                else:
                    os.system('cls')
                    os.system('clear')
                    self.inven(hero)

            elif user_input_one[0] in ['9', 'Back']:
                os.system('cls')
                os.system('clear')
                


class Villain(Character):
    def __init__(self, name, description, maxhealth, health, attack, defense, mp, gold, skills, ultimate, laugh):
        super().__init__(name, description, maxhealth, health, attack, defense, mp, gold)
        self.skills = skills
        self.ultimate = ultimate
        self.laugh = laugh


class NormalEnemy(Character):
    def __init__(self, name, description, maxhealth, health, attack, defense, mp, gold, items=None):
        super().__init__(name, description, maxhealth, health, attack, defense, mp, gold)
        self.items = items


heroes = {
    'knight': Hero(
        'Sir Steiner', 'Protector of the Queen Brahman and Princess Garnet of Alexandria, Sir Steiner has sworn his life to them.', 100, 100, 10, 8, 10, 25, ['SwordSlash', 'FireStrike'], 'Knights of The Round Table', 'Bronze Sword'),

    'mage': Hero(
        'Vivi', 'A young mage that lives in Alexandria with his grandfather. He is humble, but his training in magic makes him a deadly opponent', 100, 100, 10, 8, 10, 25, ['Fire', 'Ice'], 'Meteor', 'Old Staff'),

    'thief': Hero('Zidane', 'A smart mouth thief that has the duty of kidnapping Princess Garnet along with his crew of bandit. His wits and charm saves him in the most unexpected situations', 100, 100, 10, 8, 10, 25, [{
        'name': 'Sneak Attack',
        'description': 'I sneak behind and stab them to death',
        'dmg': 100,
        'mp_cost': 5
    },
        {'name': 'Charm Attack',
            'description': 'I charm them',
            'dmg': 5,
            'mp_cost': 3
         }], 'Backstab', [dagger], room['outside'], []),

    'healer': Hero('Garnet', 'The daughter of Queen Brahman, Garnet is the princess of Alexandria. She does not see eye to eye with her mother after her father passed after unusual circumstances and she wishes for more than anything to leave the life she has now for something more simple.', 100, 100, 10, 8, 10, 25, ['Cure', 'Barrier'], 'Healing Wind', 'Mage Staff')
}
boss = {
    'obelisk': Villain('Obelisk', 'A royal knight that protects Queen Brahman and Princess Garnet. Ever since the infamous Battle of Alexandria, his armor was stained with the blood of many civilians. He is known as the Blood Knight to everyone in the city', 100,  100, 10, 8, 10, 25, ['Sanguine Strike', 'No Mercy'], 'Blood Explosion', 'HMPH!'),

    'queen': Villain("Queen Brahman", 'The Queen of Alexandria who is also a widow. Her husband passed away leaving her to rule the kingdom along with her daughter Princess Garnet. Garnet and her do not see eye to eye after the father passed and she wants Garnet to take over the Kingdom', 100, 100, 10, 8, 10, 25, ['Summon Guard', 'Summon Chef'], 'Summon Royal Knight', 'Ahahahahah!'),
}

normal_enemy = {
    'normal_guard': NormalEnemy('Normal Guard', 'Just a normal guard of the queen. Nothing amazing here', 20, 20, 5, 8, 5, 100, [rusty_sword, knife])
}
