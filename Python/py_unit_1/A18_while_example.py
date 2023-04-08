print("___while loop Logic progems___")

print("--1.Prime Number")
x=2
ch=0
n=int(input("Enter a number : "))
if n<1:
    ch=1

while x<=n /2:
    if n%x==0:
        ch=1
        break
    else:
        x+=1
if ch==0:
    print(n," is a prime number")
else:
    print(n," is Not a Prime number ")

print("--2.Palindrome Number")
n=int(input("Enter a number : "))
temp = n
rev =0
while(n >0):
    d=n%10
    rev=rev*10+d
    n=n//10

if(temp==rev):
    print("The number is palindrome.")
else:
    print("The number is Not palindrome.")

print("--3.CountDown")

countdown = 10

while countdown > 3:
    print ('CountDown = ', countdown)
    countdown = countdown - 1

print("--4.Perfeact Number")
i=1
sum=0
n=int(input("Enter number : "))
while i< n:
    if(n%i==0):
        sum=sum+i
    i+=1
if sum == n:
    print(i," is a perfeact number")
else:
    print(i," is Not a perfeact number")

print("--5.Armstrong Number")
n=int(input("Enter number : "))
t=n
r=0
while (n> 0):
    a=n%10
    r=r+a*a*a
    n=n//10
if r == t:
    print(t," is a Armstrong number")
else:
    print(t," is Not a Armstrong number")


print("___while loop pattern progems___")
print("\n--1.\n")
i = 1
while i <= 5:
    j = 1
    while j <= i:
        print("*", end=" ")
        j += 1
    print()
    i += 1

print("\n--2.\n")
n = 5
i = 1
while i <= n:
    j = n
    while j >= i:
        print("*", end=" ")
        j -= 1
    print()
    i += 1
print("\n--3.\n")
n = 5
k = 1
i = 1
while i <= n:
    j = 1
    while j <= i:
        print("{:3d}".format(k), end=" ")
        j += 1
        k += 1
    print()
    i += 1
print("\n--4.\n")

n = 5
i = 1
while i <= n:
    print(" " * (n - i) + "*" * i,)
    i += 1


print("\n--5.\n")
n=5
i = 5
while i >= 1:

    print(" " * (n - i) + "* " * i)
    i -= 1