#Practice:01
'''for i in range(10):
    i+=1
    print(i)
#Practice:02
for i in range(5):
    print("Aleema Baig")
#Practice:03
a="Python"
for ch in a:
    print(ch)
#Practice:04
for i in range(2,21,2):
    print(i)
#Practice:05
i=1
while i<=5:
    print(i)
    i+=1
#Mini Project
num=int(input("Enter the Number: "))
for i in range(1,11):
   print(num ,"x", i ,"=" ,num*i)
#Medium Level
#Practice: 06
sum=0
for i in range(1,11 ):
    sum+=i
print("Sum= ",sum)
#Practice: 07
total=0
for i in range(1,21,2):
    total+=i
print("Total Even Numbers : ",total)
#Practice: 08
name=input("Enter Name : ")
count=0
for ch in name:
    count+=1
print("Number of Letters in Name : ",count)
#Practice: 09
n=int(input("Enter the number : "))
for i in range (1,n+1):
    print(i)
#Practice: 10
for i in range(1,6):
    print("*"*i)  
#Practice: 11
for i in range(5,0,-1):
    print("*"*i)
#Practice: 12
for i in range(1,6):
    for j in range(1,6):
        if(i>=j):
            print(j,end="")
    print()

#Practice: 14
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end="")
    print()

#Practice: 15
for i in range(5,0,-1):
    for j in range(5,0,-1):
        if(i>=j):
            print("*",end="")
    print()
      
#Practice: 16
for i in range(1,6):
    for j in range(1,6):
        print(i,end="")
    print()  
#Practice: 17
for i in range(1,6):
    for j in range(1,6):
        print(j,end="")
    print()
#Practice: 18
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()
#Practice: 19
for i in range(1,6):
    for j in range(1,i+1):
        if(i>=j):
            print(i,end="")
    print()
#Practice: 20
for i in range(5,0,-1):
    for j in range(i):
        if(i>=j):
            print(i,end="")
    print()
#Practice: 21
for i in range(1,6):
    for j in range(5,0,-1):
        print(j,end="")
    print()
#Practice: 22
for i in range(1,6):
    for j in range(5,5-i,-1):
         print(j,end="")
    print()
#Practice: 21
for i in range(1,6):
    for j in range(1,i+1):
        ch="ABCDE"
        print(ch[j-1],end="")
    print()
#Practice: 22
for i in range(1,6):
    for j in range(1,i+1):
        ch="ABCDE"
        print(ch[i-1],end="")
    print()
#Mini Project:1
n=int(input("Enter a number : "))
for i in range(1,11):
    
    print(n,"x",i,"=",i*n)
#Mini Project: 2
n=int(input("Enter the number : "))
for i in range(n,0,-1):
    print(i)
print("Time's Up")
#Mini Project: 3
n=int(input("Enter Number : "))
sum=0
for i in range(n+1):
    sum+=i

print("Sum : ",sum)
#Mini Project: 4
count1=0 
count2=0
for i in range(21):
    if(i%2==0):
        count1+=1
    else:
        count2+=1    
print("total Even number:",count1)
print("total Odd number:",count2)
#Mini Project: 5
p="admin123"
while(True):
    u=input("Enter Password : ")
    if(u!=p):
        print("Wrong Password")
    else:
        print("Access Granted")
        break   
#Mini Project: 6
a=input("Enter text: ")
count=0
for ch in a:
    if(ch.lower() in"aeiou"):
        count+=1
print("No of vowels : ",count)
#Mini Project: 7
f=6
while(True):
    n=int(input("Enter Number: "))
    if(n!=f):
        print("Wrong Number")
    else:
        print("You Win!")
        break'''
#Mini Project: 8
Total=0
for i in range(1,6):
    n=int(input("Enter Subject Marks : "))
    Total+=n
Average=Total/5
print("Total: ",Total,"Average: ",Average)






    
