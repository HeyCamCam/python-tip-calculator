#!/usr/bin/env python3

meal_total = int(input("How much was your meal?: "))
print("Meal is $" + str(meal_total))
tip_percent = int(input("What percentage would you like to tip?: "))
print("Tip percentage is " + str(tip_percent) + "%")
tip_total = meal_total * tip_percent / 100

print("You should tip $" + str(tip_total))

