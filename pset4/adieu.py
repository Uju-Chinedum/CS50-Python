import inflect

engine = inflect.engine()
names = []

while True:
    try:
        user = input()
        names.append(user)
    except (EOFError, KeyboardInterrupt):
        # print()
        break

if len(names) == 1:
    name = names[0]
else:
    name = engine.join(names)

adieu = f"Adieu, adieu, to {name}"
print(adieu)