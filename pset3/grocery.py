import sys

def main():
    stuffs = collate()
    grocery = tally(stuffs)
    display(grocery)


def collate():
    items = []
    while True:
        try:
            entry = input().upper()
            items.append(entry)
        except (KeyboardInterrupt, EOFError):
            items = sorted(items)
            return items
            sys.exit()


def tally(list_iterable):
    goods = {}
    for item in list_iterable:
        goods[item] = goods.get(item, 0)
        goods[item] += 1
    return goods


def display(dict_iterable):
    for k, v in dict_iterable.items():
        print(f"{v} {k}")


main()