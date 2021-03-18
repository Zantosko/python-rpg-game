class Goblin:
  def __init__(self, health, damage, strength, defense):
    self.health = health
    self.damage = damage
    self.strength = strength
    self.defense = defense
  def printFunc(self):
    print(f"Your health level is: {self.health}")
    print(f"Your damage level is: {self.damage}")
    print(f"Your strength level is: {self.strength}")
    print(f"Your defense level is: {self.defense}")
    

first_goblin = Goblin(15, 8, 10, 6)
first_goblin.printFunc()


class Weapons:
  def __init__(self, durability, damage):
    self.durability = durability 
    self.damage = damage
  def sword(self):
    print(f"Your sword deals a damage of {self.damage}")
    print(f"Your sword has a durability rating of {self.durability}")

sword_specs = Weapons(10, 8)
sword_specs.sword()
