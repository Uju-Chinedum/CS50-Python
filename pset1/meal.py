def main():
    user = input("Enter time: ")
    check = convert(user)

    if check >= 7 and check <= 8:
        print("breakfast time")
    elif check >= 12 and check <= 13:
        print("lunch time")
    elif check >= 18 and check <= 19:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")

    hours = int(hours)
    minutes = int(minutes)
    minutes /= 60

    return hours + minutes

if __name__ == "__main__":
    main()