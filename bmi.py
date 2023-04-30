# Calculate Body Mass Index
print("Please enter your weight in KGs:")
weight = float(input())
print()
print("Please enter your height in CMs:")
height = float(input())
print()
bmi = weight / ((height/100)**2)
print("BMI:")
print(round(bmi, 2))
print()

# Feedback (source: nhs.uk)
print("Feedback:")
if bmi < 18.5:
    print("You're in the underweight range.")
elif bmi <= 24.9:
    print("You're in the healthy weight range.")
elif bmi <= 29.9:
    print("You're in the overweight range.")
else:
    print("You're in the obese range.")