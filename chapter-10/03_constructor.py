class Employee:
  language = "pyrhon" # This is a class attribute
  salary = 340000

  def __init__(self, name , salary, language): # dunder method which is automatically called
    self.name = name
    self.salary = salary
    self.language = language
    print("I am creating an object")


  def getInfo(self):
    print(f"The language is {self.language}. The salary  {self.salary}")

  @staticmethod
  def greet():
    print("Good Morning")

sumit = Employee("komal",1200000, "javaScript")    
# sumit  = Employee()
# sumit.name = "komal"
# sumit.language = "c++"
print(sumit.name, sumit.salary, sumit.language)




