def main():
    exp = input ("Expression: ")
    calc(exp)

def calc(e):
    x, y, z = e.split(" ")
    if y == "/":
        if z == "0":
            print("Error, z cannot be 0.")
        else:
            n = int (x) / int(z)
            print (round(float(n), 1))
    if y == "+":
        n = int(x) + int(z)
        print (round(float(n), 1))
    if y == "-":
        n = int(x) - int(z)
        print (round(float(n), 1))
    if y == "*":
        n = int(x) * int(z)
        print (round(float(n), 1))


main()
