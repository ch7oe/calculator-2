"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, add_multi, add_cubes)


# while loop for REPL calculator 
while True:
    
    #tokenize user input 
    user_input = input("Enter your equation: ")
    tokens = user_input.split(" ")

    #to quit program 
    if tokens[0] == "q":
        print("program has quit")
        break

    #when not enough inputs
    elif len(tokens) < 2:
        print("not enough inputs")
        continue

    #assigning operator and num1
    operator = tokens[0]
    num1 = tokens[1]

    #assigning num2
    if len(tokens) < 3:
        num2 = "0"
    else:
        num2 = tokens[2]
    
    #assigning num3
    if len(tokens) > 3:
        num3 = tokens[3]


#place to store the return value of the math function that is call
    result = None

    #make sure arithmetic function arguments only take numbers
    if not num1.isdigit() or not num2.isdigit() or not num3.isdigit():
        print("that's not a number -_-")
        continue

    #evaluate first token to determine which prefix notation will execute its correlating function
    elif operator == "+":
        result = add(float(num1), float(num2))

    elif operator == "-":
        result = subtract(float(num1), float(num2))
    
    elif operator == "*":
        result = multiply(float(num1), float(num2))
    
    elif operator == "/":
        result = divide(float(num1), float(num2))
    
    elif operator == "square":
        result = square(float(num1))
    
    elif operator == "cube":
        result = cube(float(num1))

    elif operator == "pow":
        result = power(float(num1), float(num2))
    
    elif operator == "mod":
        result = mod(float(num1), float(num2))
    
    elif operator == "x+":
        result = add_multi(float(num1), float(num2), float(num3))
    
    elif operator == "cubes+":
        result = add_cubes(float(num1), float(num2))
    
    else:
        result = "Enter an operator followed by 2-3 integers"

    print(result)    


    



    
        

