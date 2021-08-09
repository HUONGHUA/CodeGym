# coding utf-8
import turtle
h = turtle.Turtle()
turtle.speed(10)
turtle.bgcolor('white')
h.pensize(5)
h.penup()
h.goto(-500,0)
h.pendown()
for i in range(2):
	h.fd(400)
	h.lt(90)
	h.fd(200)
	h.lt(90)
h.pensize(2)
for t in range(2):
	h.lt(90)
	h.fd(150)
	h.lt(90)
	h.fd(100)

h.penup()
h.goto(-550,0)
h.pendown()

for g in range(3):
	h.lt(90)
	h.fd(170)
	h.lt(90)
	h.fd(20)
h.fd(30)
h.lt(180)
h.fillcolor('green')
h.begin_fill()
for t in range(3):
	h.fd(80)
	h.lt(120)
h.end_fill()
for t in range(2):
	h.fd(80)
	h.lt(120)
h.rt(60)
h.fd(40)
h.lt(180)
h.fillcolor('green')
h.begin_fill()
for t in range(3):
	h.fd(80)
	h.lt(120)
h.end_fill()
for t in range(2):
	h.fd(80)
	h.lt(120)
h.penup()
h.goto(-500,150)
h.pendown()
h.rt(60)
for i in range(5):
	h.fillcolor('green')
	h.begin_fill()
	for i in range(3):
		h.fd(15)
		h.right(120)
	h.end_fill()
	h.fd(20)
h.lt(90)
for i in range(7):
	h.fillcolor('green')
	h.begin_fill()
	for i in range(3):
		h.fd(15)
		h.right(120)
	h.end_fill()
	h.fd(20)

h.penup()
h.goto(-500,0)
h.pendown()
h.lt(90)
h.fillcolor('white')
h.begin_fill()
for t in range(2):
	h.lt(90)
	h.fd(150)
	h.lt(90)
	h.fd(100)
h.end_fill()

h.fillcolor('#551122')
h.begin_fill()
for t in range(2):
	h.fd(400)
	h.rt(90)
	h.fd(20)
	h.rt(90)
h.end_fill()
h.pensize(2)
h.penup()
h.goto(-490,200)
h.pendown()
for i in range(2):
	h.fd(370)
	h.lt(90)
	h.fd(15)
	h.lt(90)
h.penup()
h.goto(-470,200)
h.pendown()
for i in range(2):
	h.fd(200)
	h.lt(90)
	h.fd(100)
	h.lt(90)
h.penup()
h.goto(-470,300)
h.pendown()
for i in range(10):
	h.fillcolor('green')
	h.begin_fill()
	for i in range(3):
		h.fd(15)
		h.right(120)
	h.end_fill()
	h.fd(20)
h.penup()
h.goto(-470,300)
h.pendown()
h.rt(90)
for i in range(5):
	h.fillcolor('green')
	h.begin_fill()
	for i in range(3):
		h.fd(15)
		h.right(120)
	h.end_fill()
	h.fd(20)

h.penup()
h.goto(-170,200)
h.pendown()
h.lt(180) # Chỉnh hướngs sang góc thêm 90 dựng cái dù
h.fd(70)
h.lt(90)
h.fd(70)
h.rt(180)
h.fillcolor('blue')
h.begin_fill()
for i in range(3):
	h.fd(140)
	h.lt(120)
h.end_fill()

h.penup()
h.goto(-270,0)
h.pendown()

h.lt(180)
h.rt(90)
h.fillcolor('pink')
h.begin_fill()
for i in range(2):
	h.fd(170)
	h.lt(90)
	h.fd(80)
	h.lt(90)
h.end_fill()

h.penup()
h.goto(-270,0)
h.pendown()

# Gốc cửa sổ 
h.penup()
h.goto(-400,70)
h.pendown()

h.fillcolor('red')
h.begin_fill()
for i in range(2):
	h.fd(70)
	h.lt(90)
	h.fd(55)
	h.lt(90)
h.end_fill()
h.penup()
h.goto(-155,70)
h.pendown()
h.fillcolor('red')
h.begin_fill()
for i in range(2):
	h.fd(70)
	h.lt(90)
	h.fd(55)
	h.lt(90)
h.end_fill()


#Vẽ măt trời

h.penup()
h.goto(100,270)
h.pendown()
h.fillcolor('yellow')
h.begin_fill()
h.circle(60)
h.end_fill()
h.rt(90)
h.fd(35)


h.penup()
h.goto(-20,270)
h.pendown()
h.lt(180)
h.fd(35)


h.penup()
h.goto(40,210)
h.pendown()
h.lt(90)
h.fd(35)


h.penup()
h.goto(40,330)
h.pendown()
h.lt(180)
h.fd(35)



















turtle.done()
