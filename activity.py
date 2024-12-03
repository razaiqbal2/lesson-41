import turtle

turtle.Screen().bgcolor("blue")

sc=turtle.Screen()
sc.setup(800,600)

turtle.title("square")
t1=turtle.Turtle()

for i in range(4):
    t1.forward(100)
    t1.right(90)
    i=i+1

turtle.done()    