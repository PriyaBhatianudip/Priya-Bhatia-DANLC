# input basic salary and experience and then if the exp>=20
# then calculate bonus = 25% of salary else bonus = 15% of salary

basic_salary = float(input("Enter Your Basic Salary : "))
exp = int(input("Enter your experience : "))

bonus = 0
if exp >= 20:
    bonus = 0.25 * basic_salary
else:
    bonus = 0.15 * basic_salary

print(f"Your Bonus is : {bonus}")


