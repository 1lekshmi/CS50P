def main():
    while True:
        prompt = input("Fractions: ")
        try:
            per = convert(prompt)
            print(gauge(per))
            break
        except (ValueError, ZeroDivisionError):
            pass

def convert(fraction):
    fraction = fraction.split("/")
    x = fraction[0]
    y = fraction.pop()
    if x.isdigit() == False or y.isdigit() == False:
        raise ValueError
    elif "." in x or "." in y or (int(x) > int(y) and int(y) != 0):
        raise ValueError
    if y == "0":
        raise ZeroDivisionError
    z = round((int(x) / int(y)) * 100)
    return z

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()