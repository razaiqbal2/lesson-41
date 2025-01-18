# tringle
import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("hotpink")

# Create a turtle object
turtle.title("triangle")
t = turtle.Turtle()

# Set turtle speed
t.speed(3)

# Draw a right-angled triangle
t.forward(150)    # Base of the triangle
t.left(90)        # Turn to 90 degrees to make the right angle
t.forward(150)    # Height of the triangle
t.left(135)       # Turn to 135 degrees to close the triangle
t.forward(213)    # Hypotenuse

# Hide the turtle after drawing
t.hideturtle()

# Close the turtle graphics window when clicked
turtle.done()   
