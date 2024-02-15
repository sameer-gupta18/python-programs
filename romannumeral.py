def romanNumeral(num):
    sumarray=[]
    romanarray=[]
    n1=str(num)
    for i in range(len(n1)):
        digit=int(n1[i])*(10**(len(n1)-1-i))
        sumarray.append(digit)
    for j in sumarray:
        if j%1000==0:
            if j/1000<4:
                for _ in range(int(j/1000)):
                    romanarray.append("M")
            else:
                continue
        elif j%100==0:
            if j/100 < 4:
                for e in range(int(j/100)):
                    romanarray.append("C")
            elif j/100 == 4:
                romanarray.append("CD")
            elif j/100==9:
                romanarray.append("CM")
            elif j/100==5:
                romanarray.append("D")
            else:
                romanarray.append("D")
                for r in range(int(j/100 - 5)):
                    romanarray.append("C")
        elif j%10==0:
            if j/10 < 4:
                for f in range(int(j/10)):
                    romanarray.append("X")
            elif j/10 == 4:
                romanarray.append("XL")
            elif j/10 == 9:
                romanarray.append("XC")
            elif j/10 ==5:
                romanarray.append("L")
            else:
                romanarray.append("L")
                for w in range(int(j/10-5)):
                    romanarray.append("X")
        else:
            if j<4:
                for o in range(int(j)):
                    romanarray.append("I")
            elif j==4:
                romanarray.append("IV")
            elif j==9:
                romanarray.append("IX")
            elif j==5:
                romanarray.append("V")
            else:
                romanarray.append("V")
                for p in range(int(j-5)):
                    romanarray.append("I")
    roman=''.join(romanarray)
    return roman
while True:
    x=int(input("Enter the number you wish to convert to Roman numerals (between 1 and 3999): "))
    if x<1 or x>3999:
        print("Please enter a number within the range")
    else:
        break
print(romanNumeral(x))