#!/usr/bin/python3

def uppercase(str) -> str:
    return ''.join([chr(ord(char) -32) for char in str if ord(char) >= 65])
print(uppercase('tayo'))


def uppercase2(str):
    for i in range(0, len(str)):
        x = ord(str[i])
        if x >= 97 and x <= 122:
            x = x-32
        y = chr(x)
        print(y, end='')

def uppercase3(str):
    result = ''
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            result += chr(ord(char) -32)
        else:
            result += char
    print("{:s}".format(result))

print(uppercase3('rear'))
    