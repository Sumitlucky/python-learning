def pattern(n):
  if(n==0):
    return
  print("*"*n)
  pattern(n-1)
pattern(5)

# lets try itself but noit successfull
# def pattern2(n):
#   if(n==0):
#     return
#   print("*"*n,)
#   print(" ", end="")
#   print("*"*(n-1))
#   print(" ", end="")
#   print("*"*(n-2))
#   print(" ", end="")
  

# pattern2(5)