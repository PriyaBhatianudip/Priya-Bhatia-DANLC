# dictname = dict()

student_list1 = dict()

student_list = dict(id=101, name ="Ajay kumar", age=18, city="delhi")

print(student_list)

# update() method is used to add new key-value pair into the dictionary

id = 102
name = "Jai kumar"
age = 17
city = "Gurgaon"

student_list.update({"id" : id, "name": name, "age":age, "city":city})
student_list1.update({"id" : id, "name": name, "age":age, "city":city})
# print(student_list)

print("-------------------------------")
# print(student_list1)

print(student_list1["id"])

for s in student_list:
    print(s,student_list[s])
