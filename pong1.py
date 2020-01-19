import turtle
import winsound


wn = turtle.Screen()
wn.title("Pong by @RomanStavinsky")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#scor
score_a = 0
score_b = 0


#Paddle A


paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=3,stretch_len=2)
paddle_a.penup()
paddle_a.goto(-350, 0)
#pADDLE B

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("blue")
paddle_b.shapesize(stretch_wid=3,stretch_len=2)
paddle_b.penup()
paddle_b.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = 0.1

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("player RED: 0 Player BLUE: 0", align="center", font=("Courier", 24, "normal"))

#Function
def paddle_a_up():
        y = paddle_a.ycor()
        y += 10
        paddle_a.sety(y)

def paddle_a_down():
        y = paddle_a.ycor()
        y -= 10
        paddle_a.sety(y)

def paddle_b_up():
        y = paddle_b.ycor()
        y += 10
        paddle_b.sety(y)

def paddle_b_down():
        y = paddle_b.ycor()
        y -= 10
        paddle_b.sety(y)


# KeyBoard binding

wn.listen()
wn.onkeypress(paddle_a_up,"1")
wn.onkeypress(paddle_a_down,"2")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")

#main game loop
while True:
    wn.update()

    #move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if paddle_a.ycor() >290:
        paddle_a.sety(280)

    if paddle_a.ycor() <-290:
        paddle_a.sety(-280)

    if paddle_b.ycor() >290:
        paddle_b.sety(280)

    if paddle_b.ycor() <-290:
        paddle_b.sety(-280)    

     
    

    #Border cheking
    if ball.ycor() >290:
        ball.sety(290)
        ball.dy*= -1
        # winsound.PlaySound("bounce.mp3", winsound.SND_ASYNC)
        ball.speed(+1)



    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy*= -1
        ball.speed(1)
        ball.speed(+1)
        


    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx*= -1
        score_a += 1
        pen.clear()
        pen.write("player RED: {} Player BLUE: {}".format(score_a,score_b), align="center", font=("Courier", 24, "normal"))
        winsound.PlaySound("bounce.mp3", winsound.SND_ASYNC)


    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx*= -1
        score_b += 1
        pen.clear()
        pen.write("player RED: {} Player BLUE: {}".format(score_a,score_b), align="center", font=("Courier", 24, "normal"))
        winsound.PlaySound("bounce.mp3", winsound.SND_ASYNC)



#paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 110 and ball.ycor() > paddle_b.ycor()):
        ball.setx(330)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 110 and ball.ycor() > paddle_a.ycor()):
        ball.setx(-330)
        ball.dx *= -1


 