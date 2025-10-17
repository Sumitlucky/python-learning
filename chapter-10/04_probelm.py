class Calculator:
  def __init__(self, n):
    self.n = n 


  def square(self):
    print(f"The square is {self.n*self.n}")


  def cube(self):
    print(f"The cube is {self.n*self.n*self.n}")  

  def squareroot(self):
    print(f"The square is {self.n**1/2}")

  @staticmethod
  def lucky():
    print("hello sumit komal kaisi hai")

a = Calculator (4) 
a.lucky()
a.square()
a.cube()
a.squareroot()