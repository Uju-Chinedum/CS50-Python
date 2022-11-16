amount = 50
change = 0

while amount > 0:
    print(f"Amount Due: {amount}")
    user = int(input("Insert Coin: "))

    if user == 25 or user == 10 or user == 5:
        change = user - amount
        amount -= user
    else:
        continue

print(change)