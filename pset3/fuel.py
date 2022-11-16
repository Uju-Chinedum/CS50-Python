def main():
    amount = round(convert() * 100)

    if amount >= 99:
        print("F")
    elif amount <= 10:
        print("E")
    else:
        print(f"{amount}%")


def convert():
    while True:
        try:
            x, y = input("Enter fraction: ").split("/")
            x = int(x)
            y = int(y)

            if x <= y:
                return x / y
        except ValueError or ZeroDivisionError:
            pass


main()