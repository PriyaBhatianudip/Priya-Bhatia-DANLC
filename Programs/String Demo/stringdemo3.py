fname = "Jai Kumar"
lname = "Sharma"

print(fname+lname)
print(fname+" "+lname)
print(fname,lname)
 # to repeat a string multiple times

str1 = "Hello"
print(str1 * 4)
result = (str1+" ") * 2
print(result)

# to fetch a substring
str2 = "Delhi is the capital of India"
s ="capital1"
result= s in str2
print(result)
exp = 12

print("His name is %s %s. he works very hard. he has %d years of experience"%(fname,lname,exp))
print("His name is {} {}. he works very hard. he has {} years of experience".format(fname,lname,exp))

