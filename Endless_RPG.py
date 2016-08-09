#Endless RPG:
'''
   
'''
from random import randint

#Character objects are the combatants taking turns in the battle loop
class Character:
    def __init__(self, name, hp, atk):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.alive = True
        self.blocking = False
        self.winding_up = False

    #damage handling, also checks if character taking damage is blocking
    def take_damage(self, damage):
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
    def __init__(self, Player):
        super(Enemy, self).__init__()
        self.name = 'monster'
        self.hp = randint(1, player.hp)
        self.atk = randint(1, player.atk)

#the Player
class Player(Character):
    def __init__(self):
        super(Character, self).__init__()
        self.name = 'you'
        self.hp = 10
        self.atk = 290
        

#tests


