def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    one = first_two(s)
    two = size(s)
    three = middle(s)
    four = punct(s)

    return one and two and three and four


def first_two(t):
    if len(t) > 1:
        return t[0].isalpha() and t[1].isalpha()
    else:
        return False



def size(u):
    return len(u) >= 2 and len(u) <= 6


def middle(v):
    if v.isalpha():
        return True
    elif v.isalnum():
        w = [int(i) for i in v if i.isdigit()]
        if w[0] == 0:
            return False
        else:
            return v[-1].isdigit() and v[:len(v) - 2].isalpha()


def punct(x):
    y = ""
    for char in x:
        if char not in " '.,;:?!":
            y += char

    return x == y


main()