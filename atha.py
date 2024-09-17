import turtle
import math

# Setup the turtle screen
screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()
t.speed(0)

def draw_circle(radius, color):
    t.penup()
    t.goto(0, -radius)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

draw_circle(100, "yellow")
draw_circle(80, "orange")
draw_circle(60, "brown") 



# Draw green leaves around outer circle

def draw_petal(radius, color):
    t.begin_fill()
    t.fillcolor(color)
    for _ in range(2):
        t.circle(radius, 60)
        t.left(120)
    t.end_fill()

num_petals = 12
radius = 100
for i in range(num_petals):
    angle = i * (360 / num_petals)
    t.penup()
    t.goto(0, 0)
    t.setheading(angle)
    t.forward(radius)
    t.pendown()
    draw_petal(60, "green")


import turtle

def draw_point(t, x, y, color="black"):
    """
    Draw a point at specified location.

    Args:
        t (Turtle): Turtle object.
        x (int): X-coordinate.
        y (int): Y-coordinate.
        color (str): Color of the point.
    """
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(2)  # Draw small circle for point
    t.end_fill()


def main():
    t = turtle.Turtle()
    t.speed(1)

    # Draw points
    points = [
        (-20, 10),
        (-20, 0),
        (20, 0),
        (40, 40),
        (10, 25),
        (25, 25),
        (15, 10)
    ]

    colors = ["black", "black", "black", "black", "black", "black", "black"]

    for i, point in enumerate(points):
        draw_point(t, point[0], point[1], color=colors[i])

    # Connect points
    t.penup()
    t.goto(points[0][0], points[0][1])
    t.pendown()
    t.color("black")  # Set line color
    t.width(2)  # Set line width

    for point in points:
        t.goto(point[0], point[1])

    turtle.done()


if __name__ == "__main__":
    main()
# Draw 2 green palm trees
t.penup()
t.goto(20, 0)
t.pendown()
t.color("green")
t.setheading(90)
t.forward(50)
t.right(45)
t.forward(30)
t.backward(30)
t.left(90)
t.forward(30)

t.penup()
t.goto(20, 0)
t.pendown()
t.color("green")
t.setheading(90)
t.forward(50)
t.right(45)
t.forward(30)
t.backward(30)
t.left(100)
t.forward(30)

turtle.done()
