# A school has following rules for grading system:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A

marks = int(input("Enter Your Marks : "))

if 80 < marks <= 100:
    print("A Grade")
elif 60 < marks <= 80:
    print("B Grade")
elif 50 < marks <= 60:
    print("C Grade")
elif 45 < marks <= 50:
    print("D Grade")
elif 25 < marks <= 45:
    print("E Grade")
elif 0 < marks <= 25:
    print("Fail")
else:
    print("Marks should be between 0 to 100!!")




