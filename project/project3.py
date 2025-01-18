# hexagon
import turtle

turtle.Screen().bgcolor("blue")

sc=turtle.Screen()
sc.setup(800,600)

turtle.title("hexagon")
t1=turtle.Turtle()

t1.hideturtle()

for i in range(6):
    t1.forward(89)
    t1.left(-59)
    t1.forward(i)
    i=i+1

turtle.done()    
