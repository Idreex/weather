#!/usr/bin/python3

for a in range(10):
    for b in range(10):
        if a >= b:
            continue 
        print("{}{}, " .format(a, b),end="")
    
