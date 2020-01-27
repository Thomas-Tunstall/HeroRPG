
import random
from time import sleep

global displayStatus 
displayStatus = False #This is the variable to enable the scouter


class Character:
    def __init__(self, health, power, name, coins, armor):
        self.health = health
        self.power = power
        self.name = name
        self.coins = coins
        self.armor = armor

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
            self.coins += othercharater.coins
            print(f"You loot through the body of {othercharater.name} and scavange up {othercharater.coins} coins from their dead corpse")
    
    def alive(self):
        while self.health > 0:
            return True
        else:
            sleep(2)
            print("You have beeen slain!")
            return False

    def crit(self): ###Crit Bug Is somewhere around here###
        self.critDamage = 1
        critChance = random.randint(1, 5)
        if critChance == 2:
            print(f'{self.name} has landed a critical blow against!')
            self.critDamage = 2
            return self.critDamage
        else:
            self.critDamage = 1
            return self.critDamage

    def buy(self, item):
        if self.coins >= item.cost:
            self.coins -= item.cost
            item.apply(self)
        else:
            print("You don't have enough coins to purchase this item!")

class Goblin(Character):
    pass

class Zombie(Character):
    def __init__(self, power, health, name, coins, armor):
        super(Zombie, self).__init__(power, health, name, coins, armor)
    
    def alive(self):
        return True
    

class Medic(Character):
    def __init__(self, power, health, name, coins, armor):
        super(Medic, self).__init__(power, health, name, coins, armor)

    def heal(self):
        healChance = random.randint(1, 5)
        if healChance == 5:
            self.health += 2
            print('Blessed by RNGsus, the Medic has healed itself by 2!')

class Shade(Character):
    def __init__(self, power, health, name, coins, armor):
        super(Shade, self).__init__(power, health, name, coins, armor)

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
    def __init__(self, power, health, name, coins, armor):
        super(Barbarian, self).__init__(power, health, name, coins, armor)

    def attack(self, othercharater):
        self.power = random.randint(9, 22)
        othercharater.health -= self.power
        print("{} do {} damage to the {}.".format(self.name, self.power, othercharater.name))
        if othercharater.health <= 0:
            print("{} has been slain!".format(othercharater.name))

class TheBridgekeeper(Character):
    pass
    

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
        print("No longer forced to use their fists {self.name} swings a long, sharp sword!")
        sleep(1)
        print("You will deal significantly more damage now!")

class SSJ:
    def __init__(self):
        self.cost = 30
        self.name = "SuperSayin"
    def apply(self, character):
        character.power *= 3.5
        print("Your character lets out a primal roar, their hair pulsates and turns into golden. You are far more powerful now")

class Scouter: #Not Functioning Yet
    def __init__(self):
        self.cost = 3
        self.name = "Scouter-Glass"
    def apply(self, character): #Enabling the scouter doesn't work
        global displayStatus
        displayStatus = True
        print("Your character can now view the power and health of themselves and your foe")

class Store:
    tonic = SuperTonic()
    armor = Armor()
    longsword = Longsword()
    supersayin = SSJ()
    scouter = Scouter()
    items = [tonic, armor, longsword, supersayin, scouter]
    def do_shopping(self, PC):
        sleep(1)
        print("You walk forward, a small hut stands before you\n")
        sleep(2)
        print("A small hermit pokes his head out and speaks to you\n")
        sleep(2)
        print("Greetings Noble Spiderman! I have wares, if you have coin!\n")
        sleep(2)
        while True:    
            print("What do you want to do?")
            print("You have {} coins.".format(PC.coins))
            for i in range(len(self.items)):
                item = self.items[i]
                print("{}. buy {} ({})".format(i + 1, item.name, item.cost))
            print("0. leave")
            raw_imp = int(input("> "))
            if raw_imp == 0:
                break
            else:
                ItemToBuy = Store.items[raw_imp - 1]
                item = ItemToBuy
                PC.buy(item)
    def go_shopping(self, character):
        print("You see a smoketrail off over the treeline\n")
        sleep(1)
        print("Will you approach it?\n")
        sleep(1)
        print("Press 1 to approach, to remain in the forest press 2")
        store_status = int(input())
        if store_status == 1:
            self.do_shopping(character)

