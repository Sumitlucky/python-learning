'''
factorial(1) = 1
factorail(2) = 2 x 2
factorail(3) = 3 x 2 x 1
factorail(n) =  n * factorail(n-1)

'''

def factorail(n):

  if(n==1 or n ==0):
    return 1
  return  n*factorail(n-1)

n = int(input("Enter a number: "))

print(f"The factorail of this number is: {factorail(n)}")