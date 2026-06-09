def main():
    expression = input("Enter math expression: ").replace(" ","")

    x, y, z = find_op(expression)
    result = math(x, y, z)
    print(result)

def find_op(expression):
    if "+" in expression:
        return expression.partition("+")
    elif "-" in expression:
        return expression.partition("-")
    elif "*" in expression:
        return expression.partition("*")
    elif "/" in expression:
        return expression.partition("/")


def math(x, y, z):
    x = int(x)
    z = int(z)
    match y:
        case "+":
            return round(float(x + z), 1)
        case "-":
            return round(float(x - z), 1)
        case "*":
            return round(float(x * z), 1)
        case "/":
            return round(float(x / z), 1)


main()

