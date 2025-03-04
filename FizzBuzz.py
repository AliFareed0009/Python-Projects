print("*"*17)
print("Fizz Buzz Project")
print("*"*17)
print("")

range_number = int(input("Enter  number : "))

my_list = []

for num in range(1, range_number+1):

    result=""

    if num % 3 == 0:
        result = result + "Fizz"
        if num % 5 == 0:
            result = result + "Buzz"
    
    elif num % 5 == 0:
        result = result + "Buzz"
    
    else:
        result = num
    
    my_list.append(result)

print(my_list)



