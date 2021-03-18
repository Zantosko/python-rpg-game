
class Sword:
  def __init__(self, damage, durability):
    self.damage = damage
    self.durability = durability
    # self.hp += 5

  def short_sword(self):
    self.damage = damage
    self.durability = durability
  def long_sword(self, damage, durability):
    pass
      
class Bow:
  def __init__(self, damage, durability):
    self.damage = damage
    self.durability = durability
  def flamming_arrow(self):
    self.damage += 5
    print(f"{self.damage}")
    self.durability += 5
    print(f"{self.durability}")
    

sword = Sword(21, 19)
print(f"Your short sword damage and durability are {sword.damage} {sword.durability} respectively")

bow = Bow(10, 10)
bow.flamming_arrow()
