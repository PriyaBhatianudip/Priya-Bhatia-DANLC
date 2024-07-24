# input units from user
units = int(input("Enter units : "))

bill = 0
if units >= 500:
    bill = (units-500) * 8 + 100 * 2.5 + 100 * 1.5 + 100 * 1.2
elif units >= 400:
    bill = (units-400) * 2.5 + 100 * 1.5 + 100 * 1.2
elif units >= 300:
    bill = (units-300) * 1.5 + 100 * 1.2
elif units >= 200:
    bill = (units-200) * 1.2
elif 0 <= units <= 200:
    bill = 0
else:
    bill = 0
    print("Units value should be positive!!")

print("Your Bill is ", bill)



