def main():
    price = 50
    while price > 0:
        print("Amount Due:", price)
        coin = int(input("Insert Coin:"))
        if coin == 25 or coin == 10 or coin == 5:
            price = price - coin

    if price == 0:
        print("Change Owed:", 0)
    else:
        print("Change Owed:", -(price))

main()
