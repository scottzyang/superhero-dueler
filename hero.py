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
    self.abilities = list()
    self.armors = list()


  def fight(self, opponent):
    if self.abilities or opponent.abilities:
      # run while both opponents are alive
      while self.is_alive() and opponent.is_alive():
        # initialize attack values for hero and opponent
        hero_attack = self.attack()
        opponent_attack = opponent.attack()
        
        # pass attack return value as damage to hero and opponent
        opponent.take_damage(hero_attack)
        self.take_damage(opponent_attack)

        # conditions to run if one has died
        if self.is_alive() and not opponent.is_alive():
          print(f'{self.name} wins the battle!')
        elif not self.is_alive() and opponent.is_alive():
          print(f'{opponent.name} wins the battle!')
        elif not self.is_alive() and not opponent.is_alive(): 
          print(f'In a hard fought battle both {self.name} and {opponent.name} have lost!')
    else: 
      print(f'{self.name} and {opponent.name} could not defeat each other. It is a draw!')

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

  def add_weapon(self, weapon):
    self.abilities.append(weapon)

  def take_damage(self, damage):
    self.current_health -=  self.defend(damage)
  
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