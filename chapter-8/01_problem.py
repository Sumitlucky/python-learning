# Gretest of three number
def gretest(a , b , c):
  if(a>b and a>c):
    return a
  elif (b>a and b>c):
    return b
  elif(c>a and c>b):
    return c
  
a = 10
b = 22
c = 7

print(gretest(a,b,c))
