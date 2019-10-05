#!/usr/bin/python3

'''
 ' Program to Draw a Snowflake
 ' Author: Sanjan Geet Singh <>
'''

from turtle import Turtle # required for turtle(logo) graphics.
t = Turtle()
t.speed(0)
b = 180
for c in range(5):
    a = 9 * c
    for i in range(100):
        t.circle(i, a)
        t.right(b)
        t.circle(i, a)
        t.right(b)
        t.circle(i, a)
        t.right(b)
        t.circle(i, a)
input('Press any key to Continue...')
