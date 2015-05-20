#!/usr/bin/env python3
from turtle import *

curve = [20, 160, 20, 20]
speed("fastest")

for i in range(40):
    forward(100)
    degree = curve[ i % len(curve)]
    right(degree)

input()

