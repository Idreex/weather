#!/usr/bin/python3

def last_digit(num) -> int:
    val = str(num)
    num = int(val[-1])
    print(num)

r = last_digit(34)
print(r)
