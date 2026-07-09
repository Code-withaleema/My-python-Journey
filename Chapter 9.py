# #Project:1
# def welcome():
#     print("Welcome to Python Programming! ")

# welcome()
# #Project:2
# def calculator(a,b):
#     print("Sum: ",a+b)
#     print("Difference: ",a-b)
#     print("Product: ",a*b)
# calculator(2,10)
# #Project:3
# def marks(m):
#     if(m>=50):
#         print("Pass")
#     else:
#         print("Fail")
# marks(20)
# #Project:4
# def data(name,age):
#     print("Name: ",name)
#     print("Age: ",age)
# data("Aleema",20)
#Project:5
# def add(a,b):
#     print("Add: ",a+b)
# def subtract(a,b):
#     print("Subtract: ",a-b)
# def product(a,b):
#     print("Product: ",a*b)
# def divide(a,b):
#     print("Divide: ",a/b)
# while True:
#     print("===Menu===")
#     print("1.Add")
#     print("2.Subtract")
#     print("3.Multiply")
#     print("4.Divide")
#     print("5.Exit")
   
#     option=input("Enter Option: ")
#     if option=="1":
#         i=int(input("Enter a: "))
#         j=int(input("Enter b: "))
#         add(i,j)
#     elif option=="2":
#         a=int(input("Enter a: "))
#         b=int(input("Enter b: "))
#         subtract(a,b)
#     elif option=="3":
#         c=int(input("Enter a: "))
#         d=int(input("Enter b: "))
#         product(c,d)
#     elif option=="4":
#         e=int(input("Enter a: "))
#         f=int(input("Enter b: "))
#         divide(e,f)
#     elif option=="5":
#         print("Thank youuu")
#         break
#     else:
#         print("Invalid")
#Challenging Project
# l=[]
# def add_student():
#     print("==Add Student==")
#     a=input("Which student you want to add: ")
#     l.append(a)
#     print("New Student is added successfully")
# def search_student():
#     print("==Search Student==")
#     b=input("Which student you want to search: ")
#     if b in l:
#         print("Student Found")
#     else:
#         print("Not Found")
# def remove_student():
#     print("==Remove Student==")
#     c=input("Which student you want to remove: ")
#     if c in l:
#         l.remove(c)
#         print("Student is removed successfully")
#     else:
#         print("Not Found")
# def display_student():
#     print("==Display Student==")
#     print(l)
# def count_student():
#     print("==Count Student==")
#     print("Total students: ",len(l))
# while True:
#     print("===Student Managment System===")
#     print("1.Add Student")
#     print("2.Search Student")
#     print("3.Remove Student")
#     print("4.Display Student")
#     print("5.Count Students")
#     print("6.Exit")
#     option=input("Enter Option: ")
#     if option=="1":
#         add_student()
        
#     elif option=="2":
#         search_student()
#     elif option=="3":
#         remove_student()
#     elif option=="4":
#         display_student()
#     elif option=="5":
#         count_student()
#     elif option=="6":
#         print("Thank You!")
#         break
#     else:
#         print("Invalid....")
#Challenging Project
balance=[1000]
def deposit_money():
    a=int(input("How much money you want to deposit: "))
    for i in range(len(balance)):
        balance[i]+=a
    print("Money is deposited successfully!")
    print("Now total balance become: ",balance)
def withdraw_money():
    b=int(input("How much amount you want to withdraw: "))
    for i in range(len(balance)):
       if balance[i]>b:
        balance[i]-=b
       print("Money is withdrawn successfully!")
    else:
        print("Error")
        print("Insufficient Balance")
    print("Now total balance become: ",balance)
def check_balance():
    print("Check the balance")
    print("The balance is ",balance)
def exit():
    print("Thank You")
while True:
    print("Bank Managment System")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check Balance")
    print("4. Exit")
    option=input("Choose the Option: ")
    if option=="1":
        deposit_money()
    elif option=="2":
        withdraw_money()
    elif option=="3":
        check_balance()
    elif option=="4":
        exit()
        break
    else:
        print("Invalid...")
        



 




        


