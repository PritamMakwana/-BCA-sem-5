print('1.set datatype')
s={10,20,30,20,50}
print(s)
ch=set("hello")
print(ch)
nch=set("adminuser")
print(nch)
lst=[1,2,5,4,3]
s=set(lst)
print(s)
s={1,2,5,4,3}
print(s)
s.update([50,60])
print(s)
s.remove(3)
print(s)

print('1.frozenset datatype')
s = {50, 60, 70, 80, 90}
print(s)
fs=frozenset(s)
print(fs)
fs = frozenset("abcdefg")
print(fs)