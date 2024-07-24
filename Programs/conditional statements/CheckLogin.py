# input user id and password from user and
# check whether it matches the userid and password which we
# already have

userid = "abc@gmail.com"
userpass = "ABC#123"

uid = input("Enter userid ")

if uid == userid:
    pass1 = input("Enter password")
    if userpass == pass1:
        print("Login Successful!!")
    else:
        print("Invalid Password!!")
else:
    print("User id is incorrect!!")


