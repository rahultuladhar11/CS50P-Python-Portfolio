import re
import sys

def main():
    try:
        print(convert(input("Hours: ")))
    except ValueError:
        sys.exit("ValueError")

def convert(s):
    time12 = re.search(r"^(\d{1,2}(?::\d{2})?) (AM|PM) to (\d{1,2}(?::\d{2})?) (AM|PM)$", s)
    if time12:
        time1 = check(time12.group(1), time12.group(2))
        time2 = check(time12.group(3), time12.group(4))

        return (f"{time1} to {time2}")
    else:
        raise ValueError

def check(time, meridien):
    if ":" in time:
        hr, min = map(int, time.split(":"))
        if 0 <= hr <= 12 and 0 <= min <= 59:
            if meridien == "AM":
                if hr == 12:
                    hr = 0
            else:
                if hr != 12:
                    hr += 12

            return f"{hr:02}:{min:02}"

        else:
            raise ValueError
    else:
        time = int(time)
        if 0 <= time <= 12:
            if meridien == "AM":
                if time == 12:
                    time = 00

            else:
                if time != 12:
                    time += 12

            return f"{time:02}:00"

        else:
            raise ValueError

if __name__ == "__main__":
    main()
