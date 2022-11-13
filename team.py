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