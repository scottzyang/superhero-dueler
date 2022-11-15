# imports
import random
from ability import Ability
from armor import Armor
from weapon import Weapon

class Hero:
  def __init__(self, name, starting_health=100):
    self.name = name
    self.starting_health = starting_health
    self.current_health = starting_health
    # list() is a constructor that returns a list (if empty, returns empty list)
    self.armors = list()
    self.abilities = list()
    self.deaths = 0
    self.kills = 0

  def add_kill(self, num_kills):
    self.kills += num_kills
  
  def add_death(self, num_deaths):
    self.deaths += num_deaths

  def fight(self, opponent):
    if self.abilities or opponent.abilities:
      # run while both opponents are alive
      while self.is_alive() and opponent.is_alive():
        # initialize attack/defend values for hero and opponent
        hero_attack = self.attack()
        hero_defend = self.defend()
        opponent_attack = opponent.attack()
        opponent_defend = opponent.defend()

        # randomize who goes first
        first_attack = random.choice([self, opponent])  

        # FIGHT ----------------------------------------------------------------------------
        # first attack damage based on randomized choice, verify if alive
        status = True
        while status == True:
          if first_attack == opponent:
            self.take_damage(opponent_attack - hero_defend)
            status = self.is_alive()
            if status == True:
              opponent.take_damage(hero_attack - opponent_defend)
              status = opponent.is_alive()
          elif first_attack == self: 
            opponent.take_damage(hero_attack - opponent_defend)
            status = opponent.is_alive()
            if status == True:
              self.take_damage(opponent_attack - hero_defend)
              status = self.is_alive()
        # ----------------------------------------------------------------------------------

        # one has to die for above loop to end, verify which one did below
        if self.is_alive():
          self.add_kill(1)
          opponent.add_death(1)
          print(f'{self.name} used {(random.choice(self.abilities)).name} and it was effective against {opponent.name}! They win!')
          return self
        else:
          opponent.add_kill(1)
          self.add_death(1)
          print(f'{opponent.name} used {(random.choice(opponent.abilities)).name} and it was effective against {self.name}! They win!')
          return opponent
    else: 
      print(f'With no abilities, {self.name} and {opponent.name} could not defeat each other. It is a draw!')
      return

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

  # update current health based on defense and damage
  def defend(self):
    total_defense = 0
    if self.current_health == 0 or not self.armors:
      total_defense = 0
    else:
      for armor in self.armors:
        total_defense += armor.block()

    return total_defense

  def add_weapon(self, weapon):
    self.abilities.append(weapon)

  def take_damage(self, damage):
    # if damage is less than 0, do nothing
    if damage < 0: 
      damage = 0
    else: 
      self.current_health -= damage
  
  def is_alive(self):
    if self.current_health <= 0: 
      return False
    else:
      return True


# this block only runs if the script if called directly
# allows us to test this logic infile, but won't run if imported to another file
if __name__ == "__main__":
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())
    weapon = (random.choice(hero.abilities)).name
    print(weapon)