import random
import sys


def main():
    while True:
        n = input("Level: ")
        try:
            n = int(n)
            if n >= 1 :
                guess(n)
            else:
                pass
        except ValueError:
            pass



def guess(n):
    x = random.randint(1, n)
    while True:
        g = input("Guess: ")
        try:
            g = int(g)
            if g < 1:
                pass
            else:
                if g == x:
                    sys.exit("Just right!")
                elif g > x:
                    print("Too large!")
                else:
                    print("Too small!")
        except ValueError:
            pass

main()
