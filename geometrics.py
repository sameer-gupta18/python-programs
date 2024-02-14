import math
sum=0
while True:
    multiplier=input("Please enter the multiplier ratio: ")
    if(multiplier.isdigit()):
        multiplier=float(multiplier)
        break
    else:
        print("Please try again")
    break
while True:
    no_of_terms=input("Please enter the number of terms: ")
    if(no_of_terms.isdigit()):
        no_of_terms=int(no_of_terms)
        break
    else:
        print("Please try again")

while True:
    a=input("Please enter the starting term: ")
    if(a.isdigit()):
        a=float(a)
        break
    else:
        print("Please try again")

terms=[0 for _ in range(no_of_terms)]
terms[0] = a
sum=a
for i in range(1, no_of_terms):
    terms[i] = multiplier * terms[i-1]
    sum+=terms[i]

print(f'The geometric sequence is: {terms}')
print(f'The sum of all terms is {sum}')
