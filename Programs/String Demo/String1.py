name = "Pooja Malhotra"
city = 'delhi'

print(name,"\n",city)
print(city[0:3])
print(city[1])

print(city[-2])

print(city[-1])
print(city[::-1])

for i in range(len(city)-1,-1,-1):  # i = 5-1=4   i>-1
    print(city[i],end="")