greet = input("Enter greeting: ").lower().strip()

hello = greet[:5]

if hello == "hello":
    print("$0")
elif hello[0] == "h":
    print("$20")
else:
    print("$100")
