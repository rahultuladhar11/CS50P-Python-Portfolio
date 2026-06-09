def main():
    time = input("What time is it? ")
    formatted_time = convert(time)
    meal = which_meal(formatted_time)
    if meal:
        print(meal)

def convert(time):
    time = time.lower().strip()

    is_pm = "p.m." in time
    is_am = "a.m." in time

    time = time.replace("p.m.", "").replace("a.m.", "").strip()

    hr,_,min = time.partition(":")
    hr = int(hr)
    min = int(min)/60

    if is_pm and hr != 12:
        hr += 12
    elif is_am and hr == 12:
        hr = 0

    return round((hr + min), 2)

def which_meal(meal_time):
    if 7 <= meal_time <= 8:
        return "breakfast time"
    elif 12 <= meal_time <= 13:
        return "lunch time"
    elif 18 <= meal_time <= 19:
        return "dinner time"

if __name__ == "__main__":
    main()
