def main():
    word = input("Input: ")
    print("Output: " + shorten(word))

def shorten(words):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for word in words:
        if word in vowels:
            words = words.replace(word,"")
    return words

if __name__ == "__main__":
    main()