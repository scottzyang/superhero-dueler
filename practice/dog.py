class Dog:
  def __init__(self, name, breed):
    self.name = name
    self.breed = breed
    print("dog initialized")

  def bark(self):
    print(f'{self.name} barked, woof!')

  def roll(self):
    print(f'{self.name} rolled over!')

  def sit(self):
    print(f'{self.name} sat!')