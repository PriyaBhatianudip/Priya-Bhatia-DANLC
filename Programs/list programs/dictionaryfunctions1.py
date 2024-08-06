data1 = {} # empty dictionary
data2 = {1: "Jai", 2:"Dheeru", 3:"Karan", 4: "Arjun", 5: "Sita", 6: "Geeta"}
data3 = dict({"id": 101, "name" : "Geeta", "Age": 23, "City": "Delhi" })
data4 = {"sno":101, "Name":None, "Age":None}

print(data2)
print(data3)

# items() : to get values one by one
print(data2.items())

str3 = data3.items()
print(str3)

# to print key and its value individually
for key, value in data3.items():
    print("key : "+key+"\tValue : "+str(value))

# copy : creates a new dictionary with the same values
data5 = data2.copy()

print("Data 5 : ", data5)

# clear : will delete all the key value pairs from the dictionary
data5.clear()
print("After clear function data 5 : ",data5)

# get is used to get the value according to the key provided
# dictionaryname.get(key,"false value)
# To get a single value
print("get value from dictionary 2 : ", data2.get(2))
print("get value from dictionary 2 : ", data2.get(22,"Key not found!!"))
# To get multiple values

print("Records from data2")

# returns all the keys
for x in data2:
    print(x, data2.get(x))

# to get all the keys
keys = data3.keys()
print("keys : ", keys)

#to get all the values
value = data3.values()
print("Values :", value)

# to print all the keys one by one
print("Keys : ")
for k in keys:
    print(k)

print("Values ")
for v in data3.values():
    print(v)

# pop() it returns the value from a list according to the key provided.
# if it is not able to find the key, it will print the message provided in default
# if it finds the key then it also removes the value from the dictionary

print("Popped value : ", data3.pop("Age"))
print("Data3 : ", data3)

# pop last key value from the dictionary

# print("last key value pair : ", data3.popitem())
st = data3.popitem()
print(st)
print("Data3 : ", data3)

# update : it is used to add a new dictionary to the existing dictionary
# also it is used to update an existing key-value pair
sub = {"Address": "123 mall road, gurgaon, haryana", "Phone": 9876543210}
data3.update(sub)
data3.update({"hobbies":"read,Swim,write", "qualification":"M. Tech"})
print(data3)
age = 23
state = "Haryana"
data3.update({"Age": age, "State": state,"pin":input("Enter Pin : ") })
print(data3)

# update an existing  value
name = input("Enter updated name : ")
data3.update({"name": name})
print(data3)

# fromkeys: will create a new dictionary by putting only the key values along with a default value(optional)
keys = ["sno","sname","course"]
defaultvalue = "na"
# syntax: dictionaryname = dict.fromkeys(keys, default value)

data6 = dict.fromkeys(keys)
print(data6)