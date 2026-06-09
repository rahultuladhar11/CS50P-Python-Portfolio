import random

def main():
    level = get_level()
    score = 0
    for i in range (10):
        attempts = 1
        x = generate_integer(level)
        y = generate_integer(level)
        answer = input(f"{x} + {y} = ")
        while attempts < 3:
            if answer != str(x+y):
                print("EEE")
                answer = input(f"{x} + {y} = ")
                attempts += 1
            else:
                score += 1
                break
        if attempts > 2:
            print("EEE")
            print(f"{x} + {y} = {x+y}")

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level

        except ValueError:
            continue
        except TypeError:
            continue


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
