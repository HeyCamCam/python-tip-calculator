#!/usr/bin/env python3

meal_total = float(input("How much was your meal?: "))
print("Meal is $" + str(meal_total))
tip_percent = int(input("What percentage would you like to tip?: "))
print("Tip percentage is " + str(tip_percent) + "%")
tip_total = round(meal_total * tip_percent / 100, 2)

print("You should tip $" + str(tip_total))
