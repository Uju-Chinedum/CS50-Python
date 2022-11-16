word = input("Enter camelCase: ")
snake = word[0]

for letter in word[1:]:
    if letter.isupper():
        snake += "_"
        snake += letter.lower()
    else:
        snake += letter

print(snake)