import turtle
import math

# Set up screen
window = turtle.Screen()
window.bgcolor("black")
window.setup(800, 800)



# Turtle pen configuration
tur = turtle.Turtle()
tur.penup()
tur.speed("fastest")
tur.pensize(1)
tur.hideturtle()

# Set up the turtle
t = turtle.Turtle()
t.pencolor("white")
t.speed(0)

# Define the starting radius
radius = 190

for i in range(150):
    # Draw the smaller circle outwards
    t.circle(radius, 90)
    t.left(90)

    # Reduce the radius for the next iteration (prevents drawing outside)
    radius -= 1.2  # Adjust the reduction factor as needed

    # Draw the smaller circle inwards
    t.circle(radius, 90)
    t.left(18)

# Function to draw a circle with a gradient
def draw_circle(tur, x, y, radius, color):
    tur.penup()
    tur.goto(x, y - radius)
    tur.pendown()
    tur.fillcolor(color)
    tur.begin_fill()
    tur.circle(radius)
    tur.end_fill()

def draw_diamond(tur, x, y, size):
    tur.penup()
    tur.goto(x, y)
    tur.setheading(45)  # Adjust angle for the diamond
    tur.pendown()
    tur.fillcolor("cyan")
    tur.begin_fill()
    for _ in range(4):
        tur.forward(size)
        tur.right(90)
    tur.end_fill()
    tur.setheading(0)

# Use softer and complementary colors
draw_circle(tur, 0, 0, 200, "#FFD700")  # Gold
draw_circle(tur, 0, 0, 150, "#FFA500")  # Orange
draw_circle(tur, 0, 0, 100, "#FF4500")  # Red-orange

# Draw flowers with varying colors and styles
def draw_flower(tur, x, y, size, petal_color, center_color):
    tur.penup()
    tur.goto(x, y)
    tur.pendown()
    
    # Draw petals
    tur.fillcolor(petal_color)
    tur.begin_fill()
    for _ in range(10):
        tur.circle(size)
        tur.right(36)
    tur.end_fill()
    
    # Draw center
    tur.fillcolor(center_color)
    tur.begin_fill()
    tur.circle(size / 3)
    tur.end_fill()

# Adding flowers with different colors around the circles
flower_colors = [("#E9967A", "#800080"), ("#BA55D3", "#9400D3"), ("#48D1CC", "#00CED1")]
for i in range(10):
    angle = i * 36
    x = 200 * math.cos(math.radians(angle))
    y = 200 * math.sin(math.radians(angle))
    draw_flower(tur, x, y, 12, *flower_colors[i % len(flower_colors)])
    
    x = 150 * math.cos(math.radians(angle))
    y = 150 * math.sin(math.radians(angle))
    draw_flower(tur, x, y, 10, *flower_colors[(i + 1) % len(flower_colors)])
    
    x = 100 * math.cos(math.radians(angle))
    y = 100 * math.sin(math.radians(angle))
    draw_flower(tur, x, y, 8, *flower_colors[(i + 2) % len(flower_colors)])


def draw_spiral(tur, x, y, size, color_start, color_end):
    tur.penup()
    tur.goto(x, y)
    tur.pendown()

    for i in range(size):
        # Calculate the color based on the gradient
        color = (
            color_start[0] + (color_end[0] - color_start[0]) * i / size,
            color_start[1] + (color_end[1] - color_start[1]) * i / size,
            color_start[2] + (color_end[2] - color_start[2]) * i / size
        )

        # Set the pen color to the calculated color
        tur.pencolor(color)

        tur.forward(i)
        tur.left(60)

# Create a turtle object
tur = turtle.Turtle()

# Draw 10 spirals with a dark red color gradient
for i in range(10):
    angle = i * 36 + 18
    x = 130 * math.cos(math.radians(angle))
    y = 130 * math.sin(math.radians(angle))
    draw_spiral(tur, x, y, 10, (0.5, 0, 0), (1, 0.2, 0.2))



# Add dots along the outermost circle for embellishment
def draw_dot(tur, x, y, size):
    tur.penup()
    tur.goto(x, y)
    tur.pendown()
    tur.dot(size)

for i in range(20):
    angle = i * 18
    x = 210 * math.cos(math.radians(angle))
    y = 210 * math.sin(math.radians(angle))
    draw_dot(tur, x, y, 10)


# Set up the turtle
turtle.up()
turtle.hideturtle()

# Scale factor (adjust as needed)
scale = 0.15

# Draw the base (brown)
turtle.color("brown")
turtle.fillcolor("brown")
turtle.setpos(-200 * scale, 150 * scale)
turtle.down()
turtle.right(90)
turtle.begin_fill()
turtle.circle(200 * scale, 180)
turtle.left(90)
turtle.forward(400 * scale)
turtle.end_fill()

# Draw the diya (black and yellow)
turtle.up()
turtle.color("black")
turtle.back(200 * scale)
turtle.right(90)
turtle.down()
turtle.forward(50 * scale)
turtle.right(90)
turtle.up()
turtle.color("#e6e854")
turtle.fillcolor("#e6e854")
turtle.begin_fill()
turtle.setpos(-50 * scale, 250 * scale)
turtle.right(90)
turtle.down()
turtle.circle(50 * scale, 180)
turtle.left(30)
turtle.forward(100 * scale)
turtle.left(120)
turtle.forward(100 * scale)
turtle.end_fill()


turtle.done()
