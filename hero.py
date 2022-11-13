# imports
import random
from ability import Ability
from armor import Armor

class Hero:
  def __init__(self, name, starting_health=100):
    self.name = name
    self.starting_health = starting_health
    self.current_health = starting_health
    # list() is a constructor that returns a list (if empty, returns empty list)
    self.abilities = list()
    self.armors = list()


  def fight(self, opponent):
    self.fighters = [self.name, opponent.name]
    # establish probability of winning based on health
    total_health = self.current_health + opponent.current_health
    hero1_probability = 100 * (self.current_health / total_health)
    hero2_probability = 100 * (opponent.current_health / total_health)

    # randomly select winner based on weighted probabilty
    winner = random.choices(self.fighters, weights=(hero1_probability, hero2_probability), k=1)
    print(f'{winner[0]} wins the fight!')

  def add_ability(self, ability):
    self.abilities.append(ability)

  def attack(self):
    total_damage = 0
    # total the amount of randominzed attack value returned from the attack() method
    for ability in self.abilities:
      total_damage += ability.attack()

    return total_damage

  def add_armor(self, armor):
    self.armors.append(armor)

  def defend(self, damage):
    total_defense = 0
    if self.current_health == 0 or not self.armors:
      total_defense = 0
    else:
      for armor in self.armors:
        total_defense += armor.block()
    
    if damage < total_defense: 
      damage = 0
    else: 
      damage -= total_defense
    
    return damage

  def take_damage(self, damage):
    self.current_health -=  self.defend(damage)


# this block only runs if the script if called directly
# allows us to test this logic infile, but won't run if imported to another file
if __name__ == "__main__":
  hero = Hero("Grace Hopper", 200)
  shield = Armor("Shield", 100)
  hero.add_armor(shield)
  hero.take_damage(150)
  print(hero.current_health)
