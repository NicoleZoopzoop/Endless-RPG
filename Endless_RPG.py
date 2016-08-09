"""Endless RPG

"""

from random import randint

class Character(object):
    """Character objects are the combatants
    taking turns in the battle loop.

    Attributes:
        name (str):
        hp (int):
        ...

    """

    def __init__(self, name, hp, atk):
        """Create a character from basic stats.

        Arguments:
            name (str): asdfasdf
            hp (int): asdfasfd
            atk (int): asdfasdf

        """

        self.name = name
        self.hp = hp
        self.atk = atk
        self.alive = True
        self.blocking = False
        self.winding_up = False

    def __str__(self):
        return '<Character "%s" hp=%s atk=%s>' % (self.name, self.hp, self.atk)
    def take_damage(self, damage):
        """Handle the supplied amount of damage
        this character is supposed to take.

        Arguments:
            damage (int): Damage to take.

        """

        if self.blocking:        
            self.hp -= int(damage / 3)
            self.blocking = False        
        else:
            self.hp -= damage
    
    #character action options

    def attack(self):
        return randint((int(self.atk / 2)), self.atk)


    def risky_attack(self):
        if randint(1, 5) == 5:
            print("Risky attack suceeds!\n")
            return self.atk*2
    
        else:  
            print("Risky attack fails!\n")
            return int(self.atk / 10)

    def windup_attack(self, target):
        if self.winding_up == True:   
            print("A powerful blow!")
            self.winding_up = False
            return self.atk * 2
        
        else:
            self.winding_up = True
            print("Gathering strength...\n")


#Characters are either Players, or Enemys

#this is a placeholder Enemy
class Enemy(Character):
    def __init__(self, name):
        super(Enemy, self).__init__(name,
                                    randint(1, player.hp),
                                    randint(1, player.atk))


#the Player
class Player(Character):

    def __init__(self, name, hp, atk):
        super(Player, self).__init__(name, hp, atk)


#tests
player = Player("Kiki", 100, 10)
enemy = Enemy("monster")
print(player)
print(enemy)
