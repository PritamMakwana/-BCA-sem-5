print("___for loop Logic progems___")

print("--1.Prime Number")
c=0
n=int(input("Enter a number : "))

for i in range(1,n+1):
    if n%i==0:
        c+=1
if c==2:
    print(n," is a prime number")
else:
    print(n," is Not a Prime number ")

print("--2.Factorial Number")
f=1
n=int(input("Enter a number : "))
for i in range(1,n+1):
    f=f*i
print("Factorial of ",n, " is ",f)

print("--3.Fibonacci Series")
a=0
b=1
n=int(input("Enter n for how many times generate series : "))
print("Fibonacci Series")
print(" ",a," ",b,end=" ")
for i in range(n):
    c=a+b
    a=b
    b=c
    print(" ",c,end=" ")

print("--4.Factorial ")
n = int (input("Enter a number : "))
for i in range(1,n+1):
    cn=i
    fact =1
    for j in range(1,cn+1):
        fact=fact*j
    print(cn," : ",fact)

print("--5.List print ")
languages = ['Swift', 'Python', 'Go', 'JavaScript']

for language in languages:
    print(language)

print("___for loop pattern progems___")
print("\n--1.\n")
n = 5
for i in range(1, n+1):
    print("*" * i)

print("\n--2.\n")
size = 5
for i in range(1, size+1):
    print(" " * (size - i) + "*" * i)

print("\n--3.\n")
n = 5
for i in range(n):
    print('*' * (n - i))

print("\n--4.\n")
size = 5
for i in range(size):
    for j in range(size):
        if i == 0 or i == size - 1 or j == 0 or j == size - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()

print("\n--5.\n")
n = 6
for i in range(1, n+1):
    for j in range(i):
        if j == 0 or j == i-1:
            print('*', end='')
        else:
            if i != n:
                print(' ', end='')
            else:
                print('*', end='')
    print()
