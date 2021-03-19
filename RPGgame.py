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

      

class Potion_type:
    def __init__(self, red, blue, green):
        self.red = red
        self.blue = blue
        self.green = green

      
inventory = []

class PotionShop():
    # def __init__(self):
        # self.name = ""
     

    def add_to_inventory(self):


        inventory_list = int(input("Please make selction (1)Red Potion, (2)Blue Potion, (3)Green Potion, (4)Exit Shop > "))

        if inventory_list == 1:
            print("You have selected Red Potion!")
            inventory.append("Red Potion")
            return print(f"Your current inventory is now {inventory}")

        elif inventory_list == 2:
            print("You have selected Blue Potion!")
            inventory.append("Blue Potion")
            return print(f"Your current inventory is now {inventory}")

        elif inventory_list == 3:
            print("You have selected Green Potion!")
            inventory.append("Green Potion")
            return print(f"Your current inventory is now {inventory}")
        
        elif inventory_list == 4:
      
            return print("You have chose to Exit Shop")
        else:
            print("Invalid choice, please select again or input exit to exit shop.")
    

# print(add_to_inventory)

potion = PotionShop()
potion.add_to_inventory()

   

# Characters

# Zach = Hero("Zach", 10, 10, 50)
# Carlo = Knight("Carlo")
# Randi = Hero("Randi")
# Tatien = Mage("Tatien")
# LeRon = Knight("LeRon")