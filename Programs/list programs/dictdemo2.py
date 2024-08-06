emp_list1 = {"id": 101, "Name": "Kiran Singh", "Age": 25}

print("Name : ",emp_list1.get("Name","Invalid Key"))
print("Age : ",emp_list1.get("Age1"))

list2 = emp_list1.items()
print(list2)

print("Keys : ", emp_list1.keys())
print("Values : ", emp_list1.values())

# print("pop : ", emp_list1.popitem())
# print(emp_list1)
#
# print("pop : ", emp_list1.popitem())
# print(emp_list1)

emp_list1.update({"city":"Gurgaon"})
print(emp_list1)

emp_list1.update({"Name": "Sanjay Singh", "Age": 27})
print(emp_list1)

new_list = dict.fromkeys(["Roll_No","Student_Name","Class"])
# emp_list1 = dict.fromkeys(["Roll_No","Student_Name","Class"])
print(new_list)
# print(emp_list1)