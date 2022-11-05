#impress your crush using python

# importing the turtle module
import turtle

# Creating an wr object of turtle
wr = turtle.Turtle()

# Setting Color
wr.fillcolor('red')
# Filling the color
wr.begin_fill()

# Start Drawing the Heart
wr.left(140)
wr.forward(113)

# Drawing the carve of heart
for i in range(200):
    wr.right(1)
    wr.forward(1)
wr.left(120)


# Drawing the carve of heart
for i in range(200):
    wr.right(1)
    wr.forward(1)

wr.forward(112)
# Ending the filling color
wr.end_fill()
wr.ht()