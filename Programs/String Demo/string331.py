cities = []

n = int(input("Enter number of cities : "))
i = 0
while i < n:
    x = input("Enter city : ")
    if x not in cities:
        cities.append(x)
    else:
        print("city already exist : ", x)
        i -= 1
    i += 1

print(cities)
newstring = "".join(cities)
print(newstring)
# while entering city names, you need to add only unique city names