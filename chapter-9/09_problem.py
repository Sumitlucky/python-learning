with open ("file.txt") as f:
  content1 = f.read()
with open("poem.txt") as f:
  content2 = f.read()  

if( content1 == content2):
  print("print yes these files are identicals")  
else:
  print("No these files are not identicals")  