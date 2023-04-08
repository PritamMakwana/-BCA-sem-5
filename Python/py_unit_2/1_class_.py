class Student:
 def __init__(self):
  self.name="raju"
  self.age=20
  self.marks=88

 def talk(self):
  print("Hi, i am ",self.name)
  print("My age is ",self.age)
  print("My marks are ",self.marks)

s1=Student()
s1.talk()