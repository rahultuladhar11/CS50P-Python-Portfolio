def main():
    greet = input("Enter greeting: ")
    print(f"${value(greet)}")


def value(greeting):
    greeting = greeting[:5].lower().strip()
    
    if greeting == "hello":
        return 0
    elif greeting[0] == "h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
