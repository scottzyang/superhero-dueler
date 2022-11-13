from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team

class Arena:
  def __init__(self):
    self.team_one = Team('Team1')
    self.team_two = Team('Team2')

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
      print(hero.name)
      self.team_one.add_hero(hero)

  # Now implement build_team_two
  #HINT: If you get stuck, look at how build_team_one is implemented
  def build_team_two(self):
    numofTeamMembers = int(input("How many members would you like on Team Two?\n"))
    for i in range(numofTeamMembers):
      hero = self.create_hero()
      self.team_two.add_hero(hero)
  
  def team_battle(self):
    self.team_one.attack(self.team_two)

  def show_stats(self):
    '''Prints team statistics to terminal.'''
    # TODO: This method should print out battle statistics
    # including each team's average kill/death ratio.
    # Required Stats:
    #     Show surviving heroes.
    #     Declare winning team
    #     Show both teams average kill/death ratio.
    # Some help on how to achieve these tasks:
    # TODO: for each team, loop through all of their heroes,
    # and use the is_alive() method to check for alive heroes,
    # printing their names and increasing the count if they're alive.
    #
    # TODO: based off of your count of alive heroes,
    # you can see which team has more alive heroes, and therefore,
    # declare which team is the winning team
    #
    # TODO for each team, calculate the total kills and deaths for each hero,
    # find the average kills and deaths by dividing the totals by the number of heroes.
    # finally, divide the average number of kills by the average number of deaths for each team

    print("\n")
    print(self.team_one.name + " statistics: ")
    self.team_one.stats()
    print("\n")
    print(self.team_two.name + " statistics: ")
    self.team_two.stats()
    print("\n")

    # This is how to calculate the average K/D for Team One
    team_kills = 0
    team_deaths = 0
    for hero in self.team_one.heroes:
        team_kills += hero.kills
        team_deaths += hero.deaths
    if team_deaths == 0:
        team_deaths = 1
    print(self.team_one.name + " average K/D was: " + str(team_kills/team_deaths))


    team2_kills = 0
    team2_deaths = 0
    for hero in self.team_two.heroes:
      team2_kills += hero.kills
      team2_deaths += hero.deaths
    if team2_deaths == 0:
      team2_deaths = 1
    print(self.team_two.name + " average K/D was: " + str(team_kills/team_deaths))

    # Here is a way to list the heroes from Team One that survived
    for hero in self.team_one.heroes:
        if hero.deaths == 0:
            print("survived from " + self.team_one.name + ": " + hero.name)

    #TODO: Now list the heroes from Team Two that survived
    for hero in self.team_two.heroes:
        if hero.deaths == 0:
            print("survived from " + self.team_two.name + ": " + hero.name)


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