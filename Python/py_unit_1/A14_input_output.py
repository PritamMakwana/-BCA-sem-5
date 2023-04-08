print("---Input---")

print(3*"Hello")
print("city name = " + "goa")
a,b=2,4
print(a)
print(a,b)
print(a,b,sep=",")
print("a value is ", a)
lst=[20,"pritam","Hello"]
print(lst)
print("...formet string...")
print("a = %i b= %d"%(a,b))
name = "KSCPAC"
print("hi %s"%name)
print("hi (%20s)"%name)
print("hi (%-20s)"%name)
print("hi %c ,%c " %(name[0],name[1]))
print("hi %s " %(name[0:2]))
num=123.45678
print("the value is : %f"%num)
print("the value is : %8.2f"%num)
print("example")
n1,n2,n3 = 1,2,3
print("n1 = {0}".format(n1))
print("n1 = {0},n2 = {1} ,n3 = {2}".format(n1,n2,n3))
print("n1 = {0},n2 = {1} ,n3 = {2}".format(n2,n1,n3))
print("n1 = {two},n2 = {one} ,n3 = {three}".format(one=n2,two=n1,three=n3))

name,sal="xyz",15000
print("hello {0} , your salary is {1}".format(name,sal))

print("---Output---")
no1=int(input("Enter any number1 : "))
no2=int(input("Enter any number2 : "))
print("sum is ",no1+no2)
print("subtraction is ",no1-no2)
print("multiplacation is ",no1*no2)
print("division is ",no1/no2)
print("using fomatinng")
print("additon of {} and {} = {}".format(no1,no2,no1+no2))
print("subtraction of {} and {} = {}".format(no1,no2,no1-no2))
print("multiplacation of {} and {} = {}".format(no1,no2,no1*no2))
print("division of {} and {} = {}".format(no1,no2,no1/no2))

print("example decimal convert ")
str=input("enter hexadesimal number : ")
n = int(str,16)
print("hexadesimal {} to deciaml  {} ".format(str,n))
str=input("enter octal number : ")
n1 = int(str,8)
print("hexadesimal {} to octal  {} ".format(str,n1))
str=input("enter binary number : ")
n2 = int(str,2)
print("hexadesimal {} to binary  {} ".format(str,n2))


print("ex three num sum ")
var1,var2,var3=[int(x) for x in input("Enter three numbers(give between ,):").split(",")]
print("sum = ",var1+var2+var3)

print("ex string ")
lst=[x for x in input('Enter strings (give between ,): ').split(',')]
print('you entered:\n',lst)

print("accept a list and display it")
lst=eval(input("Enter a list:"))
print("list = ",lst)

print("Evaluating an expression entered from keyboard")
x=eval(input("Enter an expression:"))
print("result = %d"%x)