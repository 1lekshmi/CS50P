import inflect
p = inflect.engine()

def main():
    adieu()

def adieu():
    names = []
    while True:
        try:
            name = input("Name: ")
            name = name.title()
            names.append(name)
            joined = p.join(names)
        except EOFError:
            print("Adieu, adieu, to", joined)
            break

main()
