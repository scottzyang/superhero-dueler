import random
from ability import Ability

class Weapon(Ability):
  def attack(self):
    total_damage = random.randint(self.max_damage // 2, self.max_damage)
    return total_damage

