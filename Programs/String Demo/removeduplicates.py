# remove duplicates from a string

str = input("Enter a string : ")   #  its raining today. But its very hot also
#split the string into substrings
str1 = str.split()     #  its, raining, today., But, its, very, hot, also,
                      #    0      1         2      3    4   5    6     7

result =""

for word in str1:   #  word =  today
    if word not in result:   # "its" not in result(its raining today. But)  false
        result += word +" "   # result = its raining today. But

print(result)

string1 ="find is used to fetch a substring in a string. it is useful in storing information"
word ="is"
result = string1.find(word)
print(result)
result = string1.find("is",string1.find("is")+1)
print(result)
print("count : ", string1.count("is"))



