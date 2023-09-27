#!/usr/bin/python3
import random

number = str(random.randint(-1000, 1000))

numbers = int(number)

val = int(number[-1])

if numbers < 0:
    if val != 0:
        print(f"Last digit of {numbers} is -{val} and is less than 6 and not 0") 
    else:
        print(f"Last digit of {numbers} is {val} and is less than 6 and not 0") 

elif val == 0:
    print(f"Last digit of {numbers} is {val} ")
elif val < 5:
    print(f"Last digit of {numbers} is {val} and is less than 6 and not 0")  
elif val == 5:
    print(f"Last digit of {numbers} is {val} and is less than 6")
elif val > 5:
    print(f"Last digit of {numbers} is {val} and is greater than 5 ")  
