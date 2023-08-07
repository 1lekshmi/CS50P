import sys
import validators

def main():
    print(validate_email(input("What's your email address? ")))

def validate_email(email):
    if validators.email(email):
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    main()
    