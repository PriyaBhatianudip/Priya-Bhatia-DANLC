str1 = "Hello"
str2 = "    delhi     "

print(str1.lower())
print(str2.upper())
print("length : ", len(str2))
s1 = str2.lstrip()
print("s1 : ",s1)
print("length : ", len(s1))
s2 = str2.rstrip()
print("s2 : ",s2)
print("length : ", len(s2))
s3 = str2.strip()
print("s3 : ",s3)
print("length : ", len(s3))

str3 = "He is going to play football today."
s4 = str3.replace("football","cricket")
print(s4)

str4 = str3.replace(" ","#")
print(str4)
str5 = str4.split("#")

print(str5)
print("".join(str5))
print("".join(str5))
