months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    user = input("Date: ").strip()
    try:
        if "/" in user and user.split("/")[0].isnumeric():
            m, d, y = user.split("/")
        elif "," in user and user.split(" ")[0].isalpha():
            m = str(months.index(user.split(" ")[0]) + 1)
            d = user.split(" ")[1][0:-1]
            y = user.split(" ")[2]

        if int(m) <= 12 and int(d) <= 31:
            if len(m) < 2 and len(d) < 2:
                print(f"{y}-0{m}-0{d}")
            elif len(m) < 2:
                print(f"{y}-0{m}-{d}")
            elif len(d) < 2:
                print(f"{y}-{m}-0{d}")
            else:
                print(f"{y}-{m}-{d}")
            break
        else:
            pass
    except NameError:
        pass