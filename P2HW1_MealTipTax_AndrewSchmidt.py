# Calculate the tax and tip of the tax
# 6/16/2022
# CTI-110 P2HW1 - Meal Tip Tax Calculator
# Andrew Schmidt
#
per = "{:.1%}"
food_cost = float(input("Enter Food Cost: "))
tip = float(input("\nEnter Tip Percentage: ")) 
tax = float(input("Enter Tax Percentage: "))
print('Meal tax percentage: ', per.format(tax/100))
print('Meal tip percentage: ', per.format(tip/100))

calc_tip = float(food_cost * (1 + tip/100))
print("Calculated tip: ", calc_tip)
