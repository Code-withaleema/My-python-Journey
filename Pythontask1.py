#Practice Question1(Number Range Check)
Number=int(input("Enter Number: "))
if(Number>=1 and Number<=10):
    print("Small Number")
else:
    print("Large Number")    
#Practice Question2(Password Check)
Password=input("Enter Password: ")
if(Password=="Python123"):
    print("Access Granted")
else:
    print("Access Denied")
#Practice Question3(Temperature Check)
Temp=int(input("Enter termperature: "))
if(Temp>=30):
    print("Hot Day")
else:
    print("Cold Day")
#Practice Question4(Age Category Check)
age=int(input("Enter Age: "))
if(age>=0 and age<=12):
    print("Child")
elif(age>=13 and age<=19):
    print("Teen")
else:
    print("Adult")
#Practice Question5(Multiple of 5 Check)
num=int(input("Enter Number: "))
if(num%5==0):
    print("Multiple of 5")
else:
    print("Not Multiple of 5")
#Practice Question6(Simple Logic System)
username=input("Enter Username: ")
if(username=="Admin"):
    print("Welcome Admin")
else:
    print("Unknown Admin")
#Practice Question7(Positive Even Number Check)
num1= int(input("Enter Number: "))
if(num1>0 and num1%2==0):
    print("Positive Even Number")
else:
    print("Other")