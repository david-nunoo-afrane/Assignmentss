# This program assigns a grade based on the user's score.
# The user enters a score out of 100, and the program assigns a grade (A, B, C, D, or F).

score = int(input("Enter your score out of 100: "))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")
