# code to compare the greater one of two numbers
# Enter two numbers and the code will tell you which one is greater.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 > num2:
    print("The first number is greater.")
elif num1 < num2:
    print("The second number is greater.")
else:
    print("Both numbers are equal.")
