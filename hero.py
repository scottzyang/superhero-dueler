# hero.py
import random

class Hero:
  def __init__(self, name, starting_health=100):
    self.name = name
    self.starting_health = starting_health
    self.current_health = starting_health

  def fight(self, opponent):
    self.fighters = [self.name, opponent.name]
    # establish probability of winning based on health
    total_health = self.current_health + opponent.current_health
    hero1_probability = 100 * (self.current_health / total_health)
    hero2_probability = 100 * (opponent.current_health / total_health)

    # randomly select winner based on weighted probabilty
    winner = random.choices(self.fighters, weights=(hero1_probability, hero2_probability), k=1)
    print(f'{winner[0]} wins the fight!')

# this block only runs if the script if called directly
# allows us to test this logic infile, but won't run if imported to another file
if __name__ == "__main__":
  my_hero = Hero("Grace Hopper", 600)
  print(my_hero.name)
  print(my_hero.current_health)
  
  my_hero2 = Hero("Margaret Hamilton", 10)

  my_hero.fight(my_hero2)