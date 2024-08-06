# 3 by 3
#     0     1   2
# 0   11   22   33
# 1   44   55   66
# 2   77   88   99
# rc
# 00 - First element
# 01 - second
# 02 - third
# 10 - fourth
# 11 - fifth
# 12 - sixth
# 3X2X3X3

# one dimension list -> list1 =[]
# Two dimension list -> list1= [[1,2,3],[1,2,3],[1,2,4]]
#  -> list1 =[[],[],[]]

list1= [[1,2,3],[4,5,6],[7,8,9]]
# Traverse : access each data from the matrix
for r in range(0,3):
    for c in range(0,3):
        print(list1[r][c],end="\t")
    print()
print("number of rows : ", len(list1))
print("number of columns in second row : ",len(list1[1]))

list1= [[1],[4,5],[7,8,9]]

# Traverse : access each data from the matrix


for r in range(0, len(list1)):
    for c in range(0,len(list1[r])):
        print(list1[r][c],end="\t")
    print()