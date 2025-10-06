import random, os

def game():
    print("You are playing the game..")
    score = random.randint(1, 75)

    file_path = os.path.join(os.path.dirname(__file__), "hiscore.txt")

    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.write("0")

    with open(file_path) as f:
        hiscore = f.read()
        hiscore = int(hiscore) if hiscore else 0

    print(f"Your score: {score}")

    if score > hiscore:
        print("You broke the high score!")
        with open(file_path, "w") as f:
            f.write(str(score))

    return score

game()
