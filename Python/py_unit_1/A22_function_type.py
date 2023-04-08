print("---Function Type---")
print("---Formal and Actual Arguments:--")
def sum(a,b): #a,b are formal arguments
 c=a+b
 print(c)
#call the function
x=10;y=15
sum(x,y) #x,y are actual argument

print("1.Positional Arguments")
def attach(s1,s2):
    s3=s1+s2
    print("total string: "+s3)
attach("new","york")

print("2.Keyword Arguments")
def grocery(item,price):
 print("Item=",item)
 print("Price=",price)
grocery(item="sugar",price=48.50)
grocery(price=88.00,item="Oil")

print("3.Default Arguments")
def grocery(item,price=88.00):
 print("item=%s"%item)
 print("price=%.2f"%price)
grocery(item="sugar",price=48.50)
grocery(item="Oil")

print("4.Variable length Arguments:")

def add(farg,*args):
 print("Formal arguments = ",farg)
 sum=0
 for i in args:
  sum+=i
 print("sum of all numbers= ",(farg+sum))
add(5,10)
add(15,20,25,30)

print("--Local and Global Variables--")
# global variable in a function
a=1 #this is global var
def myfunction():
 b=2 #this is local var
 print("a = ",a) #display global var
 print("b = ",b) #display local var
myfunction()
print(a) #available
# print(b) #error,not available

print("--Recursive Functions--")
def factorial(n):
 if n==0:
  result=1
 else:
  result=n*factorial(n-1)
 return result
for i in range(1,11):
 print("Factorial of {} is {}".format(i,factorial(i)))