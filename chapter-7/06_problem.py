# factorial

n = int (input("Enter  tha number: "))
product = 1
for i in range(1,n+1):
  product = product * i 

  print(f"The factorial of {n} is {product}")