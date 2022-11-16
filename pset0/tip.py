def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    amount = float(d[1:])
    return amount


def percent_to_float(p):
    rate = float(p[0:len(p) - 1]) / 100
    return rate


main()