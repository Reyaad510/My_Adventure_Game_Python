

class Character:
    def __init__(self, name, description, ultimate):
        self.name = name
        self.description = description

    def __str__(self):
        return f'{self.name}:{self.description}'


knight = Character(
    'Sir Steiner', 'Protector of the Queen Brahman and Princess Garnet of Alexandria, Sir Steiner has sworn his life to them.', 'SwordSlash')

mage = Character('Vivi', , 'A young mage that lives in Alexandria with his grandfather. He is humble, but his training in magic makes him a deadly opponent', 'Meteor')

thief = Character('Zidane', 'A smart mouth thief that has the duty of kidnapping Princess Garnet along with his crew of bandit. His wits and charm saves him in the most unexpected situations', 'Backstab')

villain = Character('Obelisk', 'A knight that used to protect Queen Brahman and went missing after a mission. He returned as a dark knight to destroy the Queen and all of Alexandria.', 'Dark Matter')
