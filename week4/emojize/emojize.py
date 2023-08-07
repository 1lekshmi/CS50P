import emoji

def main():
    emote = input("Input: ")
    convert(emote)

def convert(n):
    print("Output: ", emoji.emojize(n, language = 'alias'))

main()