
import random 
from time import sleep
import hero_rpgART

#Ideas for next version
#Add evade function
#Add a shield with a parry function on a random chance roll

global displayStatus 
displayStatus = False #This is the variable to enable the scouter

global VCFlag1 #These are the Final Boss Question flags
VCFlag1 = False
global VCFlag2
VCFlag2 = False
global VCFlag3
VCFlag3 = False


class Character:
    def __init__(self, health, power, name, coins, armor):
        self.health = health
        self.power = power
        self.name = name
        self.coins = coins
        self.armor = armor

    def attack(self, othercharacter): #module
        othercharacter.health -= self.power
        print("{} do {} damage to the {}.".format(self.name, self.power, othercharacter.name))
        if othercharacter.health <= 0:
            print("{} has been slain!".format(othercharacter.name))

    def alive(self):
        while self.health > 0:
            return True
        else:
            return False

    def status(self):
        print("{} has {} health and {} power.".format(self.name, self.health, self.power))

    def setHealth(self, health):
        self.health = health 

    def getHealth(self):
        return self.health

class Hero(Character):
    def __init__(self, power, health, name, coins, armor):
        super().__init__(power, health, name, coins, armor)

    def attack(self, othercharacter):
        self.damage = self.power * self.crit() - othercharacter.armor
        othercharacter.setHealth(othercharacter.getHealth() - self.damage)
        print(f"{self.name} has dealt {self.damage} to {othercharacter.name}")
        if othercharacter.health <= 0:
            print(f"{othercharacter.name} has been slain!")
            self.coins += othercharacter.coins
            print(f"You loot through the body of {othercharacter.name} and scavange up {othercharacter.coins} coins from their dead corpse")
    
    def alive(self):
        while self.health > 0:
            return True
        else:
            sleep(2)
            print("You have beeen slain!")
            exit()
            return False

    def crit(self):
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
        super().__init__(power, health, name, coins, armor)
    
    def alive(self):
        return True

    def setHealth(self, health):
        return


class Medic(Character):
    def __init__(self, power, health, name, coins, armor):
        super().__init__(power, health, name, coins, armor)

    def heal(self):
        healChance = random.randint(1, 5)
        if healChance == 5:
            self.health += 8
            print('Blessed by RNGsus, the Medic has healed itself by 8!\n')

class Shade(Character):
    def __init__(self, power, health, name, coins, armor):
        super().__init__(power, health, name, coins, armor)

class Barbarian(Character):
    def __init__(self, power, health, name, coins, armor):
        super().__init__(power, health, name, coins, armor)

    def attack(self, othercharacter):
        self.power = random.randint(12, 31)
        othercharacter.health -= self.power
        print("{} do {} damage to the {}.".format(self.name, self.power, othercharacter.name))
        if othercharacter.health <= 0:
            print("{} has been slain!".format(othercharacter.name))

class TheBridgekeeper(Character):
    pass
    

class SuperTonic:
    def __init__(self):
        self.cost = 10
        self.name = "Tonic of Restoration"
    def apply(self, character):
        character.health += 25
        print("Your health has increased by 25!\n")

class Armor:
    def __init__(self):
        self.cost = 10
        self.name = "Plate Armor"
    def apply(self, character):
        character.armor += 4
        print("Your character's armor has increased by 4!\n")

class Longsword:
    def __init__(self):
        self.cost = 40
        self.name = "Longsword of Dathmire"
    def apply(self, character):
        character.power += 15
        print("This sword looks like it can do some serious damage!\n")
        sleep(1)
        print("You will deal significantly more damage now!\n")

class SSJ:
    def __init__(self):
        self.cost = 125
        self.name = "SSJ"
    def apply(self, character):
        character.power *= 3
        print("Your character lets out a primal roar, their hair pulsates and turns into golden.\n")
        sleep(1)
        print("Something has awoken inside of you. You are FAR more powerful now\n")

