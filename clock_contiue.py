import turtle
import datetime
screen = turtle.Screen()
class clock:

    def __init__(self,hour,minute,second):
        self.hour = hour
        self.minute = minute
        self.second = second


    def draw_face(self):
        pen = turtle.Turtle()
        screen = turtle.Screen()
        screen.setup(height=500, width=600)
        screen.bgcolor("cyan")
        pen.speed(100)
        # Draw circle
        pen.pensize(6)
        pen.penup()
        pen.goto(0,-200)
        pen.pendown()
        pen.begin_fill()
        pen.fillcolor("white")
        pen.circle(200)
        pen.end_fill()

        pen.penup()
        pen.goto(0,0)
        pen.pendown()
        # Dot inside
        pen.dot(10)

        # Vẽ đường số - mặt số
        pen.pensize(2)
        for angle in range(0,360,6):
            pen.penup()
            pen.goto(0,0)
            pen.setheading(90-angle)
            pen.forward(160)
            pen.pendown()
            pen.fd(20) # or gọi biến i = 0 pen.write(i+1)

        pen.pensize(4)
        for angle in range(0,360,30):
            pen.penup()
            pen.goto(0,0)
            pen.setheading(90-angle)
            pen.forward(160)
            pen.pendown()
            pen.forward(30)


    def draw_time(self):
        pen = turtle.Turtle()
        pen.clear()
        pen.pensize(6)
        #Draw hour
        pen.penup()
        pen.goto(0,0)
        pen.setheading(90 - self.hour%12*36//12)
        pen.pendown()
        pen.color("black")
        pen.fd(80)

        #draw minute

        pen.penup()
        pen.goto(0, 0)
        pen.setheading(90 - self.minute*6)
        pen.pendown()
        pen.pensize(5)
        pen.fd(120)

        #draw second

        pen.penup()
        pen.goto(0, 0)
        pen.color("red")
        pen.dot(5)
        pen.setheading(90 - self.second * 6)
        pen.pendown()
        pen.pensize(4)
        pen.fd(155)



def run_time():
    global c
    d = datetime.datetime.now()
    c.hour, c.minute, c.second = d.hour, d.minute, d.second
    c.draw_time()
    screen.update()
    turtle.ontimer(run_time, 1000)


d = datetime.datetime.now()
c = clock(d.hour, d.minute, d.second)
c.draw_face()
screen.update()
run_time()








