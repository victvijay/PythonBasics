#Question 1
i = int(input("Value: "))
if(i==10):
    print("CORRECT")
else:
    print("WRONG")

#Question 2
print("-----------------------------")
password = input("Enter the password: ")
if(password=="HOPE@123"):
    print("Your password is CORRECT")
else:
    print("Your password is WRONG")
    
#Question 3
print("-----------------------------")
age = int(input("Age: "))
if(age<18):
    print("Children")
elif((age>=18) and (age<40)):
    print("Adult")
elif((age>=40) and (age<60)):
    print("Citizen")
elif(age>=60):
    print("Senior Citizen")

#Question 4
print("-----------------------------")
num = int(input("Enter any number: "))
if(num>=0):
    print("Num is positive")
else:
    print("Num is negative")

#Question 5
print("-----------------------------")
num = int(input("Enter a number to check: "))
if((num%5)==0):
    print("Num is divisible by 5")
else:
    print("Num is not divisible by 5")
    
