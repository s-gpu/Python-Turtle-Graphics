#!/usr/bin/python3

'''
 ' Program to Draw a Fake Circle With Hundred Straight Lines
 ' Author: Sanjan Geet Singh <>
'''

from turtle import penup, goto, pendown # required for turtle(logo) graphics.
from math import sin, cos, pi   # required to calculate sin, cos and pi

r = 200 # radius = 400px
inc = pi/50  # angular increment = 100th of the circle = 2*pi/100 = pi/50
t = 0   # plotting point
n = 1.5 # offset; lies in range 0 and 2pi

for i in range(100):    # there will be 100 chords(straight lines).
    # (x1, y1) is the starting point of the chord.
    x1 = r*sin(t);      y1 = r*cos(t)
    # (x2, y2) is the ending point of the chord.
    x2 = r*sin(t+n);    y2 = r*cos(t+n)

    # display the calculated values to the user along with the line number.
    print("{}: ({}, {}), ({}, {})".format(i+1, x1, y1, x2, y2))

    penup()         # lift pen
    goto(x1, y1)    # go to (x1, y1) point
    pendown()       # drop pen
    goto(x2, y2)    # go to (x2, y2) point

    t += inc    # increment angle

input("Press any key to continue...")
