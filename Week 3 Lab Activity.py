#Brian Carrion
#10/21/2022

#This program simply prints the word "Hello World'
print("Hello world")


#Print your name into the input.
Your_name = input("What is your name?:")
#A message will be received with a greeting!
print("Hello", Your_name, "is very nice too meet you!")

#Asks for user name.
username = input("What is your name?:")
user1 = "Brian"
user2 = "Mr.tovar"
#Program will reject any name except the user's name or teacher's name.
if username == user1:
    print("Hello,", user1, "is very nice too meet you!")
elif username == user2:
    print("Hello", user2, "how are you doing today?")
else:
    print("Who are you imposter?")

#A program that will find the area of the circle once user inserts radius.
PI = 3.14
r = float(input("Enter the radius of a circle:"))
area = PI * r * r
print("Area of a circle = %.2f" %area)
#Program will then print message with answer.
print("Very good you got", area, "for your answer!")


# Get miles driven from the user
miles_driven = float(input("Enter miles driven: "))

# Get gallons used from the user
gallons_used = float(input("Enter gallons used: "))

miles_per_gallon = miles_driven / gallons_used
#Program will print a message along with the answer provide in a nice message.
print("Miles per gallon:", miles_per_gallon)
print("A you can see you use", miles_per_gallon, "miles per gallon.")


#Python program to convert Fahrenheit to Celsius

print("Enter Temperature in Fahrenheit: ")
fah = float(input())
cel = (fah-32)/1.8
print("\nEquivalent Temperature in Celsius: ", cel)

#Get start day from user, convert to int, assign to a variable
vacationStart=int(input('What day does your vacation start? (Enter 0 for Sunday, 1 for monday, 2 for tuesday, 3 for wednsday, 4 for thursday, 5 for friday, 6 for saturday.) '))

#Get length of vacation from user, convert to int, assign to a variable
vacationLength=int(input('How many days will your vacation be? '))

#Take the vacation length add to the vacation start
#Use modulus operator to get the remainder of the reaminder of this value divided by 7(for 7 days of week)
returnDay=(vacationLength+vacationStart)%7

print(returnDay)

















