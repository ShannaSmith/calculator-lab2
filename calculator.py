"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )
# Replace this with your code
# pseudocode:
# if input_str_list[0] = "q"
# result quit
# while q == False:
# input_string = input("operator and numbers")
# input_string = 'operator_str, exp1, exp2'
#input_str_list = input_string.split(",")  ==> ['operator_str (aka power)', num1, num2']
# if token[0] = 'pow': 
#   print(pow(token[1], token[2]))
input_string = input("Enter your equation -> ")
tokens = input_string.split(' ')
print(tokens)
if len(tokens) == 3:
    for token in tokens:

        num1 = float(int(tokens[1]))
        print(num1)
        num2 = float(int(tokens[2]))
    

    if token[0] == 'q':
        print("Good bye")

    elif tokens[0] == '+':
        print(add(num1, num2)) 
    elif tokens[0] == '-':
        print(subtract(num1, num2))
    elif tokens[0] == '*':
        print(multiply(num1, num2))
    elif tokens[0] == '/':
        print(divide(num1, num2))
    elif tokens[0] == 'pow':
        print(power(num1, num2))
    elif tokens[0] == '%':
        print(mod(num1, num2)) 

if len(tokens) == 2: 
    for token in tokens:
        num1 = float(int(tokens[1]))
        print(num1)
           
    if token[0] == 'q':
        print("Good bye")
    elif tokens[0] == 'square':
        print(square(num1))
    elif tokens[0] == 'cube':
        print(cube(num1))

