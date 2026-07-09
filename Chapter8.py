# #Project:1
# students={
#     "Name":"Ali",
#     "Age": 20,
#     "Course":"BSCS",
#     "CGPA": 3.8
#     }
# print(students)
#Project:2
# phone={
#     "Ali": "03001234567",
#     "Sara": "03111234567"
# }
# while True:
#     print("===PHONE BOOK===")
#     print("1.Add Contact")
#     print("2.Search Contact")
#     print("3.Delete Contact")
#     print("4.Display All Contact")
#     print("5.Exit")
#     print("=====================")
#     choice=input("Select Option: ")
#     if choice=="1":
#         print("Add the Contact")
#         n=input("Enter Name: ")
#         p=input("Enter Phone No: ")
#         phone[n]=p
#         print("Contact Add Successfully!")
#     elif choice=="2":
#         print("Search the contact")
#         s=input("Search name: ")
#         if s in phone:
#             print("Found")
#         else:
#             print("Not Found")
#     elif choice=="3":
#         print("Delete the contact")
#         d=input("Enter name: ")
#         if d in phone:
#             phone.pop(d)
#             print("Contact is deleted successfully!")
#         else:
#             print("Not Found")
#     elif choice=="4":
#         print("Display All Contact")
#         print(phone)
#     elif choice=="5":
#         print("Thank youu!")
#         break
#     else:
#         print("Invalid")
#Project:3
Products={
    "Laptop":85000,
    "Mouse" :1500,
    "Keyboard ":3000
}
while True:
    print("===Product Inventory===")
    print("1.Product Name")
    print("2.Price")
    print("3.Add Product")
    print("4.Remove Product")
    print("5.Exit")
    choice=input("Enter Option: ")
    if choice=="1":
        print("===Product Name===")
        print(Products.keys())
    elif choice=="2":
        print("===Price===")
        print(Products.values())
    elif choice=="3":
        print("===Add Product==")
        a=input("Enter the Product you want to add: ")
        b=input("Enter the price of product: ")
        Products[a]=b
        print("Prodcut Added Successfully!")
    elif choice=="4":
        r=input("Which Product you want to remove: ")
        if r in Products:
            Products.pop(r)
            print("Product is removed successfully")
        else:
            print("Product not Found")
    elif choice=="5":
        print("Thank youu")
        break
    else:
        print("Invalid....")


    