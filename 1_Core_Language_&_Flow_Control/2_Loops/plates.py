def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Rule 1: Length
    if not (2 <= len(s) <= 6):
        return False

    # Rule 2: First two characters must be letters
    if not (s[0:2].isalpha()):
        return False

    # Rule 3 & 4: Digits must be at the end, and no leading zero
    for index, char in enumerate(s):
        if char.isdigit():
            digits = s[index:]
            if digits[0] == '0':
                return False
            if not digits.isdigit():
                return False
            break  # digits found, no need to check rest

    # Rule 5: No punctuation or special characters
    if not s.isalnum():
        return False

    return True

main()
