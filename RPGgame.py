# Character classes

class Hero:
    def __init__(self, strength, defense, hp):
        self.strength = strength
        self.defense = defense
        self.hp = hp


class Knight:
    def __init__(self, strength, defense, hp):
        self.strength = strength
        self.defense = defense
        self.hp = hp


class Mage:
    def __init__(self, strength, defense, hp):
        self.strength = strength
        self.defense = defense
        self.hp = hp

    inventory = []        
    def add_to_inventory():



class PotionShop(Mage):

    def new_potion():
        print("Select Potion. ((1) Hp, (2)Strength ")
        new_potion = ""
    if user_choice == 1:
        print("You have selected Hp!")
    elif user_choice == 2:
        print("You have selected Strength!")




# Define New Character function
def newcharacter():
    entry1 = input("What is your name?")
    entry3 = input("Please select one of the following. ((1) Hero, (2) Knight, (3) Mage)")

    userInput = entry3

    if userInput == "1":
        character = Hero(10, 10, 50)
        print("You have selected to be a Hero")
    elif userInput == "2":
        character = Hero(10, 10, 50)
        print("You have selected to be a Knight")
    elif userInput == "3":
        character = Hero(10, 10, 50)
        print("You have selected to be a Mage")
    else:
        pass

newcharacter()

# Characters

# Zach = Hero("Zach", 10, 10, 50)
# Carlo = Knight("Carlo")
# Randi = Hero("Randi")
# Tatien = Mage("Tatien")
# LeRon = Knight("LeRon")