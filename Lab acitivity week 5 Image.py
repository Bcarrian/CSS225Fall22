#Brian Carrion
#11/11/2022

#draws Image of a triangle
from turtle import *
import turtle
turtle.bgcolor("black")
color('red', 'orange')
begin_fill()
while True:
    forward(100)
    left(120)
    if abs(pos()) < 1:
        break
end_fill()
turtle.done()