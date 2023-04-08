print("if...else statement 15 programs")

print("--1.old and even check")

x=int(input("Enter a number: "))
if x%2==0:
 print(x," is even number")
else:
 print(x," is odd number")

print("--2.three enter who is big number")
a=int(input("Enter number1="))
b=int(input("Enter number2="))
c=int(input("Enter number3="))
if a>b and a>c:
 print(a," a is biggest")
elif b>a and b>c:
 print(b," b is biggest")
else:
 print(c," c is biggest")

print("--3.three enter who is small number")
a=int(input("Enter number1="))
b=int(input("Enter number2="))
c=int(input("Enter number3="))
if b>a and c>a:
 print(a," a is smallest")
elif a>b and c>b:
 print(b," b is smallest")
else:
 print(c," c is smallest")
print("--4.check positive number ")
n=int(input("Enter any number:"))
if n>=0:
    print(n," is positive number")
else:
    print(n, " is not positive number")
print("--5.check nagative number")
n=int(input("Enter any number:"))
if n<0:
    print(n," is nagative number")
else:
    print(n, " is not nagative number")
print("--6.Age valid to drive ")
n = int(input("Enter your age : "))
if(18<=n):
    print("your age is valid to drive")
else:
    print("your age is invalid plase play to toy drive")

print("--7.Leep Year")
y=int(input("Enter year to be checked : "))
if(y%4==0 and y%100!=0 or y%400==0):
    print(y, " The year is leap year")
else:
    print(y, " The year isn't leap year")


print("--8.sunny Number")       #3 = 3+1 = 4
import math
n=int(input("Enter the number : "))
x=math.sqrt(n+1)
if int(x) == x:
    print(n," is sunny Number")
else:
    print(n," is not sunny number")

print("--9.Anagram")         #coal cola
s1=input("enter first string: ")
s2=input("enter second string: ")
if sorted(s1) == sorted(s2):
    print("this string are anagram.")
else:
    print("this string aren't anagram.")

print("--10.GCD")
def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)

a=int(input("Enter first number : "))
b=int(input("Enter second number : "))
ans=gcd(a,b)
print("GCD is: ",ans)


print("--11.LCD")
a=int(input("Enter first number : "))
b=int(input("Enter second number : "))
if(a>b):
    min = a
else:
    min = b
while(1):
    if(min%a==0 and min%b==0):
        print("LCM is : ",min)
        break
    min = min +1

print("--12.Marksheet")
a=int(input("Enter C++ Marks : "))
b=int(input("Enter C Marks : "))
c=int(input("Enter c# Marks : "))
sum=a+b+c
print("______MarkSheet_______")
if(a>= 33 and b>= 33 and c>= 33):
   p=True
   if(sum/3 >= 70 ):
      s = "Destriction"
   elif( sum / 3 >= 60 and sum / 3 <= 69 ):
       s = "frist Class"
   elif (sum / 3 >= 50 and sum / 3 <= 59):
       s = "Second Class"
   elif ( sum / 3 <= 49):
      s = "PassOut"
else:
    p = False
    s ="Looser"
    if(a< 33):
        print("Fali in C++")
    if(b< 33):
        print("Fali in C")
    if(c< 33):
        print("Fali in C#")

print("C++ = ",a)
print("C = ",b)
print("C# = ",c)
print("Total = ",sum)
print("Pracentage = ",sum/3)
if(p==True):
    print("Result Pass")
    print("Grade = ",s)
else:
    print("Result Fails")
    print("Grade = ",s)

print("--13.Found list in number")

v=int(input("enter number :"))
x = [1,2,3,4,5,6,7]
if any([a - v == 1 for a in x]):
    print("Found it!")
else:
    print("Not belog to list number")

print("--14.Found tuple in number")
v=int(input("enter number :"))
x = (1,2,3,4,5,6,7)
if any([a - v == 1 for a in x]):
    print("Found it!")
else:
    print("Not belog to tuple number")


print("--15.Found set in number")
v=int(input("enter number :"))
x = {1,2,3,4,5,6,7}
if any([a - v == 1 for a in x]):
    print("Found it!")
else:
    print("Not belog to set number")
