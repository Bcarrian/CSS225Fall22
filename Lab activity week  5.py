#Brian Carrion
#11/11/2022

#This program print "Hellow world" 100 times
for i in range(100):
    print("Hello world")

#Gives the list of the numbers and its square root
lst = [12, 10, 32, 3, 66, 17, 42, 99, 20]

for x in lst:
    print(x)

for x in lst:
    print(str(x) + " " + str(x ** 2))

#that asks the user for the number of sides, the length of the side,
#The color of the line, and the fill color of a regular polygon
import turtle

s = turtle.Screen()

t = turtle.Turtle()

sides = int(input("Enter the number of sides: "))

length = int(input("Enter the length of the side: "))

col = input("Enter the color of your polygon: ")

t.fillcolor(col)

t.begin_fill()

for x in range(sides):

   t.forward(length)

   t.right(360/sides)

t.end_fill()

s.mainloop()

#Program that shows the numbers that are divisible by 3 or 5 or both.
for num in range(1,51):
    if num % 3 == 0 and num % 5 == 0:
        print("Divisible by both: "+str(num))
    elif num % 3 == 0:
        print("Divisible by 3:" +str(num))
    elif num % 5 == 0:
        print("Divisible by 5:" +str(num))
    else:
        print(num)







