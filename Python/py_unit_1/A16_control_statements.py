print("-----control statement-----")

print("1.if statement")
num=1
if num==1:
    print("num = one")

print("2.if...else statement")
num=2
if num==1:
    print("num = one")
else:
    print("num = not one")

print("3.if...elif...else statement")
a=10
b=30
c=20
if a>b and a>c:
  print("a is biggest")
elif b>a and b>c:
  print("b is biggest")
else:
  print("c is biggest")

print("4.while loop")
x=1
while x<=10:
  print(" ",x,end="")
  x+=1
print("\nEnd")

print("5.for loop")
for i in range(1,11):
  print(i)
print("6.else suite")
print("for with else")
for i in range(0):
  print("Yes ")
else:
  print("No ")

print("while with else")
x=10
while x<= 5:
    print(" ", x, end="")
    x += 1
else:
 print("condition false")

print("7.break statement")
group1=[1,2,3,4,5]
search=int(input("Enter element to search: "))
for element in group1:
 if search==element:
   print("Element found in group1")
   break
else:
 print("Element not found in group")

print("8.continue statement")
group1=[1,2,3,4,5]
search=int(input("Enter element to search: "))
for element in group1:
 if search==element:
  print("Element found in group1")
  continue
else:
  print("Element not found in group")

print("9.pass statement")
num=[1,2,3,-4,-5,-6,-7,8,9]
for i in num:
 if(i>0):
  pass
 else:
  print(i)

print("10.assert statement")

x=int(input('Enter a number greater than 0:'))
try:
  assert(x>0)
  print("u entered : ",x)
except AssertionError:
  print("wrong input entered")

print("11.return statement")
def add(x,y):
    return x+y
print(add(10,20))

