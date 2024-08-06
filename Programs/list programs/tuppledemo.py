#1 create tuple manually

t1 = (12, "kk", 78.393 ,22 ,"3kkd")

# create tuple from list
list1 = ["jj","dd","dde","kk","ddd"]
t2 = tuple(list1)

# create tuple from string
str1 = "hello how are you"
t3 = tuple(str1)

print(t1)
print(t2)
print(t3)
print("values using index : ", t1[3])
print("Values using slicing : ", t1[1:4])
print("Values using negative index : ",t1[-2])
print("values from slicing : ", t1[0:5:2])
print("negative slicing : ", t1[-1:-4:-1])

for x in t2:
    print(x)