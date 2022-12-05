import random


def main():
    difficulty = get_level()
    tries = 2
    score = 0

    for _ in range(10):
        x, y = generate_integer(difficulty)
        answer = int(input(f"{x} + {y} = "))

        while answer != x + y:
            if tries > 0:
                tries -= 1
                print("EEE")
                answer = int(input(f"{x} + {y} = "))
            else:
                print(x + y)
                break
        else:
            score += 1

    print(f"Score: {score}")



def get_level():
    while True:
        try:
            n = int(input("Enter level: "))
            if n > 3 or n < 1:
                pass
            else:
                return n
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        start = 0
        stop = 9
    elif level == 2:
        start = 10
        stop = 99
    elif level == 3:
        start = 100
        stop = 999

    pos_1 = random.randint(start, stop)
    pos_2 = random.randint(start, stop)

    return pos_1, pos_2

if __name__ == "__main__":
    main()