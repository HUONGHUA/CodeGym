#coding utf-8
import turtle 
h = turtle.Turtle()
h.speed(10)
screen = turtle.Screen()
h.shape('turtle')
def draw(rad):
	h.circle(rad)
	h.penup()
	h.goto(0,-rad)
	h.pendown()

for i in range(5):
	draw(20+20*i)
turtle.done()
