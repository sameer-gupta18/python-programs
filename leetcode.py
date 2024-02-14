def palindrome(s):
    one_letter_palindrome=True
    word=""
    palindromes=[]
    if len(palindrome(s))>1:
        one_letter_palindrome=False
    if len(s)==1:
        return s
    elif one_letter_palindrome:
        return s[0]
    else:
        for i in range(len(s)+1): #0-5
            for j in range(i,len(s)+1): #i-4
                if j>i and s[i:j]==s[i:j][::-1]:
                    palindromes.append(s[i:j])
        print(palindromes)
        # for k in palindromes:
        #     if len(k)>1:

        #         break
        count=0
        for k in palindromes:
            if len(k)>count:
                count=len(k)
                word=k
        return word
# palindrome("qbmhukucteihghldwdobtvgwwnhflpceiwhbkmvxavmqxedfndegztlpjptpdowwavemasyrjxxnhldnloyizyxgqlhejsdylvkpdzllrzoywfkcamhljminikvwwvqlerdilrdgzifojjlgeayprejhaequyhcohoeonagsmfrqhfzllobwjhxdxzadwxiglvzwiqyzlnamqqsastxlojpcsleohgtcuzzrvwzqugyimaqtorkafyebrgmrfmczwiexdzcokbqymnzigifbqzvfzjcjuugdmvegnvkgbmdowpacyspszvgdapklrhlhcmwkwwqatfswmxyfnxkepdotnvwndjrcclvewomyniaefhhcqkefkyovqxyswqpnysafnydbiuanqphfhfbfovxuezlovokrsocdqrqfzbqhntjafzfjisexcdlnjbhwrvnyabjbshqsxnaxhvtmqlfgdumtpeqzyuvmbkvmmdtywquydontkugdayjqewcgtyajofmbpdmykqobcxgqivmpzmhhcqiyleqitojrrsknhwepoxawpsxcbtsvagybnghqnlpcxlnshihcjdjxxjjwyplnemojhodksckmqdvnzewhzzuswzctnlyvyttuhlreynuternbqonlsfuchxtsyhqlvifcxerzqepthwqrsftaquzuxwcmjjulvjrkatlfqshpyjsbaqwawgpabkkjrtchqmriykbdsxwnkpaktrvmxjtfhwpzmieuqevlodtroiulzgbocrtiuvpywtcxvajkpfmaqckgrcmofkxynjxgvxqvkmhdbvumdaprijkjxxvpqnxakiavuwnifvyfolwlekptxbnctjijppickuqhguvtoqfgepcufbiysfljgmfepwyaxusvnsratn")


def reverseInteger(x):
    x1=str(x)
    x_rev=int(x1[::-1])
    if x_rev<((2**31)-1) and x_rev>(-(2**31)):
        return x_rev
    else:
        return 0
    
# print(reverseInteger(342938))

def myAtoi(s):
    s_num=0
    positive=True
    s=s.replace(" ","")
    if "-" in s:
        positive=False
        # s=s.replace("-","")
    # elif "+" in s:
    #     # s=s.replace("+","")
    # else:
        pass
    if(not s[0].isdigit() and s[0]!="-" and s[0]!="+"):
        return 0
    s1=s
    for i in s:
        if (not i.isdigit()):
            if (i=="-" or i=="+") and (s.find(i)==0):
                s=s.replace(i,"")
            else:
                s1=s.replace(s[s.find(i):],"")
                break
        else:
            continue
    if not s1.isdigit():
        return 0
    else:
        s_num=int(s1)
    if not positive:
        s_num*=-1

    if s_num<-(2**31):
        return -(2**31)
    elif s_num>((2**31)-1):
        return (2**31)-1
    else:
        return s_num
print(myAtoi("  -42"))