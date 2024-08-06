studentdata = []

student = dict.fromkeys(["sno","name","course"])

print(student)
n = int(input("Enter number of student records : "))

for i in range(1, n+1):
    student.update({"sno": i})
    student.update({"name": input("Enter name : ")})
    student.update({"course": input("Enter course name : ")})
    studentdata.append(student)

print(studentdata)
