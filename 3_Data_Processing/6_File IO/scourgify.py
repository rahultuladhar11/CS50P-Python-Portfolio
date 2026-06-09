import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].lower().endswith(".csv") or not sys.argv[2].lower().endswith(".csv"):
    sys.exit("Not a CSV file")

students = []

try:
    with open (sys.argv[1]) as file:
        abc = csv.DictReader(file)
        print(abc)
        print()
        for row in abc:
            last, first = row["name"].split(",")
            last = last.strip()
            first = first.strip()
            students.append({"first": first, "last": last, "house": row["house"]})

    with open(sys.argv[2], "w") as file:
        abc = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        abc.writeheader()
        abc.writerows(students)

except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")



'''with open("futonk.csv", "a") as file:
        abc = csv.DictWriter(file, fieldnames=["name", "club", "number"])
        abc.writerow({"name": name, "club": club, "number": number})'''

    #for i in students:
        #print(f"{i["first"]} {i["last"]}, {i["house"]}")