# class Battle:
#     def battle_loop(self, PC, othercharater):
#         print("=====The Battle Begins=====")
#         print("{} takes on {}".format(PC.name, othercharater.name))
#         while PC.alive() and othercharater.alive():
#             print(PC.status())
#             print(othercharater.status())
#             print("======What will you do?=====")
#             print("1. Fight {}".format(othercharater.name))
#             print("2. Stand your ground... and do nothing")
#             print("3. Flee")
#             print("> ", end=' ')
#             userchoice = int(input())
#             if userchoice == 1:
#                 PC.attack(othercharater)
#                 othercharater.attack(PC)
#             if userchoice == 2:
#                 pass
#             if userchoice == 3:
#                 print("Terminating your experience")
#         if PC.alive():
#             print("You have slain {}.".format(othercharater.name))
#             return True
#         else:
#             print("You have been slain!")
#             return False        

spiderman = Hero(100, 12, "Spiderman the Great", 5, 0)
goblinman = Goblin(20, 7, "Goblinman the Foul", 8, 0)
zombieman = Zombie(30, 7, "Zombieman the Invincible", 1000, 4)
effinghealer = Medic(40, 6, "Leeroy Jenkins the NotMedic", 11, 3)
shademan = Shade(1, 6, "Sylvannas the Tormented", 14, 0)
barbyman = Barbarian(60, 0, "Barbarossa the Forsaken", 22, 2)
bridgeboi = TheBridgekeeper(1000000, 9001, "The Legendary Bridgekeeper of Kazadum", 9000, 9000)
store = Store()

