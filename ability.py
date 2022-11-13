import random

class Ability:
  def __init__(self, name, max_damage):
    self.name = name
    self.max_damage = max_damage

  def attack(self):
    total_damage = random.randint(0, int(self.max_damage))
    return total_damage


if __name__ == "__main__":
  ability = Ability("Debugging Ability", 20)
  print(ability.name)
  print(ability.attack())