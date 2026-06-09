import sys
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif sys.argv[1][-4:] != ".csv":
    sys.exit("Not a CSV file")

table = []
i=0

try:
    with open (sys.argv[1]) as file:
        for line in file:
            if i == 0:
                headers = line.rstrip().split(",")
            else:
                row = line.rstrip().split(",")
                table.append(row)

            i += 1

    print(tabulate(table, headers, tablefmt="grid"))

except FileNotFoundError:
    sys.exit("File does not exist")
