list1 = [11,22,44,566,77,899,434]

print("Length : ",len(list1))

# list1.insert(5,"abc")
# print(list1)
# list1.insert(5,"abc1")
# print(list1)
# list1.insert(19,"dddd")
# list1.insert(-19,"dd1")
print(list1)

print("remove : ",list1.remove(44))
print(list1)

print("pop : ", list1.pop(2))
print(list1)

# print("index : ", list1.index(566))

print("find abc", "11abc" in list1)

print("count occurrence of an element : ", list1.count("abc"))

# list1.sort()
# print(list1)
#
# list2 = ["av","55","dfd","XTR","Ae"]
# list2.sort()
# print(list2)
# list1.sort(reverse=True)
print(list1)

list3 = sorted(list1)
print("list 1 : ", list1)
print("List 3 : ", list3)
list3.reverse()
print(list3)