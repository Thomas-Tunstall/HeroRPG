#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

import random
import time

class Character:
    def __init__(self, health, power, name, coins):
        self.health = health
        self.power = power
        self.name = name
        self.coins = coins
        self.armor = 0

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
        self.damage = self.power * self.crit() - othercharater.armor
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

    def buy(self, item):
        self.coins -= item.cost
        item.apply(self)

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
        else:
            if othercharater.health <= 0:
                print("{} has been slain!".format(othercharater.name))
            othercharater.power = 0
            print("{} swung and {} nimbly dodged the strike!".format(othercharater.name, self.name))

class Barbarian(Character):
    def attack(self, othercharater):
        self.power = random.randint(5, 13)
        othercharater.health -= self.power
        print("{} do {} damage to the {}.".format(self.name, self.power, othercharater.name))
        if othercharater.health <= 0:
            print("{} has been slain!".format(othercharater.name))

class SuperTonic:
    def __init__(self):
        self.cost = 3
        self.name = "tonic"
    def apply(self, character):
        character.health += 10
        print("Your health has increased by 10!")

class Armor:
    def __init__(self):
        self.cost = 7
        self.name = "armor"
    def apply(self, character):
        character.armor += 2
        print("Your character's armor has increased by 2!")

class Longsword:
    def __init__(self):
        self.cost = 13
        self.name = "Longsword"
    def apply(self, character):
        character.power += 5
        print("Your character's power has increased by 5!")

class SSJ:
    def __init__(self):
        self.cost = 30
        self.name = "SuperSayin"
    def apply(self, character):
        character.power *= 1.75
        print("Your character lets out a primal roar, their hair pulsates and turns into golden. You are far more powerful now")

class Store:
    tonic = SuperTonic()
    armor = Armor()
    longsword = Longsword()
    supersayin = SSJ()
    items = [tonic, armor, longsword, supersayin]
    def do_shopping(self, PC):
        while True:
            print("=====================")
            print("Welcome to the store!")
            print("=====================")
            print("You have {} coins.".format(PC.coins))
            print("What do you want to do?")
            for i in range(len(self.items)):
                item = self.items[i]
                print("{}. buy {} ({})".format(i + 1, item.name, item.cost))
            print("10. leave")
            raw_imp = int(input("> "))
            if raw_imp == 10:
                break
            else:
                ItemToBuy = Store.items[raw_imp - 1]
                item = ItemToBuy
                PC.buy(item)
    def go_shopping(self, character):
        store_status = int(input("""1. Enter the store. 
    Press another number to battle."""))
        if store_status == 1:
            self.do_shopping(character)

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

spiderman = Hero(100, 6, "Spiderman the Great", 5)
goblinman = Goblin(20, 5, "Goblinman the Foul", 3)
zombieman = Zombie(0, 7, "Zombieman the Invincible", 1000)
effinghealer = Medic(30, 6, "Leeroy Jenkins the NotMedic", 11)
shademan = Shade(1, 6, "Sylvannas the Tormented", 14)
barbyman = Barbarian(42, 0, "Barbarossa the Forsaken", 22)
store = Store()


def main():
    while spiderman.alive() and goblinman.alive():
        print(spiderman.status())
        print(goblinman.status())
        print("...before you {} appraoches...".format(goblinman.name))
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


    store.go_shopping(spiderman)


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

    store.go_shopping(spiderman)

    while spiderman.alive() and shademan.alive():
        print(spiderman.status())
        print(shademan.status())
        print()
        print("What do you want to do?")
        print("1. fight enemy")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            spiderman.attack(shademan)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if shademan.health > 0:
            shademan.attack(spiderman)

    store.go_shopping(spiderman)

    while spiderman.alive() and barbyman.alive():
        print(spiderman.status())
        print(barbyman.status())
        print()
        print("What do you want to do?")
        print("1. fight enemy")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            spiderman.attack(barbyman)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if barbyman.health > 0:
            barbyman.attack(spiderman)    

    store.go_shopping(spiderman)


main()
