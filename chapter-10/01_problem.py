# question -> create a class ""programmer" for storing information of few programmers working at microsoft


class Programmer:
  company = "Microsoft"
  def __init__(self,name,salary, pin):
    self.name = name
    self.salary = salary
    self.pin = pin
p = Programmer("sumit ", 12000000, 232334)    

print(p.name , p.salary,p.pin,p.company)