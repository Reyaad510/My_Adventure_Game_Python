from room import room


class Character:
    def __init__(self, name, description, maxhealth, health, attack):
        self.name = name
        self.description = description
        self.maxhealth = maxhealth
        self.health = self.maxhealth
        self.attack = attack

    def __str__(self):
        return f'{self.name}:{self.description}'


class Hero(Character):
    def __init__(self, name, description, maxhealth, health, attack, skills, ultimate, startRoom=None):
        super().__init__(name, description, maxhealth, health, attack)
        self.skills = skills
        self.ultimate = ultimate
        self.curRoom = startRoom

    def __str__(self):
        return f'{self.curRoom}'

    def tryDirection(self, d, curRoom):
        attrib = d + '_to'

        if hasattr(curRoom, attrib):
            return getattr(curRoom, attrib)
        else:
            print("You cant go that way")

        return curRoom


class Villain(Character):
    def __init__(self, name, description, maxhealth, health, attack, skills, ultimate, laugh):
        super().__init__(name, description, maxhealth, health, attack)
        self.skills = skills
        self.ultimate = ultimate
        self.laugh = laugh


heroes = {
    'knight': Hero(
        'Sir Steiner', 'Protector of the Queen Brahman and Princess Garnet of Alexandria, Sir Steiner has sworn his life to them.', 100, 100, 10, ['SwordSlash', 'FireStrike'], 'Knights of The Round Table'),

    'mage': Hero(
        'Vivi', 'A young mage that lives in Alexandria with his grandfather. He is humble, but his training in magic makes him a deadly opponent', 100, 100, 10, ['Fire', 'Ice'], 'Meteor'),

    'thief': Hero('Zidane', 'A smart mouth thief that has the duty of kidnapping Princess Garnet along with his crew of bandit. His wits and charm saves him in the most unexpected situations', 100, 100, 10, ['Sneak Attack', 'Charm Talk'], 'Backstab', room['outside']),

    'healer': Hero('Garnet', 'The daughter of Queen Brahman, Garnet is the princess of Alexandria. She does not see eye to eye with her mother after her father passed after unusual circumstances and she wishes for more than anything to leave the life she has now for something more simple.', 100, 100, 10, ['Cure', 'Barrier'], 'Healing Wind')
}
boss = {
    'obelisk': Villain('Obelisk', 'A royal knight that protects Queen Brahman and Princess Garnet. Ever since the infamous Battle of Alexandria, his armor was stained with the blood of many civilians. He is known as the Blood Knight to everyone in the city', 100,  100, 10, ['Sanguine Strike', 'No Mercy'], 'Blood Explosion', 'HMPH!'),

    'queen': Villain("Queen Brahman", 'The Queen of Alexandria who is also a widow. Her husband passed away leaving her to rule the kingdom along with her daughter Princess Garnet. Garnet and her do not see eye to eye after the father passed and she wants Garnet to take over the Kingdom', 100, 100, 10, ['Summon Guard', 'Summon Chef'], 'Summon Royal Knight', 'Ahahahahah!'),
}

normal_enemy = {
    'normal_guard': Character('Normal guard', 'Just a normal guard of the queen. Nothing amazing here', 20, 20, 5)
}


# knight = Character(
#     'Sir Steiner', 'Protector of the Queen Brahman and Princess Garnet of Alexandria, Sir Steiner has sworn his life to them.', 'SwordSlash')

# mage = Character(
#     'Vivi', 'A young mage that lives in Alexandria with his grandfather. He is humble, but his training in magic makes him a deadly opponent', 'Meteor')

# thief = Character('Zidane', 'A smart mouth thief that has the duty of kidnapping Princess Garnet along with his crew of bandit. His wits and charm saves him in the most unexpected situations', 'Backstab')

# villain = Character('Obelisk', 'A knight that used to protect Queen Brahman and went missing after a mission. He returned as a dark knight to destroy the Queen and all of Alexandria.', 'Dark Matter')
