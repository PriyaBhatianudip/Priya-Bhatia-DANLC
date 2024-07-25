class ListMethods:
    def findlength(self, list1):
        listlength = len(list1)

        return listlength

    def addelements(self, list1):
        # create sublist
        sublist = []
        for i in range(int(input("Enter number of elements : "))):
            sublist.append(input("Enter new value : "))
        print("Before adding new elements : ", list1)
        # add this sublist into main list
        list1.extend(sublist)
        print("After adding new elements : ", list1)

# insert() takes two arguments
# insert(index,element)
    def insertnewelement(self, list1):
        index = int(input("Enter index : "))

        # call function to get the length
        length = self.findlength(list1)

        print(length)
        if index >= length:
            print("invalid Index")
        else:
            # print("Enter new value : ")
            # value = int(input())
            # list1.insert(index, value)

            list1.insert(index, int(input("Enter new value : ")))

            print("list : ",list1)
    def deletevalues(self, list1):
        try:
            value = int(input("Enter an existing value : "))
            list1.remove(value)
            print("After removing value : ", list1)
        except ValueError:
            print("Error : Value not found in list!!")
# you need to create an object in order to use a function of a class
#  objectname =classname()

ob1 = ListMethods()
list1 = [43, 498, 90, 3, 48, 43]
# length = ob1.findlength(list1)
# print("Length : ", length)
# ob1.addelements(list1)

# ob1.insertnewelement(list1)

# ob1.deletevalues(list1)
# 1. if we provide the wrong positive index, then insert function will add
# value in the last of list
# 2. if we provide the wrong negative index, then insert function will add
# value in the start(0 index) of the list

# pop function :- value =  pop(), value = pop(index)
# list1.insert(-10,12800)
# print("list1 : ", list1)
# print("Popped value : ",list1.pop())
# print("lsit1 : ", list1)
# print("Popped value at index : ", list1.pop(2))
# print("lsit1 : ", list1)
# print("Popped value at index : ", list1.pop(-4))
# print("lsit1 : ", list1)
# print("Popped value at index : ", list1.pop(22)) # wrong index will generate IndexError
# print("lsit1 : ", list1)

# find the index of a value
# syntax : indexofvalue = listob.index(value)
# value = 0
# try:
#     value = int(input("Enter a value : "))
#     print(f"Index of {value} is {list1.index(value)}")
# except ValueError:
#     print(f"The value {value} does not exists in the list!!")

# print("Count : ",list1.count(list1))
#
# value = int(input("Enter a value : "))
# print(f"Count of {value} is {list1.count(value)}")

# list1.sort()
# print("list after sorting : ", list1)
# list1.sort(reverse=True)
# print("list after sorting : ", list1)

# sorted() will create a new sorted list
newlist = sorted(list1)
print("new list : ",newlist)
print("original list : ",list1)
list1.reverse()

print("Reversed List : ",list1)

list2 = list1.copy()
print("second copy : ",list2)