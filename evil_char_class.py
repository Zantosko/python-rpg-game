from charClasses import Warrior

class Sword(Warrior):
  def __init__(self):
    self.durability = 15
    self.damage = 18
    super().__init__()
  def attributes(self):
    self.strength += 20
    print(f"{self.strength}")
    self.defense += 10
    print(f"{self.defense}")
  def attack(self):
    self.damage = 18
    self.durability -= 5
  def constitution(self):
    if self.durability <= 0:
      print("Your sword has broken")

sword = Sword()
print(f"sword durability is {sword.durability}")
print(f"sword damage is {sword.damage}")

sword.attributes()
  
      
# class Bow:
#   def __init__(self, damage, durability):
#     self.damage = damage
#     self.durability = durability
#   def flamming_arrow(self):
#     self.damage += 5
#     print(f"{self.damage}")
#     self.durability += 5
#     print(f"{self.durability}")
    

# sword = Sword(21, 19)
# print(f"Your short sword damage and durability are {sword.damage} {sword.durability} respectively")

# bow = Bow(10, 10)
# bow.flamming_arrow()
