import random
from ability import Ability

class Weapon(Ability):
  def attack(self):
    total_damage = random.randint((int(self.max_damage) // 2), int(self.max_damage))
    return total_damage

