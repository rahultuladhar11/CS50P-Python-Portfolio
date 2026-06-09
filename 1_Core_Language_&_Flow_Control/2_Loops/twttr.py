string = input("Input: ")

new_string = ""

for char in string:
    if char not in "aeiouAEIOU":
        new_string += char

print("Output:", new_string)
