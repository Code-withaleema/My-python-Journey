# #Project 1
# list=[]
# while True:
#     print("===Shopping Items===")
#     print("1.Add Items")
#     print("2.Remove Items")
#     print("3.Display all Items")
#     print("4.Search Item")
#     print("5.Total Items")
#     print("6.Exit")
#     choice=int(input("Enter choice: "))
#     if(choice==1):
#         a=input("Item you want to add: ")
#         list.append(a)
#         print("----Item is added successfully!----")
#     elif(choice==2):
#         r=input("Item you want to remove: ")
#         if(r in list): 
#             list.remove(r)
#             print("----Item is removed successfully!----")
#         else:
#             print("Not found")

#     elif(choice==3):
#         print("===Display All Items===")
#         print(list)
#     elif(choice==4):
#         s=input("Search an item: ")
#         if( s in list ):
#             print("Item exsist")
#         else:
#             print("Item not exsist")
#     elif(choice==5):
#        print("Total items: ",len(list))
#     elif(choice==6):
#        print("Thank you")
#        break
# else:
#     print("Invalid")
#Project 2

# #Project 3
# n=[]
# for i in range(10):
#     num=int(input("Enter num: "))
#     n.append(num)
# print("Maximum Number: ",max(n))
# print("Minimum Number: ",min(n))
# print("Sum           : ",sum(n))
# print("Average       : ",sum(n)/len(n))
# for num in n:
#     if num % 2==0:
#         print("Even numbers: ",num)
# for num in n:
#     if num % 2!=0:
#         print("Odd numbers: ",num)
#Project 4
# n=[]
# for i in range(7):
#     l=int(input("Enter numbers: "))
#     n.append(l)
# d=[]
# for l in n:
#     if( l not in d):
#         d.append(l)
# print(d)
#Project 5
# l=[]
# while True:

#    print("===Menu===")
#    print("1.Add Student")
#    print("2.Remove Student")
#    print("3.Show attendence list")
#    print("4.Search Student")
#    print("5.Exit")
#    choice=int(input("Enter Option: "))
#    if choice==1:
#     a=input("Add the student: ")
#     l.append(a)
#     print("Student is add successfully!")
#    elif choice==2:
#      r=input("Remove the student: ")
#      if r in l:
#        print("Student is removed successfully!")
#      else:
#        print("No student found")
#    elif choice==3:
#      print("Show Attendence List")
#      print(l)
#    elif choice==4:
#      s=input("Search the Student: ")
#      if s in l:
#        print(s,"found")
#      else:
#        print("Not found")
#    elif choice==5:
#      print("Thank You!")
#      break
#    else:
#      print("Invalid")
#Project 6
# l=[]
# while True:
#   print("===Favorite Movies===")
#   print("1.Add a movie")
#   print("2.Delete a movie")
#   print("3.Search a movie")
#   print("4.Store movies alphabetically")
#   print("5.Display All movies")
#   print("6.Exit")
#   choice=int(input("Enter Option:"))
#   if choice==1:
#     m=input(("Add a movie: "))
#     l.append(m)
#     print("Movie is added successfully!")
#   elif choice==2:
#     d=input("Delete a Movie: ")
#     if d in l:
#       l.remove(d)
#       print("Movie is Deleted successfully!")
#     else:
#       print("Movie not found")
#   elif choice==3:
#     s=input("Search a movie: ")
#     if s in l:
#       print(s,"found")
#     else:
#       print("not found")
#   elif choice==4:
#     l.sort()
#     print("Sorted movies")
#     print(l)
#   elif choice==5:
#     print("Display all Movies: ")
#     print(l)
#   elif choice==6:
#     print("Thank you")
#     break
#   else:
#     print("Invalid")
#Project 7
l=[]
for i in range(10):
  n=int(input("Enter scores: "))
  l.append(n)
print("===Quiz Scores===")
print("1.Highest Score : ",max(l))
print("2.Lowest Score: ",min(l))
print("3.Average Score: ",sum(l)/len(l))
passed=0
failed=0
for n in l:
    if n>=50:
     passed+=1
    else:
      failed+=1
print("4.Number of Passed Students: ",passed)
print("5.Number of Failed Students: ",failed)
  
      
  




     
     








