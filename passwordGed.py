from random import randint



def GeneratePassword(max, sep):
    password = ""
    for i in range(0, max):
        password += chr(randint(65,122))
        if i % 5==0:
             password += sep
    return password

pass1 = GeneratePassword(4,"---")
print(pass1)
