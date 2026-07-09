# #Project:1
# fruit={"apple","kiwi","peach","papaya"}
# print(fruit)
# fruit.add("Cherry")
# fruit.remove("apple")
# print(fruit)
#Project:2
# students={"Muqadas","Mehak","Ali"}
# students.add("Zimal")
# s=input("Search Student: ")
# if s in students:
#     print("Found")
# else:
#     print("Not Found")
# students.remove("Mehak")
# print(students)
#Project:3
# A={1,2,3,4}
# B={3,4,5,6}
# print("Union: ",A | B)
# print("Intersection : ",A & B)
# print("Difference: ",A - B)
# print("Symmetric difference: ",A ^ B)
#Project:4
# num=set()
# for i in range(10):
#     a=input("Enter Numbers:  ")
#   num.update(a)
# print("Unique numbers: ",num)
# print("Total unique numbers: ",len(num))
#Challenge Project
c=set()
while True:
    print("1.Register Student")
    print("2.Remove Student")
    print("3.Search Student")
    print("4.Disply All Students")
    print("5.Total Registered Students")
    print("6.Exit")
    choice=input("Enter option: ")
    if choice=="1":
        r=input("Enter the student you want to register: ")
        c.add(r)
        print("Student is registered successfully!")
    elif choice=="2":
        a=input("Which student you want to remove: ")
        if a in c:
            c.remove(a)
            print("Student is removed successfully!")
        else:
            print("No STudent found")
    elif choice=="3":
        s=input("Search the student: ")
        if s in c:
            print("Student exists")
        else:
            print("Studnet not exists")
    elif choice=="4":
        print("Display All Students")
        print(c)
    elif choice=="5":
        print("Total registered students: ",len(c))
        
    elif choice=="6":
        print("Thank You! Program is closed")
        break
    else:
        print("Invalid Error....")
    


