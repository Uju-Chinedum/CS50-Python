user = input("Enter a string: ")
final = ""

for letter in user:
    if letter.lower() in "aeiou":
        continue
    else:
        final += letter

print(final)