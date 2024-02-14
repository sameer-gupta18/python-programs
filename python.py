# Formatted strings
first="John"
last="Smith"
msg=f'{first} [{last}] is a coder'
print(msg)

#Math module
import math
x=2.9
print(f'The ceiling number is: {math.ceil(x)}')
print(f'The floor number is: {math.floor(x)}')

#Practise problem
good_credit=False
price=1000000
if good_credit:
    print(round(0.1*price))
else:
    print(round(0.2*price))

#Reading and storing passwords 

def view():
    with open("passwords.txt","r") as f:
        output=f.readline()
    user,passw=output.split("|")
    print(f'Username: {user}, Password: {passw} \n')

def add():
    username = input("Enter the Username: ")
    password = input("Enter the password: ")
    with open("passwords.txt","a") as f:
        f.write(f'{username}|{password}\n')
    
mode = input("Do you want to view the passwords or add a password (view/add)")
if(mode=="view"):
    view()
elif(mode=="add"):
    add()
else:
    print("Error please try again")