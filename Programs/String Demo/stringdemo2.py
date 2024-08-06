fname = "Nitin Kumar"
lname = "Mehra"

print(fname+" "+lname)
name = fname+" "+lname
print(name)

print(fname * 2)
d = fname * 3
print(d)

str3 = "Hello Python. Python is very easy to learn."
s = "Python1"
result = s in str3
print("Result : ", result)

id = int(input("Enter your id : "))
name = input("Enter your name : ")
salary = float(input("Enter salary : "))
# print all of these values using the old formatting style
print("Employee Id : %d"%(id))
print("Id : %d \t Name : %s \t Salary : %f"%(id, name, salary))
print("Id : {} \t Name : {} \t Salary : {}".format(id, name, salary))

