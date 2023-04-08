# class vars or static vars example
class Sample:
    # this is a class var
    x = 10

    # this is a class method
    @classmethod  # this is a decorator
    def modify(cls): #cls must be the first parameter
        cls.x+=1 #cls.x refers to class variable x


#create 2 instances
s1=Sample()
s2=Sample()
print("x in s1=",s1.x)
print("x in s2=",s2.x)
#modify x in s1
s1.modify()
print("x in s1=",s1.x)
print("x in s2=",s2.x)