fruits = {"apple": 130, "avocado": 50, "banana": 110, "cantaloupe": 50, "grapefruit": 60, "grapes": 90,
"honeydew melon": 50, "kiwifruit": 90, "lemon": 15, "lime": 20, "nectarin": 60, "orange": 80, "peach": 60,
"pear": 100, "pineapple": 50, "plum": 70, "strawberries": 50, "sweet cherries": 100, "tangerine": 50, "watermelon": 80}

fruit = input("Enter fruit: ").lower()
try:
    print(f"Calories: {fruits[fruit]}")
except KeyError:
    print("")