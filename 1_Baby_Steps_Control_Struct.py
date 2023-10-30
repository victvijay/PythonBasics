#Question-1

print("Welcome to Assignment-1")

#Question-2

num1=int(input("Num1= "))
num2=int(input("Num2= "))
print("Add= ",num1+num2)

#Question-3

bmi_index = float(input("Enter the BMI Index: "))

if(bmi_index<=18.5):
    print("Under weight")
elif(bmi_index>18.5 and bmi_index<=24.9):
    print("Normal weight")
elif(bmi_index>24.9 and bmi_index<=29.9):
    print("Pre-obesity")
elif(bmi_index>29.9 and bmi_index<=34.9):
    print("Obesity class |")
elif(bmi_index>34.9 and bmi_index<=39.9):
    print("Obesity class ||")
elif(bmi_index>39.9):
    print("Obesity class |||")
