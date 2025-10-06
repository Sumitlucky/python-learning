f = open("poem.txt")

content = f.read()

if("ka hal chal ba" in content):
  print("The statement will be present in the content")
else:
  print("The statement will br not present in the content")
f.close()    