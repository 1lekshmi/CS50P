import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif sys.argv[1].endswith(".py") != True:
    sys.exit("Not a Python file")

try:
    with open(sys.argv[1]) as file:
        lines = file.readlines()

        sen = []
        for line in lines:
            sen.append(line.strip())
            
        leng = len(sen)
        for s in sen:
            if s == "" or s[0] == "#":
                leng -= 1
        print(leng)
except FileNotFoundError:
    sys.exit("File does not exist")
