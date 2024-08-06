# Reverse each word in a string
# input :-  Deeptech Python Training
# Output :- hcetpeeD nohtyP gniniarT

# input
str1 = input("Enter a string : ")
# split string
str = str1.split()

str2 = ""   # declare a blank string variable

# start loop to access each word
for word in str:
    # print(word)
    str2 += word[::-1]+" "
print(str2)

# now reverse each word and place it back in result string
