import random

if __name__ == "__main__":
    r1=random.choice("0123456789")
    r2 = random.choice("0123456789")
    r3 = random.choice("0123456789")
    r4 = random.choice("0123456789")
    num=r1+r2+r3+r4
    f=int(input("How Many attempts You want"))
    for i in range(f):
        num1=input("Please Enter 4 digit num")
        if (len(num1)!=4)  or (not num.isdigit()):
            print('Not a 4 digit number')
        else:
            n=0
            k=0
            for i in range(3):
                if num[i]==num1[i]:
                    n=n+1
                elif num[i] in list(num1):
                    k=k+1
            if n==4:
                print("Hurray!,you have guessed the number Right.")
            else:
                print(f"{n} cows,{k} bulls")
    else:
        print("You have no attempts!")




