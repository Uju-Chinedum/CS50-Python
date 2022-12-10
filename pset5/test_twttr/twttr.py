def main():
    user = input("Enter a string: ")
    print(shorten(user))


def shorten(word):
    final = ""

    for letter in word:
        if letter.lower() in "aeiou":
            continue
        else:
            final += letter

    return final


if __name__ == "__main__":
    main()