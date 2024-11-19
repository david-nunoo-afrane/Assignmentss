# This program checks if the user has passed or failed.
# User enters a score, and the program tells if it's "Pass" or "Fail."

score = int(input("Enter your score (0-100): "))
if score >= 50:
    print("Pass")
else:
    print("Fail")
