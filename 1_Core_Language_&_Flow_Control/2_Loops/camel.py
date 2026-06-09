def main():
    camelcase = input("Enter camelcase: ")
    print(snake_case(camelcase))

def snake_case(camelcase):
    snake_case_str = ""
    for char in camelcase:
        if char.isupper():
            if snake_case_str:
                snake_case_str += "_"
        snake_case_str += char.lower()

    return snake_case_str

main()
