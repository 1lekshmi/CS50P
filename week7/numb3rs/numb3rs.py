import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):

        if not re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip):
             return False
        else:
            numbers = ip.split(".", maxsplit = 3)

            for num in numbers:
                if re.search(r"^([01][0-9][0-9]|2[0-4][0-9]|25[0-5])$",num):
                    return True
                else:
                    return False

if __name__ == "__main__":
    main()
    