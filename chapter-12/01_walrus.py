# Using walrus operator
if (n := len([1,2,3,4,5])) > 3:
  print(f"List is too long ({n} elements, expected <= 3)") #output: list is to long (5 elements, expected < = 3)