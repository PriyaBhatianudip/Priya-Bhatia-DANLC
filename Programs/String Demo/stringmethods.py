# upper and lower : coverts a string into upper or lower case
# syntax : stringvar.upper()  stringvar.lower()

str1 = "HELLO"
str2 = "delhi"

r1 = str1.lower()
r2 = str2.upper()

print(r1,r2)
print(str1.lower())

name = input("Enter your name : ")
print(name)
print(len(name))
n1 = name.strip()

print(n1," \t length : ", len(n1))
n2 = name.lstrip()
print(n2," \t length : ", len(n2))
n3 = name.rstrip()
print(n3," \t length : ", len(n3))


