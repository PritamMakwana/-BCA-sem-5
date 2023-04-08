print('ex1')
e = [10,20,0,40,15]
x = bytearray(e)
print(x)
for i in x:
    print(i)

#byte array change value
print('ex2')
print(x[0])
x[0] = 100
print(x[0])