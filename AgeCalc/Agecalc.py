#ELIUD MARIERIE      SCT211-0094/2022

from datetime import datetime

name = input("Enter your name : ")

print(f"Welcome {name}, This is a simple calculator that calculates your  age in Years Months and Days !\n")


# Function to calculate age
def calculate_age(year_of_birth):
    # Get the current date
    currentDate = datetime.now()

    # Getting year, month, and day from the current date
    currentYear = currentDate.year
    currentMonth = currentDate.month
    currentDay = currentDate.day

    # Calculateing age
    age_years = currentYear - year_of_birth
    age_months = currentMonth
    age_days = currentDay

    if currentMonth < month_of_birth or (currentMonth == month_of_birth and currentDay < day_of_birth):
        age_years -= 1

    if currentMonth < month_of_birth or (currentMonth == month_of_birth and currentDay < day_of_birth):
        age_months = 12 - month_of_birth + currentMonth
    else:
        age_months = currentMonth - month_of_birth

    if currentDay < day_of_birth:
        age_days = (30 - day_of_birth) + currentDay
    else:
        age_days = currentDay - day_of_birth

    return age_years, age_months, age_days

# Getting year of birth
year_of_birth = int(input("Enter your year of birth: "))
month_of_birth = int(input("Enter your month of birth (1-12): "))
day_of_birth = int(input("Enter your day of birth (1-31): "))

# Calculating age
age_years, age_months, age_days = calculate_age(year_of_birth)

# Displaying the result
print("_________________________________________________________________________")
print(f"Your age is {age_years} years, {age_months} months, and {age_days} days.")
print("_________________________________________________________________________")

