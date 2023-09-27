#!/usr/bin/python

def tebahpla():
    for i in range(65, 91):
        result = ""
        if i%2== 1:
            result += chr(i).upper()
        if i%2== 0:
            result += chr(i).lower()
        r = result[::-1]
        print(r, end="")

tebahpla()
