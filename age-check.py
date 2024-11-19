# This program determines if the user is a minor or an adult.
# The user enters their age, and the program checks if they are below 18.

age = int(input("Enter your age: "))
if age < 18:
    print("You are a minor.")
else:
    print("You are an adult.")
