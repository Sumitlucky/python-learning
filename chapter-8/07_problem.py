#
def rem(l,word):

  for item in l:
    n = []
    if not(item == word):
      n.append(item.strip(word))
  return n  

l = ["sumit","rohit","rohan","komal","anjali","ritika"]

print(rem(l,"r"))