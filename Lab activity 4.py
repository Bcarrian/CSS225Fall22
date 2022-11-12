print("Welcome to the program")

first_number = int(input("Please enter the first number:"))
second_number = int(input("Please enter the second number:"))

answer = input("Would you like the Sum or the Product of the two numbers:")
if answer == "Sum":
    print(first_number + second_number)
elif answer == "Product":
    print(first_number*second_number)
else:
    print("Invalid option, good bye bozo!")






