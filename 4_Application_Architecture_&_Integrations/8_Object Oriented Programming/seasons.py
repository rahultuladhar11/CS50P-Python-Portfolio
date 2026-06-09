from datetime import datetime, date
import inflect
import sys

def main():
    ### A. Get input from user in YYYY-MM_DD format ###
    dob = input("Date of Birth:" ).strip()

    if valid_date(dob):
        sys.exit("Invalid date")

    minutes = age_to_min(dob)

    print(min_to_words(int(minutes)), "minutes")


# A.1. Check date validity #
def valid_date(dob):
    try:
        datetime.strptime(dob, '%Y-%m-%d')

    except ValueError:
        return True

### B. Calculate age to minutes ###

def age_to_min(dob):
    age = date.today() - date.fromisoformat(dob)
    return age.total_seconds()/60


### C. Convert age data in English ###
def min_to_words(min):
    translate = inflect.engine()
    english = translate.number_to_words(min)
    return english.replace(" and", "").capitalize()

if __name__ == "__main__":
    main()
