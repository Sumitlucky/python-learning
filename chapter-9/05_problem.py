words = ["Donkey","bad","ganda"]

with open("file.txt","r") as f:
  Content = f.read()
for word in words:
  ContentNew = content.replace(word,"#" * len(word))

with open("file.txt","w") as f:
  f.write(ContentNew)