def main():
    print("You stand alone, in the middle of a lightly dense forest of pine trees\n")
    sleep(1)
    print("A tree in front of you rustles and a small goblin bursts into the clearling\n")
    sleep(1)
    print("{} appraoches you".format(goblinman.name))
    if displayStatus == True:
        print(spiderman.status())
        print(goblinman.status())
        sleep(1)
    else:
        pass
    while spiderman.alive() and goblinman.alive():
        print("What do you want to do?")
        print("1. Fight {}".format(goblinman.name))
        print("2. Do Nothing")
        print("3. Flee from {}".format(goblinman.name))
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1": 
            spiderman.attack(goblinman)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("You flee from {}.".format(goblinman.name))
            sleep(1)
            print("Wow, seriously? You fled from the first enemy you encountered?")
            sleep(1)
            break
        else:
            print("Invalid input {}".format(raw_input))

        if goblinman.health > 0:
            goblinman.attack(spiderman)


    store.go_shopping(spiderman)

    print("...before you {} appraoches...".format(zombieman.name))
    sleep(1)
    print("You sense that this is a foe that you cannot defeat by conventional means")
    if displayStatus == True:
        print(spiderman.status())
        print(goblinman.status())
        sleep(1)
    else:
        pass
    sleep(1)
    while spiderman.alive() and zombieman.alive():    
        print("What do you want to do?")
        print("1. Fight {}".format(zombieman.name))
        print("2. Do nothing")
        print("3. Flee from {}".format(zombieman.name))
        print("4. Inspect {} more closely".format(zombieman.name))
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            spiderman.attack(zombieman)
        elif raw_input == "2":
            pass
            print("{} stares blankly at you, but opts not to attack".format(zombieman.name))
        elif raw_input == "3":
            print("You flee from {}.".format(zombieman.name))
            break
        elif raw_input == "4":
            sleep(1)
            print("You inspect the rooting corpse of {}\n".format(zombieman.name))
            sleep(1)
            print("Upon its corpse you see a strange glyph\n")
            sleep(1)
            print("You can't get a good look at it as {}\n".format(zombieman.name))
            sleep(1)
            print("continues to lunge around and amble aimlessly\n")
            sleep(1)
            print("Perhaps if you knocked it down, you could get a better look at it?\n")
            sleep(1)
            print("Will you attempt to grapple {} to the ground?\n".format(zombieman.name))
            print("1. = Yes or 2 = No")
            raw_input = input()
            if raw_input == "1":
                grap_check = random.randint(1,5)
                if grap_check >= 3:
                    sleep(1)
                    print("Success! You knock {} to the ground".format(zombieman.name))
                    sleep(1)
                    print("You get a better look at the glyph- it bears the markings of a phoenix\n")
                    sleep(1)
                    print("This could be valuable information, but you're not yet sure why\n")
                    sleep(1)
                    print("You decide there is no reason to linger around this foul thing anymore")
                    spiderman.coins += zombieman.coins
                    print("But not before relieving {} of his {} coins before he can get back to his feet".format(zombieman.name, zombieman.coins))
                    break
                elif grap_check < 3:
                    sleep(1)
                    print("Failure! {} overpowers you and swipes at you".format(zombieman.name))
            elif raw_input == "2":
                break        


        else:
            print("Invalid input {}".format(raw_input))

            # zombieman.health >= 0:      
        if zombieman.health > 0:
            zombieman.attack(spiderman)

    store.go_shopping(spiderman)

    print("A man cladded in an oversized robe approaches you\n")
    sleep(1)
    print("My name is {}, and I have no quarrel with you\n")
    sleep(1)
    print("That said, I will defend myself should you attack me\n")
    if displayStatus == True:
        print(spiderman.status())
        print(effinghealer.status())
        sleep(1)
    else:
        pass
    sleep(0.1)
    while spiderman.alive() and effinghealer.alive():
        print("What do you want to do?")
        print("1. Fight {}".format(effinghealer.name))
        print("2. Do Nothing")
        print("3. Flee from {}".format(effinghealer.name))
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            spiderman.attack(effinghealer)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("You flee from {}.".format(effinghealer.name))
            break
        else:
            print("Invalid input {}".format(raw_input))

        if effinghealer.health > 0:
            effinghealer.attack(spiderman)
            effinghealer.heal()

    store.go_shopping(spiderman)

    print("Out of the treeline, a ghastly shade approaches")
    sleep(1)
    print("The shade is as black as the night sky")
    sleep(1)
    print("You can feel the warmth in your face drain away- this is a foul creature")
    sleep(1)
    if displayStatus == True:
        print(spiderman.status())
        print(shademan.status())
        sleep(1)
    else:
        pass
    sleep(1)
    while spiderman.alive() and shademan.alive():    
        print("What do you want to do?")
        print("1. fight enemy")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            dodgeChance = random.randint(1, 10)
            if dodgeChance == 10:
                spiderman.health -= shademan.power
                spiderman.attack(shademan)
            else: print("{} swung and {} nimbly dodged the strike!".format(shademan.name, spiderman.name))

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

    print("Intro text here")
    while spiderman.alive() and barbyman.alive():
        if displayStatus == True:
            print(spiderman.status())
            print(goblinman.status())
            sleep(1)
    else:
        pass
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
            sleep(1)
            print("As you turn to flee {} catches you with his axe and slams you into the ground.".format(barbyman.name))
            barbyman.attack(spiderman)
            sleep(1)
            print("You cannot flee from this foe!")
            
        else:
            print("Invalid input {}".format(raw_input))

        if barbyman.health > 0:
            barbyman.attack(spiderman)    

    store.go_shopping(spiderman)

    while spiderman.alive() and bridgeboi.alive():
            print(spiderman.status())
            print(bridgeboi.status())
            print()
            print("What do you want to do?")
            print("1. fight enemy")
            print("2. do nothing")
            print("3. flee")
            print("> ", end=' ')
            raw_input = input()
            if raw_input == "1":
                print("You intend to fight me? You stand no chance against my power, however I will give you a chance to live if you can answer my riddles\n")
                sleep(1)
                print("If you will fight press 1, if you will test your wits press 2, press anything else and you will be deleted\n")
                raw_input = input()
                if raw_input == "2":
                    sleep(1)
                    print("The bridgekeeper cackles\n")
                    sleep(1)
                    print("I see you are not as dumb as you look, very well\n")
                    sleep(1)
                    print("Question 1! Who was the first enemy you fought?\n")
                    sleep(1)
                    print("1. Goblinman the Foul")
                    print("2. Gobliman the Wretched")
                    print("3. Goblianman the Complacent")
                    raw_input = input()
                    if raw_input == "1":
                        sleep(1)
                        print("You are correct, next question...\n")
                        sleep(1)
                        print("Question 2! What glpyh did {} bear?\n".format(zombieman.name))
                        print("1. A deer")
                        print("2. A phoenix")
                        print("3. A snake")
                        raw_input = input()
                        if raw_input == "2":
                            sleep(1)
                            print("You are correct, final question...1")
                        else:
                            print("WRONG!")
                            bridgeboi.attack(spiderman)
                    else:
                        print("WRONG!")
                        bridgeboi.attack(spiderman) 
                else:
                    bridgeboi.attack(spiderman)    

            elif raw_input == "2":
                pass
            elif raw_input == "3":
                print("Goodbye.")
                break
            else:
                print("Invalid input {}".format(raw_input))

            if bridgeboi.health > 0:
                bridgeboi.attack(spiderman)    

main()
