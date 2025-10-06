import os

def generateTable(n):
    # Create folder if it doesn't exist
    os.makedirs("tables", exist_ok=True)

    table = ""
    for i in range(1, 11):
        table += f"{n} X {i} = {n*i}\n"

    with open(f"tables/table_{n}.txt", "w") as f:
        f.write(table)

for i in range(2, 21):
    generateTable(i)
