while True:
    try:
        prompt = input('Fractions: ').split('/')
        x = prompt[0]
        y = prompt.pop()
        z = (int(x) / int(y) * 100)

        if '.' in x or y == '0' or int(x) > int(y):
            pass
        else:
            if z < 1:
                print("E")
            elif z > 99:
                print ("F")
            else:
                print(str(round(z)) + '%')
            break
    except ValueError:
        pass
    except ZeroDivisionError:
        pass
