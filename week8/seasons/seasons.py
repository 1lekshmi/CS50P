from datetime import date
import sys
import inflect

def main():
     try:
          # prompts user for birth day and converts it into a YYYY-mm-dd datetime format
          bday = input("Date of Birth: ")
          bday = date.fromisoformat(bday)
          print(sing(bday))
     except ValueError:
          sys.exit("Invalid Date")

# returns the numbers of day as words
def sing(bday):
     ndays = days_to_mins(bday, date.today())
     p = inflect.engine()
     song = p.number_to_words(ndays, andword="").capitalize()
     return f"{song} minutes"

# calculates the numbers of days between birthday and today
def days_to_mins(bday,today):
     day_diif = (today - bday).days * 24 * 60
     return day_diif 

if __name__ == "__main__":
    main()
