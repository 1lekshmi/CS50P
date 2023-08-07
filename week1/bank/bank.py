def main():
    greeting = input ("Greeting: ")
    greeting = greeting.lower().replace(","," ")
    greeting = greeting.split()
    greetingeval(greeting)

def greetingeval(n):
    if n[0] == "hello":
        print ("$0")
    elif n[0][0] == "h" and n[0] != "hello":
        print ("$20")
    else:
        print ("$100")

main()
