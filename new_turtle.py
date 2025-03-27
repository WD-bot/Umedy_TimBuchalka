# import turtle
# from math import radians, cos

from turtle import *
from math import radians, cos

def square(length: int) -> None:
    """Draws a square of length"""
    inner_forward = forward
    inner_right=right
    for side in range(4):
        inner_forward(length)
        inner_right(90)


def encicrled_square(length: int) -> None:
    """Draws a square of the length  length'
    then encloses it in a cirle"""
    square(length)
    angle = radians(45)
    radius = length * cos(angle)
    right(135)
    circle(radius)
    left(135)
    print(f'Inside function, namespace is: {dir()}')
    print(f'locals: {locals()}')


# encicrled_square(300)
speed('fast')
Screen().tracer(0) #disables turtle animation

for s in range(72):
    encicrled_square(120)
    left(5)

Screen().update() #updates screen
done()
print(dir()) #shows modules functions used "__" is called dunder
g= globals()
print(g['square'])

print(dir(__builtins__))