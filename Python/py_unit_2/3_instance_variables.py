#instance vars example
class Sample:
 #this is a constuctor
 def __init__(self):
  self.x=10
 #this is an instance method
 def modify(self):
  self.x+=1


     
#create 2 instances
s1=Sample()
s2=Sample()
print("x in s1=",s1.x)
print("x in s2=",s2.x)
#modify x in s1
s1.modify()
print("x in s1=",s1.x)
print("x in s2=",s2.x)