# # CREATE A LIST
# id_list = [101, 102, 103, 104, 105]
#
# #user defined list
# name_list = []
#
# # n = int(input("Enter number of values : "))
# n = 5
#
# for i in range(n):  #  i =0   i<5
#     name_list.append(input("Enter your name : "))
#
# # traverse individual list
# for x in id_list:    # x = 102
#     print(x)
#
# # another way to traverse
#
# for i in range(len(name_list)):  # i=0 1 i<5
#     print(name_list[i])    # name_list[1]
#
# # to traverse more than one list together
#
# for i in range(len(name_list)):
#     print(f"ID : {id_list[i]}\tName : {name_list[i]}")

list1 = [345, 589, 48, 47.67, 58, 48.448, "abc", 848, 45.58, "nnn"]
#         0 , 1 , 2,  3  , 4,

print(list1[2:6])
# 48,47.67,58,48.448
# 2,  3   , 4,   5

print(list1[4:9:2])
# 58, abc, 45.58

print(list1[2:9:-1])

print(list1[-1:-5:-1])
# reverse order
# negative value in step block means decrement
# positive value in step block means increment
# negative value in range block(start and stop) means negative range
# -1 represents the last value in the list, -2 represents last second and so on
# -5:-1:-1     start=-5  step=-1  increment = -1+-5=-6
# -5:-1:1       start =-5 step=1  decrement = -5 + 1=-4
print(list1[-5:-1:-1])

# list1 = [345,589,48,47.67,58,48.448,"abc",848, 45.58,"nnn"]

print(list1[-3:-1:-2])
# blank
print(list1[-4:1])
# abc to 48
print(list1[:5])
# 345 to 58
print(list1[3::])
# 47.67 to nnn
print(list1[2:-5:-1])
# 48 to 58 / abc
print(list1[::-1])
# reverse / null

# list1 = [345,589,48,47.67,58,48.448,"abc",848, 45.58,"nnn"]

# step1 : input search value from user
s = input("Enter your value : ")
# step2 : search for this value in list by
# comparing it with each element of the list
flag = 0  # 0 means not found, 1 means value found
index = -1
for i in range(len(list1)):
    # if the value matches with any element, then exit the iteration
    # and show message value found
    # print(list1[i], s, list1[i] == s)
    x = str(list1[i])
    # if list1[i].isdigit() :
    #     x = str(list1[i])

    if x == s:
        print("Value is found!")
        flag = 1
        index = i
        # list1[i] = input("Enter New value : ")
        # print("Value replaced successfully")
        break

if flag == 0:
    print("Value not found!!")
else:
    list1[index] = input("Enter new value : ")
    print("Value replaced successfully!!")

# step 3: if value is not found even after the iteration is finished,
# then print value not found
# Step 4 : if the value is found, then insert a new value in
# place of old value
