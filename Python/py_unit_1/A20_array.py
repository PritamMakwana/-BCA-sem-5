# import array
# or
from array import *
print("Array")
print("1.")
a=array('i',[2,4,6,8])
print("the array element are ")
for element in a:
    print(element)

print("2.")
x = array('i',[10,20,30,40,50,60,70])
n = len(x)
print("Lenght = ",n)

y=x[1:4]
print(y)

y=x[0:]
print(y)

y=x[:4]
print(y)

y=x[-4:]
print(y)

y=x[-4:-1]
print(y)

y=x[0:7:2]
print(y)

y=x[0:7:3]
print(y)





