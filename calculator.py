"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, add_multi, add_cubes)


# Replace this with your code
while True:
    user_input = input("Enter equation: ")
    tokens = user_input.split(" ")

    if tokens[0] == "q":
        print("program has quit")
        break

    elif len(tokens) < 2:
        print("not enough inputs")
        continue

    operator = tokens[0]
    num1 = tokens[1]

    

    
        

