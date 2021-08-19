import turtle
t = turtle.Turtle()
t.hideturtle()
t.pencolor("red")
i = 0
a = int(input("Nhap vao canh cua goc vuong"))
while i < 4:
    t.forward(a)
    t.right(90)
    i +=1
turtle.done()