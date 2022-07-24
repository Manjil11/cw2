import random
import pickle
import sys

info={}
print(info)

print("Hello,welcome")

#with open("Doc2.docx","br") as readfile:
# info =pickel.load(readfiles)
question=input("Do you want to generate the password [yes/no]: ")
if question =="yes" or question=="YES":
    print("Processing success")
else:
    print("You are not allowed")
    sys.exit()

s="abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*()-^?"

len_password = int(input("Enter a length of a password: "))
password ="".join (random.sample(s,len_password))
print(password)
answer = input ("Would you like to keep this password [yes/no]: ")
if answer =="yes" or answer=="YES" or answer=="Yes":
    account_name=input("Enter account name: "":")
    info[account_name]=password
    
elif answer=="no" or answer=="No" or answer=="NO":
    print("Password not saved!!")
else:
    print("Wrong option")

    with open ("game.p","bw") as filewrite:
        pickle.dump(info, filewrite,protocol=2)
