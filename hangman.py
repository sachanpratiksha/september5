from random import randint
def randomword():
    with open('sowpods.txt', 'r') as f:
      words = f.readlines()
      index = randint(0, (len(words)-1))
      str1=words[index].strip()
      return str1

def guessletter(str2):
    print("Welcome to the hangman!")
    print(str2)
    list2=list(str2)
    guessed = "_" * (len(str2))
    guessed = list(guessed)
    chance=6
    while True:
        letter=input("Guess!").upper()
        if letter in list2:
            if letter not in guessed:
                p=[i for i,x in enumerate(list2) if x== letter]
                for each in p:
                    guessed[each]=letter
                print(f"You have guessed it right {letter}")
                print(' '.join(guessed))
            else:
                print(f"{letter} letter has been guesed before")
        else:
            chance=chance-1
            print(f"This is Incorrect Guess!, You have {chance} remaining/n")

        if '_' not in guessed:
            print("You won!!")
            # play_again=input("wanna play again!").upper()
            # if play_again=='Y':
            return
            # else:




if __name__=="__main__":
    play_again='Y'
    while play_again!='N':
        word=randomword()
        guessletter(word)
        play_again = input("wanna play again!").upper()



# print(readingfile())

