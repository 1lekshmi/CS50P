import re
import sys

def main():
    print(count(input("Text: ")))

def count(s):
    listofum = re.findall(r"\bum\b", s, re.IGNORECASE)
    return len(listofum)

if __name__ == "__main__":
    main()
    