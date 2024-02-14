first_num=int(input("Enter the first number"))
second_num=int(input("Enter the second number"))
if(second_num<=first_num or (second_num-first_num)==1 or (second_num-first_num)==-1):
    print("Error. Second Number is greater than first number")
i=first_num
while(i+1<second_num):
    print(i+1)
    i=i+1