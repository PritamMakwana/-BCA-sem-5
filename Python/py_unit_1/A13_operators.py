
print("1.Arithmetic operators")
a=13
b=5
print(a+b)
print(a-b)
print(a*b)
print(a%b)
print(a/b)
print(a**b)
print(a//b)

print("2.Assignment operators")
x=20
y=10
z=5
z=x+y
print(z)
z=5
z+=x
print(z)
z=5
z-=x
print(z)
z=5
z*=x
print(z)
z=5
z/=x
print(z)
z=5
z%=x
print(z)
z=5
z**=y
print(z)
z=5
z//=y
print(z)

print("3.Relational operators")
a=1
b=2
print(a>b)
print(a>=b)
print(a<b)
print(a<=b)
print(a==b)
print(a!=b)

print("4.Logical and Boolean operators")
a=True
b=False
c=True

if(a and c):
    print("yes")
else:
    print("no")

if(b or a):
    print("yes")
else:
    print("no")

if(not c):
    print("yes")
else:
    print("no")


print("5.Unary minus operators")
n=10
print(-n)
num=-10
num=-num
print(num)

print("6.Membership operators (in ,not in)")
x=10
list=[10,20,30,40,50]
if(x in list):
 print("10 is present")
else:
 print("10 is not present")

x=100
if(x not in list):
 print("100 is not present")
else:
 print("100 is present")

print("7.identity operators (is ,not is)")
a=2
b=2
c=a+b
print(id(a))
print(id(b))
print(id(c))

if(a is b):
 print("a and b have same identity")
else:
 print("a and b do not have same identity")

if(a is not c):
    print("a and c do not have same identity")
else:
    print("a and b have same identity")
