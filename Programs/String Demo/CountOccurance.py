# Write a Python program to count the occurrences of each word in a
# given sentence

str1 = input("Enter a string : ")
searchstring = input("Enter a character or word to check its occurrences : ")

#  str1 = Kiran is going to the market for buying vegetables.
#  She will also go to the temple on the way
# searchstring = t

# count number of occurrences of a character
count = 0
for i in str1:
    if i == searchstring:
        count += 1

print("Number of Occurrences : ", count)

# count number of occurrences of a word
word = input("Enter a word : ")
str2  = str1.split()
count = 0
for s in str2:
    if s == word:
        count += 1
print("No of Occurrences of word : ", count)


# String = “Deeptech Python Training”
# String1 = "hcetpeeD nohtyP gniniarT"




