print("Dictionaries")

dict={'Name':'xyz','Id':200,'Salary':9080.50}
print("name of employee=",dict['Name'])
print("id number=",dict['Id'])
print("salary=",dict['Salary'])

print("key in dict=",dict.keys()) #display only keys
print("Values in dict=",dict.values()) #display only values
print("items in dict=",dict.items()) #display both key and value pairs as tuple

dict=eval(input("Enter elements in {}: "))
#find the sum of values
s=sum(dict.values())
print("Sum of values in the dictionary: ",s)