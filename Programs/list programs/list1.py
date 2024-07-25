list1 = [34,667,24,848,"abc",83.399,48.584]
# To access an element of this list
try:
    n = int(input("Enter the position to access value : "))
    print(f"Value at {n} position is {list1[n-1]}")
    slice1 = list1[2:5]
    print(slice1)
    slice2 = list1[-3:-1:1]
    print(slice2)
    slice3 = list1[-5:-1:2]
    print(slice3)
    slice4 = list1[-5:-1:-2]
    print(slice4)
    slice5 = list1[1:5:-2]
    print(slice5)
    slice6 = list1[-1:-5:-2]
    print(slice6)
    slice7 = list1[-1:-5:2]
    print(slice7)
    slice8 = list1[-1:5:2]
    print(slice8)
    slice8 = list1[1:-3:2]
    print(slice8)
    print(list1[::])
    print(list1[::-1])
    print(list1[:5:])
    print(list1[3::])

except ValueError as ve:
    print("exception : ",ve)
    print()
