#!/usr/bin/env python3

import random

stupid_response = ['You\re so generous.', 'Good for you.', 'Or maybe more...', '...But was the meal that good? Just saying.', 'Eating out is expensive.']

meal_total = float(input("How much was your meal?: "))
print("Meal is $" + str(meal_total))
tip_percent = int(input("What percentage would you like to tip?: "))
print("Tip percentage is " + str(tip_percent) + "%")
tip_total = round(meal_total * tip_percent / 100, 2)

print(f"You should tip ${str(tip_total)}.")
print(f"{random.choice(stupid_response)}")
