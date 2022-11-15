from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team
from colorama import Fore, Back, Style

class Arena:
  def __init__(self):
    self.team_one = Team('Red Team')
    self.team_two = Team('Blue Team')

  def create_ability(self):
    name = input("What is the ability name?  ")
    max_damage = int(input(
      "What is the max damage of the ability?  "))

    return Ability(name, max_damage)

  def create_weapon(self):
    weapon_name = input("What is the weapon name? ")
    max_damage = int(input("What is the max damage of the weapon? "))

    return Weapon(weapon_name, max_damage)

  def create_armor(self):
    armor_name = input("What is the armor name? ")
    max_block = int(input("What is the max block of the armor? "))

    return Armor(armor_name, max_block)

  def create_hero(self):
    '''Prompt user for Hero information
      return Hero with values from user input.
    '''
    hero_name = input("Hero's name: ")
    hero = Hero(hero_name)
    add_item = None
    while add_item != "4":
      add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
      if add_item == "1":
        new_ability = self.create_ability()
        hero.add_ability(new_ability)
      elif add_item == "2":
        new_weapon = self.create_weapon()
        hero.add_weapon(new_weapon)
      elif add_item == "3":
        new_armor = self.create_armor()
        hero.add_armor(new_armor)
    return hero

    # build_team_one is provided to you
  def build_team_one(self):
    num_team_members = int(input("How many members would you like on Team One?\n"))
    for i in range(num_team_members):
      hero = self.create_hero()
      self.team_one.add_hero(hero)

  # Now implement build_team_two
  #HINT: If you get stuck, look at how build_team_one is implemented
  def build_team_two(self):
    num_team_members = int(input("How many members would you like on Team Two?\n"))
    for i in range(num_team_members):
      hero = self.create_hero()
      self.team_two.add_hero(hero)
  
  def team_battle(self):
    self.team_one.attack(self.team_two)

  def show_stats(self):
    print("\n")
    print(Fore.RED + self.team_one.name + " statistics: ")
    self.team_one.stats()
    print("\n")
    print(Fore.BLUE + self.team_two.name + " statistics: ")
    self.team_two.stats()
    print(Style.RESET_ALL + "\n")

    # This is how to calculate the average K/D for Team One
    team_kills = 0
    team_deaths = 0
    survivors = list()
    for hero in self.team_one.heroes:
        team_kills += hero.kills
        team_deaths += hero.deaths
        if hero.is_alive():
          survivors.append(hero.name)
    if team_deaths == 0:
        team_deaths = 1
    print(self.team_one.name + " average K/D was: " + str(team_kills/team_deaths))

    team_kills = 0
    team_deaths = 0
    survivors = list()
    for hero in self.team_two.heroes:
      team_kills += hero.kills
      team_deaths += hero.deaths
      if hero.is_alive():
        survivors.append(hero.name)
    if team_deaths == 0:
      team_deaths = 1
    print(self.team_two.name + " average K/D was: " + str(team_kills/team_deaths) + "\n")

    for hero in self.team_one.heroes:
      if hero.deaths == 0:
          print("Survived from " + self.team_one.name + ": " + hero.name)

    for hero in self.team_two.heroes:
      if hero.deaths == 0:
          print("Survived from " + self.team_two.name + ": " + hero.name)


if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()