def main():
    answer = input ("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    evaluate(answer.strip().lower())

def evaluate(n):
    if n == "42" or n == "forty-two" or n == "forty two":
        print("Yes")
    else:
        print("No")

main()