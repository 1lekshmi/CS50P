grocery_list = {}

while True:
    try:
        items = input("")
        grocery_list[items] = grocery_list.get(items, 0) + 1
    except EOFError:
        for items in sorted(grocery_list):
            print(grocery_list[items], items.upper())
        break
    except KeyError:
        pass