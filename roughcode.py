def compareTriplets(a, b):
    diff=list(map(lambda x,y:x-y,a,b))
    bob=0
    alice=0
    print(diff)
    for each in range(len(diff)):
        print(diff[each])
        if  diff[each]>0:
            alice+=1
        elif  diff[each]==0:
            pass
        else :
            bob+=1
    return [alice,bob]

if __name__ == '__main__':

    a = list(map(int, input("Enter  a").rstrip().split()))

    b = list(map(int, input("Enter b").rstrip().split()))

    result = compareTriplets(a, b)
    print(result)

