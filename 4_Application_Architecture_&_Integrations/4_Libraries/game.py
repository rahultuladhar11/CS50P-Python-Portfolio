import random

while True:

    try:
        level = int(input("Level: "))
        if level >= 1:
            break

    except ValueError:
        continue
    except TypeError:
        continue

answer = random.randint(1, level)

while True:

    try:
        guess = int(input("Guess: "))
        if  1 <= guess:
            if guess < answer:
                print("Too small!")
            elif guess > answer:
                print("Too large!")
            else:
                print("Just right!")
                break

    except ValueError:
        continue
    except TypeError:
        continue
