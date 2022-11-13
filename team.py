import random
from hero import Hero

class Team:
  def __init__(self, name):
    self.name = name
    self.heroes = list()

  def remove_hero(self, name):
    foundHero = False
    # loop through each hero in our list
    for hero in self.heroes:
      if hero.name == name:
        self.heroes.remove(hero)
        foundHero = True

    if not foundHero:
      return 0
  
  def add_hero(self, hero):
    self.heroes.append(hero)

  def view_all_heroes(self):
    for hero in self.heroes:
      print(hero.name)

  def stats(self):
    for hero in self.heroes:
      kd = hero.kills / hero.deaths
      print(f"{hero.name} Kill/Deaths:{kd}")

  def revive_heroes(self, health=100):
    for hero in self.heroes:
      hero.current_health = hero.starting_health

  def attack(self, other_team):
    ''' Battle each team against each other.'''

    living_heroes = list()
    living_opponents = list()

    for hero in self.heroes:
      living_heroes.append(hero)

    for hero in other_team.heroes:
      living_opponents.append(hero)

    while len(living_heroes) > 0 and len(living_opponents)> 0:
      # TODO: Complete the following steps:
      # 1) Randomly select a living hero from each team (hint: look up what random.choice does)
      # 2) have the heroes fight each other (Hint: Use the fight method in the Hero class.)
      # 3) update the list of living_heroes and living_opponents
      # to reflect the result of the fight
      champion1 = random.choice(living_heroes)
      champion2 = random.choice(living_opponents)

      winner = champion1.fight(champion2)
      if winner.name == champion1.name:
        living_opponents.remove(champion2)
      elif winner.name == champion2.name:
        living_heroes.remove(champion1)
      else: 
        print(f'No winner!')
