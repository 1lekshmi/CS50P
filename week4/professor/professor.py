import random

def main():
    level = get_level()
    i = 0
    score = 0
    fails = 0
    while i != 10:
        x,y = generate_integer(level)
        ques = f"{x} + {y} = "
        ans = int(input(ques))
        i += 1
        if ans == x + y:
            score += 1
            fails = 0
        else:
            print("EEE")
            fails += 1
            while fails < 3:
                ans = int(input(ques))
                if ans != x + y:
                    print("EEE")
                    fails += 1
                else:
                    score += 1
                    fails = 0
            print(ques + str(x + y))


    print(f"Score: {score}")


def get_level():
    while True:
        try:
            n = int(input("Level: "))
        except ValueError:
            continue
        else:
            if n == 1 or n == 2 or n == 3:
                return n
            else:
                continue

def generate_integer(level):
    if level == 1:
        a = random.randint(0,9)
        b = random.randint(0,9)
    elif level == 2:
        a = random.randint(10,99)
        b = random.randint(10,99)
    elif level == 3:
        a = random.randint(100,999)
        b = random.randint(100,999)
    else:
        raise(ValueError)
    return a,b


if __name__ == "__main__":
    main()
    