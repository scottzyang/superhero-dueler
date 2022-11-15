import random
from hero import Hero

class Team:
  def __init__(self, name):
    self.name = name
    self.heroes = list()

  def remove_hero(self, name):
    found_hero = False
    # loop through each hero in our list
    for hero in self.heroes:
      if hero.name == name:
        self.heroes.remove(hero)
        found_hero = True

    if not found_hero:
      return 0
  
  def add_hero(self, hero):
    self.heroes.append(hero)

  def view_all_heroes(self):
    for hero in self.heroes:
      print(hero.name)

  # update KD stats and print per person
  def stats(self):
    for hero in self.heroes:
      if hero.deaths == 0:
        hero.deaths  = 1
      kd = hero.kills / hero.deaths
      print(f"{hero.name}: Kill/Death ratio = {kd}")

  def revive_heroes(self, health=100):
    for hero in self.heroes:
      hero.current_health = hero.starting_health

  # team battle and update living heroes list
  def attack(self, other_team):
    ''' Battle each team against each other.'''

    living_heroes = list()
    living_opponents = list()

    for hero in self.heroes:
      living_heroes.append(hero)

    for hero in other_team.heroes:
      living_opponents.append(hero)

    while len(living_heroes) > 0 and len(living_opponents) > 0:
      champion1 = random.choice(living_heroes)
      champion2 = random.choice(living_opponents)

      winner = champion1.fight(champion2)
      if winner == champion1:
        living_opponents.remove(champion2)
      elif winner == champion2:
        living_heroes.remove(champion1)
      else: 
        print(f'No winner!')
        return
