def input_num():
    num=input("Enter the num")
    return num
if __name__=="__main__":
    num1=[]
    for i in range(3):
        num1.append(input_num())
    print(num1)
    num1.sort( )
    print(num1[2])


