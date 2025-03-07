def add(num1, num2):
    return num1 + num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def sub(num1, num2):
    return num1 - num2

math_operations = {
    "+": add,
    "-": sub,
    "/": divide,
    "*": multiply
}

# Get the values from the users
def calculator():
    should_continue = True
    num1 = int(input('Enter the first number: '))

    while should_continue:
        num2 = int(input('Enter the next number: '))
        for ops in math_operations:
            print(ops)
        math_operations_input = input('Select the operation: ') 
        operation_function = math_operations[math_operations_input]
        answer = operation_function(num1, num2)
        print(f'Result of {num1} {math_operations_input} {num2} is {answer}')
        if input(f'Continue the operation with {answer}? y/n: ') == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()