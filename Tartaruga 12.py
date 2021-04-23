# -*- coding: utf-8 -*-

import turtle
a = turtle.Screen()
tartaruga = turtle.Turtle()
tartaruga.shape("turtle")
tartaruga.fillcolor("aquamarine")
# Desenha um círculo e dá 3 voltas.
for step in range(0, 90):
    tartaruga.forward(6)
    tartaruga.left(4)
    # A cada 20 passos
    if step % 10 == 0:
        tartaruga.stamp()
a.exitonclick()