def main():
    greetings = input("Greeting: ")
    print(f"${value(greetings)}")

def value(greeting):
    greeting = greeting.lower().replace(",", " ")
    greeting = greeting.split()
    if greeting[0] == "hello":
        return 0
    elif greeting[0][0] == "h" and greeting[0] != "hello":
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
