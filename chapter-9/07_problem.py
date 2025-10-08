with open("log.html", "r") as f:
    lines = f.readlines()

lineno = 1
found = False  # to track if we found 'python'

for line in lines:
    if "python" in line:
        print(f"Yes, python is present. Line no: {lineno}")
        found = True
        break
    lineno += 1

if not found:
    print("No, python is not present")
