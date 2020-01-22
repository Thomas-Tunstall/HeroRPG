#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee
class Hero:                                             #Hero Class
    def __init__(self, health, power):
        self.health = health
        self.power = power
        
    def hero_attack(self, othercharater): #module
        othercharater.health -= self.power
        print("You do {} damage to the goblin.".format(self.power))

    def hero_alive(self):
        while self.health > 0:
            return True
        else:
            return False

        

class Goblin:                                           #Goblin Class
    def __init__(self, health, power): 
        self.health = health
        self.power = power
    
    def goblin_attack(self, othercharater): #module
        othercharater.health -= self.power
        print("The goblin does {} damage to you.".format(self.power))
    
    def goblin_alive(self):
        if self > 0:
            return True
        else:
            return False

spiderman = Hero(10, 8)
goblinman = Goblin(6, 2)


def main():



    while spiderman.health > 0 and goblinman.health > 0:
        print("You have {} health and {} power.".format(spiderman.health, spiderman.power))
        print("The goblin has {} health and {} power.".format(goblinman.health, goblinman.power))
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # spiderman attacks goblin
            spiderman.health -= goblinman.power
            if goblinman.health <= 0:
                print("The goblin is dead.")
            # Hero.attack(Goblin)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if goblinman.health > 0:
            # Goblin attacks hero
            goblinman.health -= spiderman.power
            print("The goblin does {} damage to you.".format(goblinman.power))
            if spiderman.health <= 0:
                print("You are dead.")

main()

# def main():
#     while goblin_health > 0 and hero_health > 0:
#         print("You have {} health and {} power.".format(hero_health, hero_power))
#         print("The goblin has {} health and {} power.".format(goblin_health, goblin_power))
#         print()
#         print("What do you want to do?")
#         print("1. fight goblin")
#         print("2. do nothing")
#         print("3. flee")
#         print("> ", end=' ')
#         raw_input = input()
#         if raw_input == "1":
#             # Hero attacks goblin
#             goblin_health -= hero_power
#             print("You do {} damage to the goblin.".format(hero_power))
#             if goblin_health <= 0:
#                 print("The goblin is dead.")
#             # Hero.attack(Goblin)
#         elif raw_input == "2":
#             pass
#         elif raw_input == "3":
#             print("Goodbye.")
#             break
#         else:
#             print("Invalid input {}".format(raw_input))

#         if goblin_health > 0:
#             # Goblin attacks hero
#             hero_health -= goblin_power
#             print("The goblin does {} damage to you.".format(goblin_power))
#             if hero_health <= 0:
#                 print("You are dead.")

# main()