#Practice : 1
"""name="aleema Baig"
print(name[0])
print(len(name))
print(name.startswith("Aleema"))
print(name.endswith("Baig"))
print(name.replace("Aleema","Aleeha"))
print(name.title())
#Practice : 2
n="University"
print(n[9])
#Practice : 3
subject="Chemistry"
print(subject.upper())
print(subject.lower())
#Practice : 4
a="Python is fun"
print(a[0:6])
print()
#Practice : 5
b=input("Enter Name : ")
parts=b.split()
print("First Name : ",parts[0])
print("Second Name : ",parts[1])
#Practice : 6
word=["I","love","Python"]
print(" ".join(word))
#Practice : 6
c="Ahmed"
d="Khan"
print(c+" "+d)
#Project 
s=input("Enter a sentence: ")
print(len(s))
print(s.upper())
print(s.lower())
print(s.title())
print(s.strip())
print(s.replace("Aleema","Affan"))
print(s.startswith("My"))
print(s.endswith("old"))
print(s.split())
#Mini Project 1
n=input("Enter Full name: ")
print("Original name: ",n)
print("Uppercase: ",n.upper())
print("Lowercase: ",n.lower())
print("Length: ",len(n))
print("First Character: ",n[0])
print("Last Character: ",n[-1])
#Mini Project 2
count1=0
count2=0
count3=0
n=input("Enter : ")
for ch in n:
    if(ch.lower() in"a,e,i,o,u"):
        count1+=1
    if(ch.lower() not in " ,a,e,i,o,u"):
        count2+=1
    if(ch.lower() in " "):
        count3+=1
print("Total vowels:  ",count1)
print("Total consonants:  ",count2)
print("Total spaces:  ",count3)
#Mini Project 3
count=0
n=input("Enter : ")
parts=n.split()
space=n.strip()
print("Number of words: ",len(parts))
print("Numbers of Characters: ",len(n))
for ch in n:
    if(ch.lower() in " "):
        count+=1
print("Number of spaces: ",count)
#Mini Project 4
e=input("Enter email: ")
if("@" in e  and e.endswith(".com") and " " not in e ):
    print("Valid")
else:
    print("Invalid")
#Mini Project 5
u=input("Enter username: ")
if(u[0].isalpha() and u.isalnum() and len(u)>=6):
    print("Valid")
else:
    print("Invalid")
#Mini Project 6
a=input("Enter the word: ")
r=a[::-1]
print("Input: ",a)
print("Output: ",r)
if(a==r):
    print("Palindrome")
else:
    print("Not Palindrome")
#Mini Project 7
b=input("Enter sentence: ")
print("Characters : ")
c=b[::-1]
print(c)
w=b.split()
r=w[::-1]
print("Words : ")
print(" ".join(r))
#Mini Project 8
count=0
n=input("Enter text : ")
printed=""
for ch in n:
    if (ch not in printed):
        print(ch ,":",n.count(ch))
        printed+=ch
#Mini Project 9
n=input("Enter Password: ")
has_upper=False
has_lower=False
has_digit=False
has_special=False
for ch in n:
    if(ch.isupper()):
        has_upper=True
    if(ch.islower()):
        has_lower=True
    if(ch.isdigit()):
        has_digit=True
    if(not ch.isalnum()):
        has_special=True
if(len(n)>=8 and has_upper and has_lower and has_digit and has_special ):
    print("STRONG PASSWORD")
else:
    print("WEAK PASSWORD")
#Mini Project 10
text=input("Enter text : ")
old_word=input("Word to replace: ")
new_word=input("New word: ")
print(text.replace(old_word,new_word))
#Mini Project 10
a=input("Enter word : ")
b=input("Enter word : ")
count=0
count1=0
if(len(a)>len(b)):
    print(a ,"is Longest word")
else:
    print(b ,"is longest word")
if(len(b)<len(a)):
    print(b, "is shortest word")
else:
    print(a ,"is shortest word")
for ch in a :
    count+=1
for ch in b:
    count1+=1
print("Average word length: ",(count+count1)/2)
#Mini Project 11
s=input("Enter text: ")
words=s.split()
printed=[]
for word in words:
    if(words not in printed):
        print(word,":",words.count(word))
        printed+=word"""
#Major Project
p=input("Enter a paragraph: ")
print("Original Paragraph: ",p)
print("Uppercase Version: ",p.upper())
print("Lowercase Version: ",p.lower())
print("Total Characters: ",len(p))
words=p.split()
count=len(words)
print("Total words : ",count)
space=" "
count1=0
for space in p:
 if(" " in p):
    count1+=space
    print("Total spaces: ",count1)





       
    




