import inflect
p = inflect.engine()

name_list = []
try:
    while True:
            name_list.append(input("Name: "))

except EOFError:
    print()
    print(f"Adieu, adieu, to {p.join(name_list)}")
