message = ""
while message != "q":

    number_1 = int(input("Enter the first number : "))
    number_2 = int(input("Enter the second number : "))

    print("")
    print("+ - Addition")
    print("- - Subtraction")
    print("/ - Division")
    print("* - Multiplication")
    print("quit - quit the program")
    print("")

    symbol = input("Select a operation : ")
    
    if symbol == 'quit':
        message = 'q'

    elif symbol == "+":
        result = number_1 + number_2
        print(f"Result of {number_1} + {number_2} is {result}")
        print("")

    elif symbol == "-":
        result = number_1 - number_2
        print(f"Result of {number_1} - {number_2} is {result}")
        print("")

    elif symbol == "/":
        result = print(f"Result of {number_1} / {number_2} is {result}")
        print("")

    elif symbol == "*":
        result = print(f"Result of {number_1} * {number_2} is {result}")
        print("")

    else:
        print("Please select a operation")
        print("")