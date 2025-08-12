import turtle

# Set up the screen with background color
screen = turtle.Screen()
screen.bgcolor("lightblue")  # Change background color here

# Create a turtle object
t = turtle.Turtle()
t.pensize(3)     # Pen thickness
t.pencolor("black")
t.fillcolor("yellow")  # Fill color for the square

# Draw a filled square
t.begin_fill()
for _ in range(4):
    t.forward(100)
    t.right(90)
t.end_fill()

# Finish
turtle.done()
