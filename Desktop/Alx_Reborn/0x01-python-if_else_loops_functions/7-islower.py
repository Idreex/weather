#!/usr/bin/python3

def isupper(c:str) -> bool:
    if ord(c) >= 65 and ord(c) <= 90:
        return True
    return False

def islower(c: str) -> bool:
    if ord(c) >=97 and ord(c) <= 122:
        return True
    return False

def islower2(c:str) -> bool:
    if c in "abcdefghijklmnopqrstuvwxyz":
        return True
    return False


print("a is {}" .format("lower" if islower("a") else "upper"))
print("H is {}" .format("lower" if islower("H") else "upper"))
print("A is {}" .format("lower" if islower("A") else "upper"))
print("3 is {}" .format("lower" if islower("3") else "upper"))
print("g is {}" .format("lower" if islower("g") else "upper"))