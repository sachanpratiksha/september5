# import string
# import random
# def generatepass(length):
#     character=string.ascii_uppercase+string.ascii_lowercase+string.digits+string.punctuation
#     return ''.join(random.choice(character) for i in range(length)
#
#
# result=generatepass(9)
# print result
import random
import string

# get random string password with letters, digits, and symbols
def get_random_password_string(length):
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_characters) for i in range(length))
    print("Random string password is:", password)

get_random_password_string(11)
get_random_password_string(10)