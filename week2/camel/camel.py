def main():
    variable_name = input("camelCase: ")
    convert(variable_name)

def convert(name):
    letters = [name[0].lower()]
    for n in name[1:]:
        if n.isupper() == True:
            letters.append("_")
            letters.append(n.lower())
        else:
            letters.append(n)
    print("snake_case: " + "".join(letters))

main()