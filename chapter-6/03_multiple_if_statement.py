a = int(input("Enter your age: ")) 


if(a%2==0):
  print("a is even:")
if(a%2!=0):
  print("a is odd: ")


if(a>18):
  print("you are above the age of consent: ",a)
elif(a<0):
  print("are you entering an invalid age: ")  
    
else:
  print("you are below the age of consent")  



print("End of the program")  