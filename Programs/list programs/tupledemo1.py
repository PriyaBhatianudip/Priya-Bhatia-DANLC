t1 = ()
t2 = ("aaa",33,34.44,"dbb",44,442)
list1 = ["hh","dd","de","gf",333,422]
t3 = tuple(list1)
s1 = "hello how are you"
t4 = tuple(s1)
d1 = {1: 34, 2: "dd", 3: 44}

t5 = tuple(d1.items())
t6 = tuple(d1)
print("t1 : ", t1)
print("t2 : ", t2)
print("t3 : ", t3)
print("t4 : ", t4)
print("t5 : ", t5)
print("t6 : ", t6)

a = (44)
b = (45,)

print(a)
print(b)

print("value at index 4 : ", t3[4])
print("last index value : ", t3[-1])
print("Slicing from 1 to 4 : ", t3[1:5])
print("Slicing from 0 to 79: ", t3[0:79:2])
print("negative range : ", t3[-1:-4:-1])
print("negative range : ", t3[::-1])
print("range : ", t3[:4])
print("range : ", t3[2:])

