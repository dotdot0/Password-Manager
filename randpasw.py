
import random

def passwGen():
    mainStr = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789[]()}{!@#$%&*/'

    n = int(input('length of password: '))
    password = ''

    for i in range(0, n + 1):
        t = random.randint(0,len(mainStr))
        
        password = password + mainStr[t]

    return password
