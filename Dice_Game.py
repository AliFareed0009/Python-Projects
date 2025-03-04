import random

print("*"*10)
print("Dice Game")
print("*"*10)
print("")

while True:
    number = random.randint(1, 6)
    print(f"The Number is {number}")
    try_again = input("\nDo you want to continue : y/n : ")
    if try_again == "n":
        print("Thanks for Playing !")
        break