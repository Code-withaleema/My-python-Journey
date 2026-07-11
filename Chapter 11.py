#Practice:01
try:
    age=int(input("Enter Age: "))
    print("age: ",age)
except:
    print("Invalid Age")
#Practice:02
try:
    a=int(input("Enter First Number: "))
    b=int(input("Enter Second Number: "))
    print("Division Answer: ",a/b)
except:
    print("Invalid Input or Cannot Divide by Zero")
#Practice:03
try:
    marks=int(input("Enter Marks: "))
    print("Result Saved")
except:
    print("Invalid Marks")
#Project:01
#simple login
try:
    pin=int(input("Enter PIN: "))
    print("Login Successful")
except:
    print("Invalid PIN")
#Project:02
#Safe Calculator
try:
    num1=int(input("Enter Number: "))
    num2=int(input("Enter Number: "))
    print("Addition: ",num1+num2)
    print("Subtraction: ",num1-num2)
    print("Product: ",num1*num2)
    print("Division: ",num1/num2)
except:
    print("INVALID INPUT")
