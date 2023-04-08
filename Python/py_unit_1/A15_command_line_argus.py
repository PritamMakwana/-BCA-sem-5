print("command line argrument")
import sys
import math

print("ex1")
print("first argrs only program name " ,sys.argv[0])
sum=int(sys.argv[1])+int(sys.argv[2])
print("{} + {} = {}" .format(sys.argv[1],sys.argv[2],sum))

print("ex2")
args=sys.argv[1:]
print(args)
sum=0
for a in args:
    x=int(a)
    if x%2==0:
        sum+=x
print('sum of evens args = ',sum)

print("ex3 Area ")
print("round = {}".format(sys.argv[1]))
area=math.pi*int(sys.argv[1])**2
print("Area of circle = ",area)
print('Area of circle {:0.2f}'.format(area))