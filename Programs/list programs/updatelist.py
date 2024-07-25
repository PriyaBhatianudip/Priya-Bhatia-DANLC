list1 = []

n = int(input("Enter number of elements : "))

for i in range(0,n):
    list1.append(input("Enter new value : "))

# print elements of list one by one
print("elements of list : ")
for i in range(0,n):
    print(list1[i])

print("elements of list : ")
for i in list1:
    print(i)
# Q Wap to search an element in a list and replace it with another element.
# Both the values should be entered by user at runtime