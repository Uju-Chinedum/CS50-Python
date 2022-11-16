def convert(user):
    output = user.replace(":)", "🙂")
    output = output.replace(":(", "🙁")

    return output

def main():
    user = input("Enter a string: ")
    print(convert(user))

main()