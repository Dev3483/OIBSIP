
"""
    Calculate BMI (Body Mass Index)

    weight: weight in kg
    height: height in meters
    Give BMI value and Range of it.
"""
   
print("BMI Calculator")
try:
        
    weight =float( input("Enter your weight (in kg): "))
    height =float( input("Enter your height (in meters): "))
    if weight <= 0 or height <= 0:
            raise ValueError("Weight and height must be positive numbers")
    else:
          bmi = weight / (height ** 2)
except ValueError as e:
        print(f"Error: {e}")
except TypeError:
        print("Error: Invalid input type. Please enter numbers only.")

print(f"Your BMI is: {bmi:.2f}")
if (bmi <= 18.4):
           print("You are Underweight")
elif (bmi >= 18.5 and bmi <= 24.9):
            print("Your Weight is Normal")
elif (bmi >= 25 and bmi <= 29.9):
            print("You are Overweight")
elif (bmi >= 30 and bmi <= 34.9):
            print("You are in Obese Class I")
elif (bmi >= 35 and bmi <= 39.9):
            print("You are in Obese Class II")
elif (bmi >= 40):
            print("You are in Obese Class III")