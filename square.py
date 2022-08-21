import turtle
import math
bob = turtle.Turtle()
print(bob)


def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)


def circle(t, r):
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 1
    length = circumference / n
    polygon(t, n, length)


def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)


def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)


arc(bob, 1, 1)
polygon(bob, 7, 70)
square(bob, 200)
circle(bob, 150)

turtle.mainloop()
