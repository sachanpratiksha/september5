inp_str=input("Please enter the string").capitalize()
a=inp_str.split(' ')
print(a)
b= a[::-1]
result=' '.join(b)
print(result)