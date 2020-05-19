#!/usr/bin/env python3.8

#BMI = (weight in kg / height in meters squared)
#BMI = (weight in lbs / height in inches squared) * 703

def gather_info():
    height = float(input("What is your height? (in inches or meters) "))
    weight = float(input("What is your weight? (in pounds or kilograms) "))
    system = input("Are your measurements in metric or imperial units? ").lower().strip()
    return (height, weight, system)

def calculate_bmi(weight, height, system='metric'):
    """
    Return the Body Mass Index (BMI) for the
    given weight, height, and measurement system.
    Default is the metric system.
    """
    if system == 'metric':
        bmi = (weight / (height ** 2))
    else:
        bmi = 703 * (weight / (height ** 2))
    return bmi

while True:
    height, weight, system = gather_info()
    if system == "imperial":
        bmi = calculate_bmi(weight, system='imperial', height=height)
        print(f"Your BMI is {bmi}")
        break
    elif system == "metric":
        bmi = calculate_bmi(weight, height)
        print(f"Your BMI is {bmi}")
        break
    else:
        print("Error: Unknown measurement system. Please use imperial or metric.")
