import turtle


screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor("white")
screen.title("터틀로 라이언 그리기")

t = turtle.Turtle()
t.speed(0)
t.pensize(3)


def set_fill(color):
    t.fillcolor(color)
    t.pencolor("black")


def draw_circle(x, y, radius, color):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    set_fill(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()


def draw_face():
    t.penup()
    t.goto(0, -180)
    t.setheading(0)
    t.pendown()
    set_fill("#D89B5B")
    t.begin_fill()

    for _ in range(2):
        t.circle(180, 90)
        t.circle(220, 90)

    t.end_fill()


def draw_ears():
    draw_circle(-120, 180, 55, "#D89B5B")
    draw_circle(120, 180, 55, "#D89B5B")


def draw_eyes():
    draw_circle(-55, 40, 10, "black")
    draw_circle(55, 40, 10, "black")


def draw_nose():
    t.penup()
    t.goto(0, 5)
    t.setheading(-90)
    t.pendown()
    set_fill("black")
    t.begin_fill()
    t.circle(18, steps=6)
    t.end_fill()


def draw_mouth():
    t.penup()
    t.goto(-35, -20)
    t.setheading(-60)
    t.pendown()
    t.circle(40, 120)

    t.penup()
    t.goto(35, -20)
    t.setheading(240)
    t.pendown()
    t.circle(40, 120)


def draw_eyebrows():
    t.penup()
    t.goto(-85, 80)
    t.setheading(10)
    t.pendown()
    t.forward(55)

    t.penup()
    t.goto(30, 88)
    t.setheading(-10)
    t.pendown()
    t.forward(55)


draw_ears()
draw_face()
draw_eyes()
draw_nose()
draw_mouth()
draw_eyebrows()

t.hideturtle()
turtle.done()