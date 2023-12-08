import turtle
turtle.Screen().bgcolor('#ADD8E6')
t=turtle.Turtle()
t.pensize(5)
t.speed(3)

def go(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

#Bird Body
t.fillcolor('red')
go(-150,-70)
t.seth(-30)

t.begin_fill()
t.circle(220,130)
t.circle(120,180)
t.circle(-120,110)
t.seth(-50)
t.circle(220,30)
t.end_fill()

#Wing
t.fillcolor('brown')
go(-100,90)
t.seth(160)
t.begin_fill()
t.circle(-25,180)
t.circle(-120,60)
t.circle(-40,60)
t.circle(-120,60)
t.circle(-30,180)
t.seth(180)
t.circle(-50,45)
t.circle(-30,190)
t.end_fill()

#Eye
t.fillcolor('#1c0508')
t.pencolor('#1c0508')
t.pensize(7)
go(60,200)
t.seth(-180)

t.begin_fill()
t.circle(35)
t.end_fill()

t.fillcolor('white')
t.begin_fill()
t.circle(35,180)
t.end_fill()

#Feet
go(-30,-100)
t.seth(-80)
t.pensize(10)
t.circle(-90,40)

go(30,-90)
t.seth(-80)
t.pensize(10)
t.circle(-120,35)

t.color('orange')
go(180,170)
t.seth(15)
t.circle(60,30)
go(180,160)
t.seth(-15)
t.circle(-50,40)

#Sun positioned in the corner
t.penup()
t.goto(-330, 240) 
t.pendown()
t.color('yellow')
t.begin_fill()
t.circle(50)
t.end_fill()

#Clouds
t.penup()
t.goto(-290, 120)
t.color('white')
t.begin_fill()
t.circle(60)
t.end_fill()

t.goto(-340, 120)
t.begin_fill()
t.circle(40)
t.end_fill()

t.goto(-210, 120)
t.begin_fill()
t.circle(40)
t.end_fill()

t.penup()
t.goto(-290, -290)
t.color('white')
t.begin_fill()
t.circle(60)
t.end_fill()

t.goto(-340, -290)
t.begin_fill()
t.circle(40)
t.end_fill()

t.goto(-210, -290)
t.begin_fill()
t.circle(40)
t.end_fill()

t.penup()
t.goto(120, -290)  
t.color('white')
t.begin_fill()
t.circle(60)
t.end_fill()

t.goto(200, -290)  
t.begin_fill()
t.circle(40)
t.end_fill()

t.goto(60, -290)  
t.begin_fill()
t.circle(40)
t.end_fill()

t.hideturtle()
turtle.done()