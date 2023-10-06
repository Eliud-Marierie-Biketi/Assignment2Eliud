#ELIUD MARIERIE         SCT211-0094/2022

name = input("Enter your Name: ")
print(f"Hello {name}, We are going to calculate your BMI and tell you if you are:\n 1.Overweight\t2.Normalweight\t3.Underweight")

patientWeight = float(input("Enter your weight in KGs:"))
patientHeight = float(input("Enter your height in Metres:"))

patient_BMI = patientWeight/pow(patientHeight, 2)
print("_______________________________________________")
print(f"Your BMI is{patient_BMI: 3f}")

if patient_BMI < 18.5 :
    print(f"{name}, you are Underweight.")
elif patient_BMI > 18.5 and patient_BMI <24.9 :
    print(f"{name}, you are of Normal weight.")
else :
    print(f"{name}, you are Overweight.")
print("________________________________________________")

