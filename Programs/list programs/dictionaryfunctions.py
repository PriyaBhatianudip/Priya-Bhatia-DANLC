
data = {1: "Arun sharma", 2: "Kavita kumari", 3:"Garima", 4:"Jia", 5:"Sarita"}

print(data)

for key, value in data.items():
    print("key : "+str(key), end =" ")
    print("Name: "+value)

# copy : creates a new copy of the existing dictionary with new name
d1 = data.copy()
print("d1 : ", d1)
# clear : to clear all the contents of a dictionary
d1.clear()
print("d1 : ", d1)

# to return a single value
k = int(input("Enter key : "))
print("Name : "+data.get(k, "Key does not exist"))
print("items : ", data.items())
print("Keys : ", data.keys())
print("Values : ", data.values())

keys = data.keys()  # dict_keys([1, 2, 3, 4, 5])
for k in keys:  # k = 1
    print("Name : ", data.get(k, f"This key {k} does not exists "))  #  data.get(k)

print("-------------------------------------")
values= data.values()
for x in values:
    print(x)

# pop will return the last value or will provide the value according to given key  from the
# dictionary. it also deletes that value from the list.
# pop() : it will not work with dictionary but popitem() function will return the last value
# pop(key)
print("pop : "+data.pop(3))
print("pop item : ", data.popitem())
print("After pop function : ", data)

# update function is used to add a new value and update an existing value
# add a new value
d = {11: "Neha", 22: "Varun"}
data.update(d)
print("After adding new value\n", data)
# update existing value
newname = "Sanjay kumar"
k = 1
data.update({k: newname})
print("After updating value \n", data)

data1 = dict.fromkeys({"id","name","age","city"})
print(data1)