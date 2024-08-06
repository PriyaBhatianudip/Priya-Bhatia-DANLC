str = input("Enter a string : ")

# 1. count vowels
# 2. display vowels
# a e i o u

count = 0
# str =  traverse each character in a string
for ch1 in str:  #  i = t
    ch = ch1.lower()
    if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
        count += 1
        print(ch1)

print("No of vowels ", count)



count = 0
# str =  traverse each character in a string
ac = 0
ec = 0
ic = 0
oc = 0
uc = 0
for ch1 in str:  #  i = t
    ch = ch1.lower()
    if ch == "a":
        ac += 1
    elif ch == "e":
        ec += 1
    elif ch == "i":
        ic += 1
    elif ch == "o":
        oc += 1
    elif ch == "u":
        uc += 1

print(f"a :{ac} \t e : {ec} \t i : {ic} \t o : {oc} \t u : {uc}")

