# Build out Warrior, Mage, Knight, and Warlock classes
# 100 hp, 50 strength, 50 defense, 50 magic
# Hello Joe-
# Make a dungeon and make a new enemy inside the dungeon, make a new function called dungeon (after the initial function) make a character class called dragon and give him stats, 
# put the dragon inside the dungeon
class Warrior:
    def __init__(self):
        self.hp = 100
        self.strength = 50
        self.defense = 50
        self.magic = 50

    def takeDamage(self):
        self.hp += -10 

    def takeCriticalDamage(self):
        self.hp += -25

# class Mage:
#     def __init__(self):
#         self.hp = 100
#         self.strength = 50
#         self.defense = 50
#         self.magic = 50

#     def takeDamage(self):
#         self.hp += -10 

#     def takeCriticalDamage(self):
#         self.hp += -25
    
# class Knight:
#     def __init__(self):
#         self.hp = 100
#         self.strength = 50
#         self.defense = 50
#         self.magic = 50

#     def takeDamage(self):
#         self.hp += -10 

#     def takeCriticalDamage(self):
#         self.hp += -25

# class Warlock:
#     def __init__(self):
#         self.hp = 100
#         self.strength = 50
#         self.defense = 50
#         self.magic = 50
    
#     def takeDamage(self):
#         self.hp += -10 

#     def takeCriticalDamage(self):
#         self.hp += -25
        

class Dragon:
    def __init__(self):
        self.fire = 1000
        self.abilities = 100
        self.hp = 10000
        self.magic = 1000

    def takeDamage(self):
        self.hp += -10 
        print(f"""You dealt 10 damage to the dragon.
                 The Dragons health is now {self.hp}.""")

    def takeCriticalDamage(self):
        self.hp += -25
        print(f"""You dealt 25 damage to the dragon.
                 The Dragons health is now {self.hp}.""")

# def startGame():
#     print("Welcome to my game!")

#     char1 = Warrior()
#     char2 = Mage()

#     while char1.hp > 0 or char2.hp > 0:
#         userInput = int(input("Would you like to be a Warrior (Type 1) or a Mage (Type 2)."))

#         if userInput == 1:
#             print("You're a Warrior!")

#         elif userInput == 2:
#             print("You're a Mage!")    
        
#         else:
#             print("That's not an option.")
#             exit(0)

# startGame()



def dungeon():
    char1 = Warrior()
    enemy = Dragon()
    print("""Welcome to the Dungeon!!
             Be wary.
             You've made it this far, 
             but be careful, danger 
             lurks around every corner!""")
    choice = int(input("Please press (1) to enter the Dungeon.")) 
    if choice == 1:
        print("Welcome to the Dragon's Lair, prepare to fight the Dragon.")
    elif choice != 1:
        print("That's the wrong choice, please press 1.")
    while choice != 1:
        choice = int(input("Please press (1) to enter the Dungeon."))
        if choice == 1:
            print("Welcome to the Dragon's Lair, prepare to fight the Dragon.")
            if choice2 == 1:
                enemy.takeDamage()
            if choice2 == 2:
                    print("You defend against the dragons attack.")
        else:
            print("That's the wrong choice, please press 1.")
    choice2 = int(input("Press (1) to attack the Dragon, press (2) to defend."))
    if choice2 == 1:
        enemy.takeDamage()
        if choice2 == 2:
                print("You defend against the dragons attack.")
    

        
        

dungeon()
    

    # enemy1 = Dragon()
    
     
 
    

# def underWaterLevel():
#         print("""You are now underwater...
#              How does it feel?""")


# dungeon()  




