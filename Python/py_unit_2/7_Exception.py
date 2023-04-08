# 1.
# try:
#  x=int(input("Enter number1:"))
#  y=int(input("Enter number2:"))
#  print(x/y)
# except ZeroDivisionError:
#  print("Can not divide zero")

# 2
# try:
#     f = open("myfile", "w")
#     a, b = [int(x) for x in input("Enter two numbers: ").split()]
#     c = a / b
#     f.write("Writing %d into myfile" %c )
# except ZeroDivisionError:
#     print("Division by zero happened")
#     print("please do not enter 0 in input")
# finally:
#     f.close()
#     print("File closed")

#3
# try:
#  date=eval(input("Enter date: "))
# except SyntaxError:
#  print("Invalid date entered")
# else:
#  print("You entered: ",date)

# Enter date: 2016,10,3
# You entered:  (2016, 10, 3)

# 4.assert statement
# try:
#  x=int(input("Enter a number between 5 and 10: "))
#  assert x>=5 and x<=10
#  print("The number entered:",x)
# except AssertionError:
#  print("The condition is not fulfilled")