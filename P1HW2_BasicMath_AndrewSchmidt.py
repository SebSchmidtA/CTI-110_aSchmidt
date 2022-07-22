# Calculating monthly expenses
# 6/13/2022
# CTI-110 P1HW2 - Basic Math
# Andrew Schmidt
#

#unformatted values
expense=input("Enter name of expense: ")
charge=float(input("Enter monthly charge: "))
tax= float(charge*.06)
monthly_charge= float(charge+tax)
annual_charge= float(monthly_charge*12)

#formatted values
ccharge="${:.2f}".format(charge)
ctax="${:.2f}".format(tax)
cmonthly_charge="${:.2f}".format(monthly_charge)
cannual_charge="${:.2f}".format(annual_charge)

#I tried two different ways of formatting currecy here
print("\n")
print("Bill: ", expense, "------- Before Tax: ",f'${charge:.2f}')
print("Monthly Tax: ",ctax)
print("Monthly Charge: ",cmonthly_charge)
print("Annual Charge: ",cannual_charge)
