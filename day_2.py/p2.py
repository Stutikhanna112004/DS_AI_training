marks = 70

if(marks>=40):
    print("student is pass in exam")
else:
    print("better luck next time")
#student is pass in exam 

age = int(input("enter a Age:"))
if(age>=18):
    print("Congrats! you are selected")
else:
    print("Alas! you are NOT selected")
#enter a Age:19
#Congrats! you are selected

a = int(input("enter a nummber:"))
if (a%2==0):
    print("number is even")
else:
    print("number is odd")
#enter a nummber:44
#number is even

l=int(input("Enter a number:"))
if(l>=0):
    print("Positive Number!!")
elif(l<=0):
    print("Negative Number!!")
else:
    print("Zero!!")
#Enter a number-4
#Negative Number

agee= int(input("Enter your Age: "))
license = input("Do you have a license? yes/no:")
if(agee>=20):
    if(license.lower()=="yes"):
        print("You can drive")
    else:
        print("You need a license first")
else:
    print("you are under age")
#Enter your Age: 20
#Do you have a license? yes/no: yes
#You can drive