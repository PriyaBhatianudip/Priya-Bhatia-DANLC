# name = input("Enter your full name : ")
#
# if name.startswith("Miss") or name.startswith("Mrs."):
#     print("Female")
# elif name.startswith("Mr."):
#     print("Male")
# else:
#     print("Salutation Not provided")
#
# filename = input("Enter file name with extension : ")
#
# if filename.endswith(".mp3"):
#     print("Audio File")
# elif filename.endswith(".mp4"):
#     print("Video file")
# else:
#     print("Invalid file type!!")
#

ch = input("Enter a character : ")

if ch.isalpha():
    print("alphabet")
elif ch.isnumeric():
    print("Number value")
else:
    print("special character")

if ch >= 'A' and ch <= 'Z':
    print("Capital letter")

# Wap to check the strength of a password
# it will be checked in two levels
#1. check if its length is 6 or not
#2. should contain atleast one capital,small,number and special character
# if password is ok then print password strength is good
# else