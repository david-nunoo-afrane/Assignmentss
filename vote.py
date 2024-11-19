# Code to check if the someone is eligible to vote.

age = int(input("Enter your age: "))  
country = input("Enter your country: ") 

if age >= 18 and (country == "Ghana" or country == "ghana" or country == "GHANA"):  
    print("You can vote.")  
else:  
    print("You cannot vote.")  
