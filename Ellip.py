import turtle
h = turtle.Turtle()
scree = turtle.Screen()
h.speed(100)
turtle.bgcolor("white")
turtle.speed(100)
turtle.shape('turtle')
j=0
colr = ['yellow','red','blue','green','orange','violet']
inde = 0
while j<30:
    def ellip(r):
        i=0
        while i<2:
            h.circle(r,90)
            h.circle(r/2,90)
            i +=1
    ellip(90)
    j +=1
    h.color(colr[inde])
    if inde==5:
        inde = 0
    else:
        inde +=1
    h.right(10)
turtle.hideturtle()
turtle.done()


