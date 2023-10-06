#ELIUD MARIERIE      SCT211-0094/2022

def calculate_total_bill_amount(bill_amount, tip_percentage):
    tip_amount = bill_amount * (tip_percentage / 100)
    total_amount = bill_amount + tip_amount
    return total_amount

def calculate_per_person_amount(total_amount, num_people):
    per_person_amount = total_amount / num_people
    return per_person_amount

bill_amount = float(input("Enter the total bill amount: "))

while True:
    tip_percentage = int(input("Enter the tip percentage (10, 12, or 15): "))
    if tip_percentage in [10, 12, 15]:
        break
    else:
        print("Invalid input. Please enter 10, 12, or 15 for the tip percentage.")

num_people = int(input("Enter the number of people splitting the bill: "))

total_amount = calculate_total_bill_amount(bill_amount, tip_percentage)

per_person_amount = calculate_per_person_amount(total_amount, num_people)

print(f"Each person should pay: Ksh.{per_person_amount:.2f}")
