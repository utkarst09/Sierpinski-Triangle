from math import sqrt
from turtle import *
from random import randint

def drawPoint(x,y):
    penup()
    goto(x,y)
    pendown()
    colormode(255)
    color(138,0,0)
    dot(5)

def mid(prev_x, prev_y, x, y):
    return ((prev_x+x)/2, (prev_y+y)/2)

side = 500
speed(0)
corner = ((0,side/sqrt(3)), (side/2,-side/(2*sqrt(3))), (-side/2,-side/(2*sqrt(3))))

drawPoint(corner[0][0],corner[0][1])
drawPoint(corner[1][0],corner[1][1])
drawPoint(corner[2][0],corner[2][1])

x,y = 10000, 10000
n = 5000
for i in range(n):
    r = randint(0,2)
    x,y = mid(x,y,corner[r][0],corner[r][1])
    drawPoint(x,y)


done()
