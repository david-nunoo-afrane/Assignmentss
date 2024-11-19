# This program checks the current temperature and gives a description.
# The user enters the temperature, and the program tells if it's hot, warm, or cold.

temperature = int(input("Enter the current temperature: "))
if temperature >= 30:
    print("It’s hot!")
elif 15 <= temperature < 30:
    print("It’s warm.")
else:
    print("It’s cold.")
