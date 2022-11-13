class Animal:
  def __init__(self, name):
    self.name = name
  
  def eat(self):
    print(f'{self.name} eats!')

  def drink(self):
    print(f'{self.name} drank!')


class Frog(Animal):
  def jump(self):
    print(f'{self.name} is jumping!')


animal = Animal('Scott')
frog = Frog('Tama')
frog.eat()
frog.drink()
frog.jump()