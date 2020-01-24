#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

import random
import time

class Character:
    def __init__(self, health, power, name):
        self.health = health
        self.power = power
        self.name = name

    def attack(self, othercharater): #module
        othercharater.health -= self.power
        print("{} do {} damage to the {}.".format(self.name, self.power, othercharater.name))
        if othercharater.health <= 0:
            print("{} has been slain!".format(othercharater.name))

    def alive(self):
        while self.health > 0:
            return True
        else:
            return False

    def status(self):
         print("{} has {} health and {} power.".format(self.name, self.health, self.power))


class Hero(Character):
    def attack(self, othercharater):
        self.damage = self.power * self.crit()
        othercharater.health -= self.damage
        print(f"{self.name} has dealt {self.damage} to {othercharater.name}")
        if othercharater.health <= 0:
            print(f"{othercharater.name} has been slain!") 

    def crit(self):
        self.critDamage = 1
        critChance = random.randint(1, 5)
        if critChance == 5:
            print(f'{self.name} has landed a critical blow against!')
            self.critDamage = self.power * 2
            return self.critDamage
        else:
            self.critDamage = 1
            return self.critDamage

class Goblin(Character):
    pass

class Zombie(Character):
    def alive(self):
        return True

class Medic(Character):
    def heal(self):
        healChance = random.randint(1, 5)
        if healChance != 5:
            self.health += 2
            print('Blessed by RNGsus, the Medic has healed itself by 2!')

class Shade(Character):
    def ghastly(self, othercharater):
        dodgeChance = random.randint(1, 10)
        if dodgeChance == 10:
            self.health -= othercharater.power
            print("{} do {} damage to the {}.".format(self.name, self.power, othercharater.name))
            if othercharater.health <= 0:
                print("{} has been slain!".format(othercharater.name))
        else:
            othercharater.power = 0
            print("{} swung and {} nimbly dodged the strike!".format(othercharater.name, self.name))

class Barbarian(Character):
    def attack(self, othercharater):
        self.power = random.randint(5, 13)
        othercharater.health -= self.power
        print("{} do {} damage to the {}.".format(self.name, self.power, othercharater.name))
        if othercharater.health <= 0:
            print("{} has been slain!".format(othercharater.name))






class Battle:
    def battle_loop(self, PC, othercharater):
        print("=====The Battle Begins=====")
        print("{} takes on {}".format(PC.name, othercharater.name))
        while PC.alive() and othercharater.alive():
            print(PC.status())
            print(othercharater.status())
            print("======What will you do?=====")
            print("1. Fight {}".format(othercharater.name))
            print("2. Stand your ground... and do nothing")
            print("3. Flee")
            print("> ", end=' ')
            userchoice = int(input())
            if userchoice == 1:
                PC.attack(othercharater)
                othercharater.attack(PC)
            if userchoice == 2:
                pass
            if userchoice == 3:
                print("Terminating your experience")
        if PC.alive():
            print("You have slain {}.".format(othercharater.name))
            return True
        else:
            print("You have been slain!")
            return False        


spiderman = Hero(100, 6, "Spiderman the Great")
goblinman = Goblin(20, 5, "Goblinman the Foul")
zombieman = Zombie(0, 7, "Zombieman the Invincible")
effinghealer = Medic(30, 6, "Leeroy Jenkins the NotMedic")
shadman = Shade(1, 6, "Sylvannas the Tormented")
barbyman = Barbarian(42, 0, "Barbarossa the Forsaken")


def main():



    while spiderman.alive() and goblinman.alive():
        print(spiderman.status())
        print(goblinman.status())
        print()
        print("What do you want to do?")
        print("1. fight enemy")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            spiderman.attack(goblinman)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if goblinman.health > 0:
            goblinman.attack(spiderman)

    while spiderman.alive() and effinghealer.alive():
        print(spiderman.status())
        print(effinghealer.status())
        print()
        print("What do you want to do?")
        print("1. fight enemy")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            spiderman.attack(effinghealer)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if effinghealer.health > 0:
            effinghealer.attack(spiderman)

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


# def __init__(self, damage, critDamage, health, power, name):
    #     self.damage = damage
    #     self.critDamage = critDamage
    #     super(Hero, self).__init__(health, power, name)