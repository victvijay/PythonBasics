#Program 1:
class SubfieldsInAI:

    def Subfields():
        print("Subfields in AI are:")
        list=("Machine learning","Nueral networks", "Vision","Robotics", "Speech processing","Natural Language Processing")
        for temp in list:
            print(temp)

SubfieldsInAI.Subfields()
print("---------------------------------")
#Program 2:
class OddEven:

    def OE():
        num = int(input("Enter a number"))
        if((num%2)==0):
            print(num, " is Even number")
        else:
            print(num, " is Odd number")

OddEven.OE()
print("---------------------------------")
#Program 3:
class ElegibilityForMarriage:

    def Elegible():
        gender = input("Your gender: ")
        age = int(input("Your age: "))
        if(age>=21):
            print("Elegible")
            output = "Elegible"
        else:
            print("Not Elegible")
            output = "Not Elegible"
        return output

ElegibilityForMarriage.Elegible()
print("---------------------------------")
#Program 4:
class FindPercent:

    def percentage():
        sub1 = float(input("Subject1= "))
        sub2 = float(input("Subject2= "))
        sub3 = float(input("Subject3= "))
        sub4 = float(input("Subject4= "))
        sub5 = float(input("Subject5= "))
        Total = sub1 + sub2 + sub3 + sub4 + sub5
        print("Total= ", Total)
        print("Percentage = ", Total/5)

FindPercent.percentage()
print("---------------------------------")
#Program 5:
class Triangle:

    def formula():
        height = float(input("Height: "))
        breadth = float(input("Breadth: "))
        print("Area formula: (Height*Breadth)/2")
        print("Area of triangle: ",((height*breadth)/2))
        height1 = float(input("Height1: "))
        height2 = float(input("Height2: "))
        breadth1 = float(input("Breadth: "))
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of triangle: ", height1+height2+breadth1)
        
Triangle.formula()
