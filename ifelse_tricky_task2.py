#PracticeQuestion(TRiangle Type checker)
a= int(input("Enter a: "))
b= int(input("Enter b: "))
c= int(input("Enter c: "))
if(a==b==c):
    print("Equilateral Triangle")
elif(a==b or b==c or a==c):
    print("Isoceles Triangle")
elif(a!=b and b!=c and c!=a):
    print("Scalene TRiangle")
else:
    print("Not Valid Triangle")
#PracticeQuestion(Number guessing)
fixednum=9
num=int(input("Enter number: "))
if(num==fixednum):
    print("Correct Guess")
else:
    print("Wrong Guess")
#PracticeQuestion(Discount System)
shopnum=int(input("Enter amonut:"))
if(shopnum>=5000):
    bill=shopnum*(20/100)
    print("Final bill : ",bill)
elif(shopnum>=3000 and shopnum<5000):
    bill=shopnum*(10/100)
    print("Final bill : ",bill)
elif(shopnum>=1000 and shopnum<3000):
    bill=shopnum*(5/100)
    print("Final bill : ",bill)
elif(shopnum<1000):
    print("No Discount")
    print("Final bill : ",shopnum)
else:
    print("Invalid")
#practiceQuestion(Leap Year Checker)
year=int(input("Enter year: "))
if(year%4==0 and year%100!=0 or year%400==0):
    print("Leap Year")
else:
    print("Not Leap Year")