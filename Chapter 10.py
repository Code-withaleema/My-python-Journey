# #Program 1
# file=open("name.txt","w")
# file.write("ali")
# file.close()
# #Program 2
# file=open("name.txt","r")
# print(file.read())
# file.close()
# #Program 3
# file=open("name.txt","a")
# file.write("\nLahore")
# file.close()
# #Task 1
# a=input("Enter the name: ")
# file=open("name.txt","w")
# file.write(a)
# file.close()
# #Task 2
# file=open("name.txt","r")
# print(file.read())
# file.close()
# # #Task 3
# n=input("Student Name: ")
# c=input("CGPA: ")
# file=open("name.txt","w")
# file.write("Name: "+n)
# file.write("\n")
# file.write("CGPA: "+c)
# file.close()
#Task 4
# while True:
#     print("1.Write Notes")
#     print("2.Read Notes")
#     print("3.Exit")
#     option=input("Select Option: ")
#     if option=="1":
#         a=input("What you want to write: ")
#         file=open("name.txt","a")
#         file.write("Notes:"+a)
#         file.write("\n")
#         file.close()
#     elif option=="2":
#         file=open("name.txt","r")
#         print(file.read())
#         file.close()
#     else:
#         print("Thank you")
#         break
#Task 5
# a=input("Enter Daily Note: ")
# file=open("name.txt","a")
# file.write(""+a)
# file.write("\n")
# file.close()
# #Task 6
# while True:
#     print("1. Add Students")
#     print("2. View Students")
#     print("3. Exit")
#     option=input("Choose the option: ")
#     if option=="1":
#         name=input("Enter Name: ")
#         cgpa=input("Enter CGPA: ")
#         file=open("name.txt","a")
#         file.write("Name: "+name)
#         file.write("\n")
#         file.write("CGPA: "+cgpa)
#         file.close()
#     elif option=="2":
#         file=open("name.txt","r")
#         print(file.read())
#         file.close()
#     elif option=="3":
#         print("Thank you")
#         break
#     else:
#         print("Invalid")
#Super Challenge
balance=[1000]
while True:

    print("===BANK TRANSACTION SYSTEM===")
    print("1. Deposit")
    print("2.Withdraw")
    print("3.View History")
    print("4.Exit")
    option=input("Choose Option: ")
    if  option=="1":
        a=int(input("How much Money you want to deposit: "))
        for i in range(len(balance)):
          balance[0]+=a
        file=open("history.txt","w")
        file.write("Deposited: "+str(balance[0]))
        file.close()
        print("Money is deposited successfully")
    elif option=="2":
        b=int(input("How much Money you want to withdraw: "))
        for i in range(len(balance)):
            if balance[0]>b:
                balance[0]-=a
                file=open("history.txt","w")
                file.write("Withdraw: "+str(balance[0]))
                file.close()
                print("Balance is withdrawn successfully")
            
            else:
                print("Insufficient Balance")
    elif option=="3":
        print("View History")
        file=open("History.txt","r")
        print(file.read())
        file.close()
    elif option=="4":
        print("Thank You")
        break
    else:
        print("Invalid")





            
       









