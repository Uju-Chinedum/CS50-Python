import random

while True:
    try:
        n = int(input("Enter level: "))
        if n < 0:
            pass

        number = random.randint(1, n)

        while True:
            guess = int(input("Enter guess: "))
            if guess < 0:
                pass
            elif guess < number:
                print("Too small!")
                pass
            elif guess > number:
                print("Too large!")
                pass
            else:
                print("Just right!")
                break
        break

    except ValueError:
        pass