def main():
    while True:
        try:
            fraction = input("Fraction: ").replace(" ","")
            percentage = operation(fraction)
            while percentage > 100 or percentage < 0:
                fraction = input("Fraction ").replace(" ","")
                percentage = operation(fraction)
            if percentage <= 1:
                print("E")
                break
            elif percentage >= 99:
                print("F")
                break
            else:
                print(f"{percentage}%")
                break

        except ValueError:
            pass
        except ZeroDivisionError:
            pass


def operation(fraction):
    x, _, y = fraction.partition("/")
    percentage = int(round((int(x)/int(y)*100), 0))
    return percentage

main()
