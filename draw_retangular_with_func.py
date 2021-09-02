import turtle
# import math
# # def draw_circle(r):
# #     pen = turtle.Turtle()
# #     pen.speed(100)
# #     pen.hideturtle()
# #     pen.pencolor("red")
# #     pen.circle(r)
# #     turtle.done()
# # draw_circle(100)
# def area(r):
#     return math.pi * r * r
# s = area(30)
# print("Area of circle with R = {} la: {}".format(30,s))
### Nhập thông số cạnh đầu vào hình chữ nhật :
a = int(input("Please enter width of retanguar : "))
b = int(input("Please enter length of retanguar : "))
clo = input("Please enter color for big retangular: ")
sclo = input("Please enter color for small retangular: ")
def draw_retangular_big():#a la chieu rong , b la chieu dai
    global a,b,clo,pen
    pen.fillcolor(clo)
    pen.begin_fill()
    def draw_s(a,b):
        pen.fillcolor(clo)
        pen.begin_fill()
        for i in range(2):
            pen.fd(a)
            pen.lt(90)
            pen.fd(b)
            pen.lt(90)
        pen.end_fill()
    pen.end_fill()
    draw_s(a,b)
    draw_s(a,b//2)
    draw_s(a // 2, b // 2)
    draw_s(a//2,b)
    draw_s(a // 2, b // 2)
    return a,b,clo
### Vẽ cửa sổ nhỏ
def draw_retangular_small():
    global sclo,pen
    pen.speed(100)
    pen.fillcolor(sclo)
    pen.begin_fill()
    for i in range(2):
        pen.fd(a//9)
        pen.lt(90)
        pen.fd(b//6)
        pen.lt(90)
    pen.end_fill()
    put_pen_home()
    return sclo

# Đặt buôn hàm
def put_pen(m,n):
    pen.penup()
    pen.goto(m,n)
    pen.pendown()
    return m,n
def put_pen_home():
    pen.penup()
    pen.goto(0,0)
    pen.pendown()
## Bắt đầu vẽ
pen = turtle.Turtle()
pen.speed(100)
pen.color("red")
draw_retangular_big()
put_pen(a//5,b//5)
draw_retangular_small()
put_pen(a//5,b//1.5)
draw_retangular_small()
put_pen(a//1.5,b//5)
draw_retangular_small()
put_pen(a//1.5,b//1.5)
draw_retangular_small()
turtle.done()










