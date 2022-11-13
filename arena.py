from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team

class Arena:
  def __init__(self):
    self.team_one = None
    self.team_two = None

  def create_ability(self):
    name = input("What is the ability name?  ")
    max_damage = input(
      "What is the max damage of the ability?  ")

    return Ability(name, max_damage)

  def create_weapon(self):
    weapon_name = input("What is the weapon name? ")
    max_damage = input("What is the max damage of the weapon? ")

    return Weapon(weapon_name, max_damage)

  def create_armor(self):
    armor_name = input("What is the armor name? ")
    max_block = input("What is the max block of the armor? ")

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
    numOfTeamMembers = int(input("How many members would you like on Team One?\n"))
    for i in range(numOfTeamMembers):
      hero = self.create_hero()
      self.team_one.add_hero(hero)

  # Now implement build_team_two
  #HINT: If you get stuck, look at how build_team_one is implemented
  def build_team_two(self):
    numofTeamMembers = int(input("How many members would you like on Team Two?\n"))
    for i in range(numofTeamMembers):
      hero = self.create_hero()
      self.team_two.add_hero(hero)
  