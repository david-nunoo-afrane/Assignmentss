# This program checks if the user is eligible for a discount based on their age.
# The user enters their age, and the program determines if they qualify for a discount.

age = int(input("Enter your age: "))
if age < 12 or age > 65:
    print("You are eligible for a discount.")
else:
    print("No discount available.")
