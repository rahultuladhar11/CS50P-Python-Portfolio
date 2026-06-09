
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    date = input("Date: ").strip()


    if "/" in date:
        x = date.split("/")
        if len(x) == 3:
            mm, dd, yyyy = x
            if mm.isdigit() and dd.isdigit() and yyyy.isdigit():
                mm = int(mm)
                dd = int(dd)
                yyyy = int(yyyy)
                if 1 <= mm <= 12 and 1 <= dd <= 31:

                    print(f"{yyyy:04}-{mm:02}-{dd:02}")
                    break


    elif "," in date:
        try:
            mm_dd, yyyy = date.split(",")
            yyyy = yyyy.strip()
            mm, dd = mm_dd.strip().split(" ")
            dd = dd.strip()
            if mm in months and dd.isdigit() and yyyy.isdigit():
                mm = months.index(mm) + 1
                dd = int(dd)
                yyyy = int(yyyy)
                if 1 <= dd <= 31:
                    print(f"{yyyy:04}-{mm:02}-{dd:02}")
                    break
        except:
            pass
