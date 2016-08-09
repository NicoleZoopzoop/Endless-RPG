"""Endless RPG

"""

from random import randint
from sys import exit

BORDER = "----------------------------------------------"

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

    def windup_attack(self):
        if self.winding_up == True:   
            print("A powerful blow!\n")
            self.winding_up = False
            return self.atk * 2
        
        else:
            self.winding_up = True
            print("Gathering strength...\n")
            return 0

#Characters are either Players, or Enemys

#this is a placeholder Enemy, controlled by rolls
class Enemy(Character):
    def __init__(self, name):
        super(Enemy, self).__init__(name,
                                    randint(1, player.hp),
                                    randint(int(player.atk / 2), player.atk))


#the Player is controlled by user input
class Player(Character):

    def __init__(self, name, hp, atk):
        super(Player, self).__init__(name, hp, atk)

###################################################################
#Game loop and friends!
#instantiate player
player = Player("Kiki", 50, 5)
print("You enter the Dungeon of Doom and Glory!\n")
print(player)

#declare general character placeholder variables for use during turns
turn_taker = ""
turn_takers_opponent = ""

while player.hp > 0:
    #round begins!
    #instantiate monster
    enemy = Enemy("monster")
    print("\nA monster appears!\n")
    print(enemy)
    print("\n")

    if randint(1, 2) == 1:
        print("They get the jump on you!\n")
        turn_taker = enemy
        turn_takers_opponent = player

    else:
        print("You sneak up on them...\n")
        turn_taker = player

    #condition for whether a new round is started
    while enemy.hp > 0:
        #check if player is alive
        if player.hp <= 0:
            #player death
            print("You have died! You should have made better decisions!\nTry again if you dare!\n")
            exit()
            
        #logic for enemy's turn
        if turn_taker == enemy:
            print("Monster attacks!\n")
            roll_selection = randint(1,4)

            #makes it easier for player to clock windup attacks
            if enemy.winding_up == True:
                roll_selection = 3

            #enemy makes its selection
            if roll_selection == 1:
                print("Monster uses its regular attack.\n")
                player.take_damage(enemy.attack())
                print(player)

                turn_taker = player

            elif roll_selection == 2:
                print("Monster takes a chance and uses its risky attack!\n")  
                player.take_damage(enemy.risky_attack())
                print(player)

                turn_taker = player

            elif roll_selection == 3:
                print("Monster takes an unusual stance...")
                player.take_damage(enemy.windup_attack())
                print(player)

                turn_taker = player

            else:
                print("Monster puts arms in front of face...")
                enemy.blocking = True

                turn_taker = player
            
            print("\n" + BORDER + "\n")

        #logic for player's turn
        elif turn_taker == player:
            print("\nWhat shall you do?\n1: Attack\n2: Risky attack\n3: Wind-up attack\nor\n4: Block\n")
            decision = input("Enter one of the above options via it's number: ")
            print("\n" + BORDER + "\n")            

            if decision == 1:
                print("You strike the monster with your normal attack...\n")
                enemy.take_damage(player.attack())
                print(enemy)
                
                turn_taker = enemy

            elif decision == 2:
                print("This technique is difficult... you try to attack anyway...\n")
                enemy.take_damage(player.risky_attack())
                print(enemy)
                
                turn_taker = enemy
            
            elif decision == 3:
                print("You try to concentrate your energy...\n")
                enemy.take_damage(player.windup_attack())
                print(enemy)

                turn_taker = enemy

            else:
                print("You raise your shield...\n")
                player.blocking = True

                turn_taker = enemy

        else:
            input("Whose turn is it??????")
    #round reward and cleanup
    print("Enemy defeated! Player HP replenished by 10 and ATK raised by 2!\n")
    player.hp += 10
    player.atk += 2
    player.blocking = False
    player.winding_up = False
    print("\n" + BORDER + "\n")

