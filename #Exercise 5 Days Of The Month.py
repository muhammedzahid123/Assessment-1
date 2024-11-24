#Exercise 5 Days Of The Month

# Define the number of days in each month
days_in_month = {
    1: 31,  # January
    2: 28,  # February (default value)
    3: 31,  # March
    4: 30,  # April
    5: 31,  # May
    6: 30,  # June
    7: 31,  # July
    8: 31,  # August
    9: 30,  # September
    10: 31, # October
    11: 30, # November
    12: 31  # December
}

# Determine if a given year is a leap year
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Prompt the user for the month number
try:
    month = int(input("Enter a month number (1-12): "))

    if month < 1 or month > 12:
        print("Please enter a valid month number between 1 and 12.")
    else:
        # Handle February separately for leap years
        if month == 2:
            year = int(input("Enter a year: "))
            if is_leap_year(year):
                print("February has 29 days (leap year).")
            else:
                print("February has 28 days.")
        else:
            print(f"Month {month} has {days_in_month[month]} days.")
except ValueError:
    print("Invalid input. Please enter numbers only.")