from charClasses import Warrior

class Sword(Warrior):
  def __init__(self):
    self.durability = 15
    self.damage = 18
    super().__init__()
  def attributes(self):
    self.strength += 20
    print(f"Your strength has increased by 20 points, your strength is now {self.strength}")
    self.defense += 10
    print(f"Your defense has increased by 10 points, your defense is now {self.defense}")
  def attack(self):
    self.damage = 18
    self.durability -= 5
    if sword.durability == 0:
      sword.constitution()
    print(f"Your sword durability is now {self.durability}")
  def constitution(self):
    if self.durability <= 0:
      print("Your sword has broken")

sword = Sword()

sword.attributes()

while sword.durability > 0:
  to_attack = int(input("Select 1 to attack?"))
  if to_attack == 1:
    sword.attack()
  else:
    pass

  
class Shield(Warrior):
  def __init__(self):
    self.durability = 30
    super().__init__()
  def attributes(self):
    self.defense += 20
    print(f"Your defense has increased by 20 and is now {self.defense}")
  def defend(self):
    self.durability -= 5
    print(f"Your shield durability has decreased by 5 and is now {self.durability}")
    if self.durability <= 0:
      print("Your shield has broken")

shield = Shield()

while shield.durability > 0:
  to_defend = int(input("Select 1 to defend youself"))
  if to_defend == 1:
    shield.defend()
  else:
    pass

class Staff(Warrior):
  def __init__(self):
    self.durability = 10
    self.damage = 12
    super().__init__()
  def attributes(self):
    self.strength += 10
    print(f"Your strength has increased by 10 points, your strength is now {self.strength}")
    self.defense += 5
    print(f"Your defense has increased by 5 points, your defense is now {self.defense}")
  def attack(self):
    self.damage = 12
    self.durability -= 5
    if staff.durability == 0:
      staff.constitution()
    print(f"Your staff durability is now {self.durability}")
  def constitution(self):
    if self.durability <= 0:
      print("Your staff has broken")

staff = Staff()

while staff.durability > 0:
  to_attack = int(input("Select 1 to attack"))
  if to_attack == 1:
    staff.attack()
  else:
    pass

# this is a comment