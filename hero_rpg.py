#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee
class Character:
    def __init__(self, health, power, name):
        self.health = health
        self.power = power
        self.name = name

    def attack(self, othercharater): #module
        othercharater.health -= self.power
        print("You do {} damage to the {}.".format(self.power, othercharater))

    def alive(self):
        while self.health > 0:
            return True
        else:
            return False

    def status(self):
         print("{} has {} health and {} power.".format(self.name, self.health, self.power))


class Hero(Character):                                             #Hero Class
    def __init__(self, health, power, name):
        super(Hero, self).__init__(health, power, name)
        

class Goblin(Character):
    def __init__(self, health, power, name):
        super(Goblin, self).__init__(health, power, name)




spiderman = Hero(10, 5, "Spiderman the Great")
goblinman = Goblin(6, 2, "Goblinman the Foul")


def main():



    while spiderman.alive() and goblinman.alive():
        print(spiderman.status())
        print(goblinman.status())
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            spiderman.attack(goblinman)
            if goblinman.health <= 0:
                print("The goblin is dead.")
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if goblinman.health > 0:
            goblinman.attack(spiderman)
            if spiderman.health <= 0:
                print("You are dead.")

main()



# def main():



#     while spiderman.health > 0 and goblinman.health > 0:
#         print("You have {} health and {} power.".format(spiderman.health, spiderman.power))
#         print("The goblin has {} health and {} power.".format(goblinman.health, goblinman.power))
#         print()
#         print("What do you want to do?")
#         print("1. fight goblin")
#         print("2. do nothing")
#         print("3. flee")
#         print("> ", end=' ')
#         raw_input = input()
#         if raw_input == "1":
#             # spiderman attacks goblin
#             spiderman.health -= goblinman.power
#             if goblinman.health <= 0:
#                 print("The goblin is dead.")
#             # Hero.attack(Goblin)
#         elif raw_input == "2":
#             pass
#         elif raw_input == "3":
#             print("Goodbye.")
#             break
#         else:
#             print("Invalid input {}".format(raw_input))

#         if goblinman.health > 0:
#             # Goblin attacks hero
#             goblinman.health -= spiderman.power
#             print("The goblin does {} damage to you.".format(goblinman.power))
#             if spiderman.health <= 0:
#                 print("You are dead.")

# class Hero:                                             #Hero Class
#     def __init__(self, health, power):
#         self.health = health
#         self.power = power
        
#     def attack(self, othercharater): #module
#         othercharater.health -= self.power
#         print("You do {} damage to the goblin.".format(self.power))

#     def alive(self):
#         while self.health > 0:
#             return True
#         else:
#             return False

#     def status(self):
#          print("The goblin has {} health and {} power.".format(spiderman.health, spiderman.power))

        

# class Goblin:                                           #Goblin Class
#     def __init__(self, health, power): 
#         self.health = health
#         self.power = power
    
#     def attack(self, othercharater): #module
#         othercharater.health -= self.power
#         print("The goblin does {} damage to you.".format(self.power))
    
#     def alive(self):
#         if self.health > 0:
#             return True
#         else:
#             return False
    
#     def status(self):
#         print("The goblin has {} health and {} power.".format(goblinman.health, goblinman.power))
