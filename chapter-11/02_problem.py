class Animals:
  pass

class Pets(Animals):
  pass

class Dog(Pets):
  @staticmethod 
  def bark():
    print("BOW BOW!")
 
D = Dog()
D.bark()