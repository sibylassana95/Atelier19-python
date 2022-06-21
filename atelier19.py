# Écrire un programme, qui trace un hexagone (polygone à 6 côtés, angles interne à 120°)
import turtle
from turtle import *
c=2
u=100
for k in range(6):
    forward(c*u)
    left(72)
exitonclick()