class Scouter:
    def __init__(self):
        self.cost = 5
        self.name = "Scouter-Glass"
    def apply(self, character):
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
        print("A small hermit pokes his head\n")
        sleep(2)
        print("Greetings {}! I have wares, if you have coin!\n".format(spiderman.name))
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
        hero_rpgART.smokestack()
        print("1. Approach")
        print("2. Remain in the forest")
        store_status = int(input())
        if store_status == 1:
            self.do_shopping(character)     

# Obj name = Class(HP, Power, Name, Money, Armor)
spiderman = Hero(100, 12, "Spiderman the Great", 10, 0)
goblinman = Goblin(30, 9, "Goblinman the Foul", 15, 0)
zombieman = Zombie(50, 7, "Zombieman the Invincible", 25, 4)
effinghealer = Medic(100, 13, "Leeroy Jenkins the Anti-Medic", 35, 3)
shademan = Shade(1, 18, "Sylvannas the Tormented", 50, 0)
barbyman = Barbarian(150, 0, "Barbarossa the Forsaken", 75, 2)
bridgeboi = TheBridgekeeper(500, 75, "The Legendary Bridgekeeper of Kazadum", 9000, 5)
store = Store()

def main():
    print("You wake up, hanging upside down, you are the {}\n".format(spiderman.name))
    hero_rpgART.spidermanART()
    sleep(5)
    print("With a crack, the tree branch that you were hanging to snaps and you plummet to the ground\n")
    sleep(1)
    print("You stand alone, in the middle of a lightly dense forest of pine trees\n")
    sleep(1)
    print("You have no idea where you are, but you feel like you need to get out of this place as soon as you can\n")
    sleep(1)
    print("A tree in front of you rustles and a small goblin bursts into the clearling\n")
    sleep(1)
    print("{} appraoches you\n".format(goblinman.name))
    sleep(2)
    hero_rpgART.goblinArt()
    while spiderman.alive() and goblinman.alive():
        print("What do you want to do?")
        print("1. Fight {}".format(goblinman.name))
        print("2. Do Nothing")
        print("3. Flee from {}".format(goblinman.name))
        print("4. Speak with {}.".format(goblinman.name))
        if displayStatus == True:
            print("5. Initialize scouter")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1": 
            spiderman.attack(goblinman)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("You flee from {}.\n".format(goblinman.name))
            sleep(1)
            print("Wow, seriously? You fled from the pipsqeuak {}?\n".format(goblinman.name))
            sleep(1)
            break
        elif raw_input == "4":
            print("You move closer to {} and attempt to speak with it\n".format(goblinman.name))
            sleep(1)
            moneyStolen = random.randint(1,5)
            spiderman.coins -= moneyStolen
            moneyStolen += goblinman.coins
            print("As you attempt to communicate, {} leaps at you and steals {} pieces of your gold!\n".format(goblinman.name, moneyStolen))
            sleep(1)
            print("As this happens, you notice a red skull with a blue sickle on the back of {}\n".format(goblinman.name))
            sleep(1)
            print("You feel like this is important, but you are not sure why\n")
            global VCFlag1
            VCFlag1 = True
        elif raw_input == "5":
            if displayStatus == True:
                print(spiderman.status())
                print(goblinman.status())
                sleep(1)
        else:
            print("Invalid input {}".format(raw_input))

        if goblinman.health > 0:
            goblinman.attack(spiderman)


    store.go_shopping(spiderman)

    print("From beyond the trees you heard a loud and gutteral groan\n")
    sleep(1)
    print("{} appraoches\n".format(zombieman.name))
    sleep(1)
    print("You sense that this is a foe that you cannot defeat by conventional means\n")
    sleep(2)
    hero_rpgART.zombieArt()
    while spiderman.alive() and zombieman.alive():    
        print("What do you want to do?")
        print("1. Fight {}".format(zombieman.name))
        print("2. Do nothing")
        print("3. Flee from {}".format(zombieman.name))
        print("4. Inspect {} more closely".format(zombieman.name))
        if displayStatus == True:
            print("5. Initialize scouter")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            spiderman.attack(zombieman)
        elif raw_input == "2":
            pass
            print("{} stares blankly at you, but opts not to attack\n".format(zombieman.name))
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
            print("1. Yes")
            print("2. No")
            raw_input = input()
            if raw_input == "1":
                grap_check = random.randint(1,5)
                if grap_check >= 3:
                    sleep(1)
                    print("Success! You knock {} to the ground\n".format(zombieman.name))
                    sleep(1)
                    print("You get a better look at the glyph- it bears the markings of a phoenix\n")
                    sleep(1)
                    print("This could be valuable information, but you're not yet sure why\n")
                    sleep(1)
                    global VCFlag2
                    VCFlag2 = True
                    print("You decide there is no reason to linger around this foul thing anymore\n")
                    spiderman.coins += zombieman.coins
                    print("But not before relieving {} of his {} coins before he can get back to his feet\n".format(zombieman.name, zombieman.coins))
                    break
                elif grap_check < 3:
                    sleep(1)
                    print("Failure! {} overpowers you and swipes at you\n".format(zombieman.name))
            elif raw_input == "2":
                break        
        elif raw_input == "5":
            if displayStatus == True:
                print(spiderman.status())
                print(zombieman.status())
                sleep(1)

        else:
            print("Invalid input {}".format(raw_input))
     
        if zombieman.health > 0:
            zombieman.attack(spiderman)

    store.go_shopping(spiderman)

    print("A man cladded in white, flowing robes approaches you\n")
    sleep(1)
    print("My name is {}, and I have no quarrel with you\n".format(effinghealer.name))
    sleep(1)
    print("That said, I will defend myself should you attack me\n")
    hero_rpgART.medicArt()
    while spiderman.alive() and effinghealer.alive():
        print("What do you want to do?")
        print("1. Fight {}".format(effinghealer.name))
        print("2. Do Nothing")
        print("3. Flee from {}".format(effinghealer.name))
        print("4. Speak with {}".format(effinghealer.name))
        if displayStatus == True:
            print("5. Initialize scouter")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            spiderman.attack(effinghealer)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("You flee from {}.".format(effinghealer.name))
            break
        elif raw_input == "4":
            print("You speak with {}".format(effinghealer.name))
            sleep(1)
            print("He tells you that he can dramatically increase your stamina\n")
            sleep(1)
            print("It would cost every gold piece you have\n")
            sleep(1)
            print("Do you want to proceed?\n")
            print("1. Yes {}! Make me far more impervious to damage.\n".format(effinghealer.name))
            print("2. No {}, I would prefer to keep my money.\n".format(effinghealer.name))
            raw_input = input()
            if raw_input == "1":
                spiderman.health = 300
                spiderman.coins = 0
                sleep(2)
                print("{} raises his hands and radiates a golden energy which floats from him to you\n".format(effinghealer.name))
                sleep(1)
                print("You feel your body brimming with power, you feel much stronger now\n")
                sleep(1)
                print("You hand {} all of your money, thank him and then turn away\n".format(effinghealer.name))
                break
            else:
                pass

        elif raw_input == "5":
            if displayStatus == True:
                print(spiderman.status())
                print(effinghealer.status())
                sleep(1)

        else:
            print("Invalid input {}".format(raw_input))

        if effinghealer.health > 0:
            effinghealer.attack(spiderman)
            effinghealer.heal()

    store.go_shopping(spiderman)

    print("Out of the treeline, a ghastly shade approaches\n")
    sleep(1)
    print("The shade is as black as the night sky\n")
    sleep(1)
    print("You can feel the warmth in your face drain away- this is a foul creature\n")
    sleep(1)
    print("You can hear it faintly whispering something, but you cannot quite make out what...\n")
    sleep(1)
    hero_rpgART.shadeArt()
    while spiderman.alive() and shademan.alive():    
        print("What do you want to do?")
        print("1. Fight {}".format(shademan.name))
        print("2. Do nothing")
        print("3. Flee from {}".format(shademan.name))
        print("4. Listen to {}".format(shademan.name))
        if displayStatus == True:
            print("5. Initialize scouter")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            dodgeChance = random.randint(1, 10)
            if dodgeChance == 10:
                spiderman.health -= shademan.power
                spiderman.attack(shademan)
            else: print("{} swung and {} nimbly dodged the strike!\n".format(shademan.name, spiderman.name))

        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("You flee from {}.".format(shademan.name))
            break
        elif raw_input == "4":
            print("You move right next to {}".format(shademan.name))
            sleep(1)
            print("You make out half of a word\n")
            sleep(1)
            print("Silve-\n")
            sleep(3)
            print("As you make out the first half of the phrase, the shade attacks you\n")
            sleep(1)
            shademan.attack(spiderman)
            print(spiderman.status())
            print("Will you attempt to hear the rest of what the shade was saying?\n")
            print("1. Yes")
            print("2. No")
            raw_input = input()
            if raw_input == "1":
                sleep(1)
                print("You stand your ground and listen to the {}'s wail\n".format(shademan.name))
                sleep(1)
                print("-rmoon\n")
                sleep(3)
                print("You connect the two phrases in your mind 'Silvermoon'\n")
                global VCFlag3
                VCFlag3 = True
                sleep(2)
                print("The shade attacks again\n")
                shademan.attack(spiderman)
                print("You leap back out of range of the shade\n")
            else:
                pass
        elif raw_input == "5":
            if displayStatus == True:
                print(spiderman.status())
                print(shademan.status())
                sleep(1)
        
        else:
            print("Invalid input {}".format(raw_input))
        
        if shademan.health > 0:
            shademan.attack(spiderman)

    store.go_shopping(spiderman)

    print("A loud roar pierces through the quiet night sky\n")
    sleep(1)
    print("A hulking barbarian emerges through the treeline\n")
    sleep(1)
    print("Across his back is an axe almost as large as you\n")
    sleep(1)
    print("{} roars at you\n".format(barbyman.name))
    sleep(1)
    print("THIS IS MY FOREST, YOU WILL NOT DISTUB MY HOME\n")
    sleep(1)
    print("He charges toward you with fury burning in his eyes\n")
    sleep(1)
    hero_rpgART.barbarianArt()
    while spiderman.alive() and barbyman.alive():
        print("What do you want to do?")
        print("1. Fight {}".format(barbyman.name))
        print("2. Do nothing")
        print("3. Flee from {}".format(barbyman.name))
        print("4. Speak with {}".format(barbyman.name))
        if displayStatus == True:
            print("5. Initialize scouter")
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
        elif raw_input == "4":
            sleep(1)
            print("You attempt to speak to {}".format(barbyman.name))
            sleep(1)
            print("{} is not one to be reasoned with")
            barbyman.attack(spiderman)

        elif raw_input == "5":
            if displayStatus == True:
                print(spiderman.status())
                print(barbyman.status())
                sleep(1)    
        else:
            print("Invalid input {}".format(raw_input))

        if barbyman.health > 0:
            barbyman.attack(spiderman)    

    store.go_shopping(spiderman)

    print("Ahead, you see a clearing in the trees\n")
    sleep(1)
    print("A massive canyon looms before you\n")
    sleep(1)
    print("Spanning the chasm, is a fifty foot long bridge, stone pillars reaching down into the chasm below\n")
    sleep(3)
    hero_rpgART.bridgeArt()
    sleep(3)
    print("As you approach, you see an old man standing at the front of the bridge\n")
    sleep(1)
    print("The man is covered in a red and black robe, his eyes glitter an emerald green\n")
    sleep(1)
    print("Across his back is an enormous sword set on dragonteeth\n")
    sleep(1)
    print("This does not seem like someone who you should cross\n")
    sleep(1)
    print("Will you approach the man on the bridge?\n")
    print("1. = Approach")
    print("2. = Turn back")
    raw_input =  input()
    if raw_input == "1":
        pass
    else:
        return


    while spiderman.alive() and bridgeboi.alive():
            print("What do you want to do?")
            print("1. Fight {}".format(bridgeboi.name))
            print("2. Do nothing")
            print("3. Flee from {}".format(bridgeboi.name))
            if displayStatus == True:
                print("4: Initialize Scouter")
            print("> ", end=' ')
            raw_input = input()
            if raw_input == "1":
                hero_rpgART.bossArt()
                print("You intend to fight me? I'm warning you, you stand no chane against me\n")
                sleep(1)
                print("I will give you the chance to test your wits instead of your might\n")
                sleep(1)
                print("So which will it be? Might or Wits?\n")
                sleep(0.5)
                print("Press 1 for Might")
                print("Press 2 for Wits")
                raw_input = input()
                if raw_input == "2":
                    sleep(1)
                    print("The bridgekeeper cackles\n")
                    sleep(1)
                    print("I see you are not as dumb as you look, very well\n")
                    sleep(1)
                    print("Question 1! What emblem did {} bear?\n".format(goblinman.name))
                    sleep(1)
                    print("1. Red Skull with a Blue Sickle")
                    print("2. Black Cross with a Red Sword")
                    print("3. White Shield with a Purple Lance")
                    raw_input = input()
                    if raw_input == "1":
                        sleep(1)
                        print("You are correct, next question...\n")
                        sleep(1)
                        print("Question 2! What glpyh did {} bear?\n".format(zombieman.name))
                        print("1. A Deer")
                        print("2. A Phoenix")
                        print("3. A Snake")
                        raw_input = input()
                        if raw_input == "2":
                            sleep(1)
                            print("You are correct, final question...\n")
                            sleep(1)
                            print("Where is the homeland of {}?\n".format(shademan.name))
                            sleep(2)
                            print("1. Silvermoon")
                            print("2. Quel'Thalas")
                            print("3. Stormwind")
                            raw_input = input()
                            if raw_input == "1":
                                print("Once again you are correct!\n")
                                if (VCFlag1 == True) and (VCFlag2 == True) and (VCFlag3 == True):
                                    sleep(2)
                                    print("You have answered all my questions correctly, you may pass on\n")
                                    sleep(1)
                                    print("{} motions you across\n".format(bridgeboi.name))
                                    break
                                else:
                                    print("However, you simply got lucky and guessed\n")
                                    sleep(1)
                                    print("There is no way that you figured all three of those out on your own!\n")
                                    sleep(1)
                                    print("And for your insolence, you will perish")
                                    bridgeboi.attack(spiderman)
                            else:
                                print("WRONG!")
                                bridgeboi.attack(spiderman)

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
                print("You've come too far, there's no turning back now.\n")
                sleep(1)
                pass
            elif raw_input == "4":
                if displayStatus == True:
                    print(spiderman.status())
                    print("You tap your scouter, but you cannot get a tactical readout on {}\n".format(bridgeboi.name))
                    sleep(1)
            else:
                print("Invalid input {}".format(raw_input))

            if bridgeboi.health > 0:
                bridgeboi.attack(spiderman)

            if bridgeboi.health <= 0:
                print("Despite the odds, you managed to slay {}".format(bridgeboi.name))
                sleep(2)    

    print("You emerge on the other side of the bridge\n")
    sleep(2)
    print("You have overcome every obstacle that you faced, and emerged triumphant!")
    sleep(2)
    print("YOU ARE VICTORIOUS\n")
    sleep(5)
hero_rpgART.victoryART()

main()