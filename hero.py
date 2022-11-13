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

  def defend(self):
    total_defense = 0
    if self.current_health == 0 or not self.armors:
      total_defense = 0
    else:
      for armor in self.armors:
        total_defense += armor.block()
    
    return total_defense
      


# this block only runs if the script if called directly
# allows us to test this logic infile, but won't run if imported to another file
if __name__ == "__main__":
  # my_hero = Hero("Grace Hopper", 600)
  # print(my_hero.name)
  # print(my_hero.current_health)
  
  # my_hero2 = Hero("Margaret Hamilton", 10)

  # my_hero.fight(my_hero2)

  ability = Ability("Great Debugging", 50)
  another_ability = Ability("Smarty Pants", 90)
  hero = Hero("Grace Hopper", 200)
  hero.add_ability(ability)
  hero.add_ability(another_ability)
  # print(hero.attack())

  armor = Armor("Firewall", 60)
  another_armor = Armor("Ad Blocker", 150)
  hero.add_armor(armor)
  hero.add_armor(another_armor)
  print(hero.defend())