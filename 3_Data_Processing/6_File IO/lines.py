import sys
from PyPi

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif sys.argv[1][-3:] != ".py":
    sys.exit("Not a Python file")

try:
    with open (sys.argv[1]) as file:
        i = 0
        for line in file:
            line = line.strip()
            if line.startswith("#") or line == "":
                continue
            else:
                i += 1

        print(i)

except FileNotFoundError:
    sys.exit("File does not exist")
