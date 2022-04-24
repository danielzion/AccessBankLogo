# code to draw Access Bank Logo
import turtle

AccessBank = turtle.Turtle()
# set color to orange
AccessBank.color('orange')

def DrawLogo():
    AccessBank.width(5)
    AccessBank.right(135)
    AccessBank.forward(30)
    AccessBank.right(270)
    AccessBank.forward(30)
    AccessBank.right(270)
    AccessBank.forward(30)
    AccessBank.right(-90)
    AccessBank.forward(30)
    AccessBank.penup()
    AccessBank.forward(10)
    AccessBank.pendown()
    AccessBank.right(270)
    AccessBank.forward(40)
    AccessBank.right(270)
    AccessBank.forward(50)
    AccessBank.right(270)
    AccessBank.forward(50)
    AccessBank.right(-90)
    AccessBank.forward(60)
    AccessBank.right(270)
    AccessBank.penup()
    AccessBank.forward(20)
    AccessBank.pendown()
    AccessBank.forward(40)
    AccessBank.right(270)
    AccessBank.forward(70)
    AccessBank.right(270)
    AccessBank.forward(70)
    AccessBank.right(-90)
    AccessBank.forward(90)
        
# calls the function that draws logo
DrawLogo()