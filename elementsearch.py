def ordered_list(list1 ):
    list1.sort()
    return  list1


def numberpresent(order_list):
    num2 = int(input("input the number"))
    if num2 in order_list:
        return True
    else:
        return False


if __name__=="__main__":
    k=[]
    n="Please Enter your choices of num"
    print(n)
    while n!=' ':
        n = input()
        if n=='Exit':
            break
        else :
            k.append((int(n)))
print(k)
order_list=ordered_list((k))
result=numberpresent((order_list))
print(result)


