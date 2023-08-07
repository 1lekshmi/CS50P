months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Date: ")

        if "/" in date:
            x, y, z = date.split("/")
            if x.title() in months:
                pass
        elif "," in date:
            date = date.replace(",","")
            x, y, z = date.split(" ")

        if x.title() in months and "/" not in date:
            x = months.index(x.title()) + 1
            x = int(x)
        else:
            x = int(x)
        y = int(y)
        z = int(z)

        if 0 < x <= 12 and 0 < y <= 31:
            print(f"{z}-{x:02}-{y:02}")
            break
    except ValueError:
        pass
    except EOFError:
        break

