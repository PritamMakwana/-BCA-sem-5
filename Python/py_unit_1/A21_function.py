print("Function")

print("1.--")
def add(x,y):
    return x+y
def sub(a,b):
    print("the sub = ",a-b)
def even_odd(num):
    if num % 2 == 0:
        print(num," is even ")
    else:
        print(num ,"is odd")
def Factorial(n):
        f=1
        for i in range(1,n+1):
            f=f*i
            print("Factorial of ", i, " is ", f)
def prime(n):
     c=0
     for i in range(1,n+1):
         if n%i==0:
             c+=1
     if c==2:
         print(n," is a prime number")
     else:
         print(n," is Not a Prime number ")

def primeShow(n):
     for a in range(2,n+1):
         c=0
         k=0
         for i  in range(2,a//2+1):
             if(a%i==0):
                 k=k+1

         if(k<=0):
            print(a,end=" ")
     print()
def listGet(lst):
    lst.append(9)
    print(lst)
    print(id(lst))

print("--1.simple function")
sub(100,200)
print("--2.return function")
print("sum = ",add(10,20))
print("--3.function using check old even number")
even_odd(10)
even_odd(13)
print("--4.Factorial Number")
Factorial(10)
print("--6.Prime Number")
prime(11)
print("--6.Raqnge Prime  Number")
primeShow(10)
print("--7.List pass in function")
l = [1,2,3,4]
listGet(l)
print(id(l))

