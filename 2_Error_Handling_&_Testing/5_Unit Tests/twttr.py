def main():
    string = input("Input: ")
    print(f"Output: {shorten(string)}")

def shorten(word):
    new_string = ""

    for char in word:
        if char not in "aeiouAEIOU":
            new_string += char

    return new_string

if __name__ == "__main__":
    main()
