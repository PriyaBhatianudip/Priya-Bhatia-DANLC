def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def multi(a, b):
    return a * b


def div(a, b):
    return a / b


def modulus(a,b=1):
    return a % b


print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")

choice = int(input("Enter your choice : "))
if 1 <= choice <= 5:
    print("Enter two numbers : ")
    a = int(input())
    b = int(input())

if choice == 1:
    print(f"Sum : {add(a, b)}")
    # sum = add(a,b)
    # print("Sum : ",add(a,b))
elif choice == 2:
    print(f"Difference  : {sub(a, b)}")
elif choice == 3:
    print(f"Product  : {multi(a, b)}")
elif choice == 4:
    print(f"Division  : {div(a,b)}")
elif choice == 5:
    print(f"Remainder  : {modulus(a, b)}")
    print(f"Remainder  : {modulus(a)}")
else:
    print("Invalid choice!!")
