# coding utf-8
import math
import turtle
h = turtle.Turtle()
screen = turtle.Screen()

h.speed(10)
screen.bgcolor("lightcyan")
h.color("black")
h.shape("turtle")
h.fillcolor("pink")
h.begin_fill()
# Bien chieu dai ngoi nha
cdai = 400
crong = 250
for i in range(2):
	h.fd(cdai)
	h.lt(90)
	h.fd(crong)
	h.lt(90)
h.end_fill()

h.penup()
h.goto(0,250)
h.pendown()

h.fillcolor("maroon")
h.begin_fill()
for i in range(3):
	h.fd(cdai)
	h.lt(120)
h.end_fill()

h.penup()
h.goto(50,0)
h.pendown()
h.fillcolor("cyan")
h.begin_fill()
for i in range (2):
	h.fd(cdai/4)
	h.lt(90)
	h.fd(crong * 3 /4)
	h.lt(90)
# 
h.end_fill()
h.penup()
h.goto(cdai/3 +50,crong/4)
h.pendown()

# Goi bien Windows

a = 50
h.fillcolor("cyan")
h.begin_fill()
for i in range (4):
	h.fd(a*2)
	h.lt(90)
h.end_fill()
for i in range (4):
	h.fd(a)
	h.lt(90)

for i in range (2):
	h.fd(a)
	h.lt(90)
	h.fd(a*2)
	h.lt(90)

for i in range (2):
	h.fd(a*2)
	h.lt(90)
	h.fd(a)
	h.lt(90)


turtle.done()