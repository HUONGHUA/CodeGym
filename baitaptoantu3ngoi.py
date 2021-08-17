import turtle

'''shapeInput = input('Circle and square, what is your favorite shape?:')

if shapeInput == 'circle' or shapeInput == 'square':
    colorInput = input('What color will it be?, yellow, red or blue? :')

    if colorInput == 'yellow' or colorInput == 'red' or colorInput == 'blue':
        wn = turtle.Screen()
        wn.bgcolor("black")
        wn.title("Your shape")

        displayShape = turtle.Turtle()
        displayShape.shape(shapeInput)
        displayShape.color(colorInput)

        turtle.done()

    else:
        print("Sorry, I don't have this color :(")
else:
    print("Sorry, I don't have this shape :(")
'''
'''import random
number = random.uniform(0,3)
intNumber = int(number)
h = turtle.Screen()
h.bgcolor("black")
h.title("circle")

ball = turtle.Turtle()
ball.shape("circle")

if intNumber <1:
    ball.color("green")
elif intNumber <2:
    ball.color("red")
elif intNumber < 3:
    ball.color("yellow")
turtle.done()
'''
import math
msg =int(input("Vui long nhap vô số nguyên ?"))
if msg%2 == 0: print("%.0f là số chẳn"%msg)
else: print("%.0f là số lẻ "%msg)
