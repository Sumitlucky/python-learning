class Employee:
  a = 1
  @classmethod  #classs method format to read clss attribute
#self meaning -> oject par method chal raha hai
  def show(cls): #cls -> abject will be work in object

    print(f"The class attribute of a is {cls.a}")

e = Employee()

e.a =  45

e.show()