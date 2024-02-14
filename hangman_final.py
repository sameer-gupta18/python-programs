import operator as op
while True:
    word1=input("PLEASE ENTER THE SELECTED WORD: ").lower()
    word=word1.replace(" ","/")
    if(len(word)==1):
        print("Try again")
    else:
        break
while True:
    max_attempts=input("Please enter the maximum number of wrong guesses allowed: ")
    if max_attempts.isdigit():
        max_attempts=int(max_attempts)
        break
    else:
        print("Enter a valid integer")

characters=[]
for i in word:
    characters.append(i)
word_guess=["_" for i in range(len(characters))]
for k in range(0,len(characters)):
    if(characters[k]=="/"):
        word_guess[k]="/"
wrong=0
while True:
    is_exist=False
    for i in range(len(word_guess)):
        print(word_guess[i].upper(), end=" ")
    guess=input("\nPlease enter your letter guess: ").lower()
    if(len(guess)==1):
        if(guess=="/"):
            continue
        if(op.countOf(word_guess,guess)>0):
            wrong+=1
            print(f'REPEATED VALUE. You have used {wrong}/{max_attempts} wrong guesses \n')
            continue
        for j in range(len(characters)):
            if(guess==characters[j]):
                word_guess[j]=guess
                is_exist=True
            else:
                continue
        if is_exist:
            print(f'{guess.upper()} is one of the correct letters. GOOD JOB!')
        else:
            wrong+=1
            print(f'{guess.upper()} is NOT one of the correct letters. ')
        print(f'You have used {wrong}/{max_attempts} wrong guesses \n')
    else:
        print("Please enter only one letter \n")
    if(wrong>=max_attempts):
        print("YOU LOST!")
        print(f'The word was: {word1.upper()}')
        break;
    if(word_guess==characters):
        print("YOU WIN!!!!")
        print(f'The word was: {word1.upper()}')
        break
