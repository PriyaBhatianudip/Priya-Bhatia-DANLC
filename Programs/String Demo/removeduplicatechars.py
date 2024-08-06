str = input("Enter a string : ")

str1 = ""
for ch in str:
    if ch not in str1:
        str1 += ch

print(str1)

# remove all the duplicate words from a string
