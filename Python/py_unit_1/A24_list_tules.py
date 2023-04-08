print("List")
lst=list(range(1,5))
print(lst)
lst.append(9)
print(lst)
lst[1]=8 #update 1st element of lst
print(lst)
lst[1:3]=10,11 #update 1st and 2nd elements of lst
print(lst)
lst.remove(9) #delete 9 from lst
print(lst)
del lst[1] #delete 1st element from lst
print(lst)
lst.reverse()
print(lst)

print("tuples")
#inserting a new element into a tuple
names=('a','b','c','d')
print(names)
#accept new name and position number
lst=[input("Enter a new name:")]
new=tuple(lst)
pos=int(input("Enter position no:"))
#copy from 0th to pos-2 into another tuple names1
names1=names[0:pos-1]
#concatenate new element at pos-1
names1=names1+new
#concatenate the ramaining elements of names from pos-1 till end
names=names1+names[pos-1:]
print(names)