class Employee:
  language = "pyrhon" # This is a class attribute
  salary = 340000



  def getInfo(self):
    print(f"The language is {self.language}. The salary  {self.salary}")

  @staticmethod
  def greet():
    print("Good Morning")
sumit  = Employee()

sumit.language = "c++"
sumit.getInfo()




