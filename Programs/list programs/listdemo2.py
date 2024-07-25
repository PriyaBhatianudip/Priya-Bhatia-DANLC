# # access the list elements along with its index
# list1 = [11,22,33,44,55,66,77,88,99,110]
#
# print("index\t: value")
# for index, value in enumerate(list1):
#     print(f"{index}\t: {value}")

# 5. Write a Python program to traverse
# a given list in reverse order, and
# print the elements with the original index.
# Original list: ['red', 'green', 'white', 'black']
# Traverse the said list in reverse order: black white green red

colorlist = ['red', 'green', 'white', 'black']
#              0      1         2         3

print(colorlist[::-1])
print("Normal list : ")
print("index\t: value")
for index, value in enumerate(colorlist):  #  index = 1   value = green
    print(f"{index}\t: {value}")

print("Reversed list: ")
print("index\t: value")
# for index, value in enumerate(reversed(colorlist)):
#     print(f"{index}\t: {value}")


for i in range(len(colorlist)-1, -1,-1):  #  i= 4-1=3-1=2 i>-1  decrement = -1
    print(f"{i}\t: {colorlist[i]}")   # 2   white

