# -*- coding: utf-8 -*-
 #Getting input of the user
Weight = float(input("Enter your weight in kg: " ))
Height = float(input("Enter your height in cm: "))
Age = int(input("Enter you age in years: "))
Gender = input("What is your gender?: (Male or Female) ")

    #Calculating BMR
def calculate_bmr(Gender, Weight, Height, Age):
    "Calculating the Basal Metabolic Rate (BMR)"
    if Gender == "Male":
        bmr =  88.362 + (13.397 * Weight) + (4.799 * Height) - (5.677 * Age)
    else: 
        bmr = 447.593 + (9.247 * Weight) + (3.098 * Height) - (4.330 * Age)
    return bmr

    
bmr = calculate_bmr(Gender, Weight, Height, Age)
print(bmr)

#calculating the maintenance calories, taking in the amount of exercise
Workouts = int(input("Enter the amount of workouts you do in a week: " ))
Workouts2 = input("Would you classify this exercise as light, moderate or hard? ")

def calculate_main(bmr, Workouts, Workouts2):
    "Calculating the maintenance calories with the amount of exercise"
    if Workouts == 0:
        main = bmr * 1.2  # sedentary
    elif Workouts in [1, 2] or (Workouts == 3 and Workouts2 == "light"):
        main = bmr * 1.375  # lightly active
    elif Workouts in [3, 5] and Workouts2 in ["moderate", "hard"]:
        main = bmr * 1.55  # moderately active
    elif Workouts in [6, 7]:
        main = bmr * 1.725 # Very active
    elif Workouts >7:
        main = bmr * 1.9 # Extra active
    else:
        main = bmr * 1.2  # default fallback
    return main

main = calculate_main(bmr, Workouts, Workouts2)
print(main)

#defining the goal and using that to calculate the calories needed
Goal = input("Enter your goal: (weightgain, maintenance, weightloss) ")
Time = input("Do you want to reach your goal quickly or slowly? ")
def calculate_cal(main, Goal):
    "Calculating the needed calories bij adding or subtracting either 250 or 500 calories"
    if Goal == "weightgain" and Time == 'quickly':
        cal = main + 500
    elif Goal =="weightgain" and Time == "slowly":
        cal = main + 250
    elif Goal == "weightloss" and Time == "quickly":
        cal = main - 500
    elif Goal == "weightloss" and Time == "slowly":
        cal = main - 250
    else:
        cal = main
    return cal
calories = calculate_cal(main,Goal)
print(calories)
        