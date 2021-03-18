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


