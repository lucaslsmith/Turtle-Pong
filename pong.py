import turtle #THE HEART AND SOUL OF THIS PROJECT.
import winsound #AUDIO CAPABILITIES.

window = turtle.Screen() 
window.title ("PONG")
window.bgcolor("black")
window.setup(width=800, height=600) #FIXED DIMENSIONS.
window.tracer(0)

player1_score = 0
player2_score = 0

#CREATE THE P1 PADDLE.
player1_paddle = turtle.Turtle()
player1_paddle.speed(0)
player1_paddle.shape("square")
player1_paddle.color("blue")
player1_paddle.shapesize(stretch_wid=5, stretch_len=1)
player1_paddle.penup()
player1_paddle.goto(-350, 0) #START POSITION.

#CREATE THE P2 PADDLE.
player2_paddle = turtle.Turtle()
player2_paddle.speed(0)
player2_paddle.shape("square")
player2_paddle.color("red")
player2_paddle.shapesize(stretch_wid=5, stretch_len=1)
# player2_paddle.tiltangle(180) TO APPLY ROTATION INCASE OF SHAPE CHANGE.
player2_paddle.penup()
player2_paddle.goto(350, 0) #START POSITION.

ball = turtle.Turtle()
ball.speed(0)
ball.shape("turtle")
ball.color("white")
ball.penup()
ball.goto(0, 0) #START POSITION.
ball.dx = 0.2 #START DIRECTION.
ball.dy = -0.2 #START DIRECTION.

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260) #START POSITION.
pen.write("P1: 0                          P2: 0", align = "center", font = ("Courier", 24, "bold")) #SCOREBOARD DETAILS AND POSITION.



def player1_paddle_up(): #EXECUTES MOVEMENT.
    y = player1_paddle.ycor()
    y += 20
    player1_paddle.sety(y)
    

def player1_paddle_down(): 
    y = player1_paddle.ycor()
    y -= 20
    player1_paddle.sety(y)

def player2_paddle_up(): 
    y = player2_paddle.ycor()
    y += 20
    player2_paddle.sety(y)

def player2_paddle_down(): 
    y = player2_paddle.ycor()
    y -= 20
    player2_paddle.sety(y)

window.listen() #CHECKS FOR USER INPUT AND RUNS THE ASSOCIATED ACTION.
window.onkeypress(player1_paddle_up, "w")
window.onkeypress(player1_paddle_down, "s")
window.onkeypress(player2_paddle_up, "Up")
window.onkeypress(player2_paddle_down, "Down")

while True: #MAIN LOOP. 
    window.update()

    ball.setx(ball.xcor() + ball.dx) #CHECKS FOR X COORDINATE UPDATES.
    ball.sety(ball.ycor() + ball.dy) #CHECKS FOR Y COORDINATE UPDATES. 

    #ALL OF THESE CHECK FOR COLLISION OR GOING OUT OF BOUNDS. 
    if ball.ycor() > 290: 
        ball.sety(290)
        ball.dy *= -1 #CHANGES THE DIRECTION ON IMPACT. THIS APPLIES TO ALL OF THE FOLLOWING IF STATEMENTS.
        winsound.PlaySound("audio/bounce.wav", winsound.SND_ASYNC) #PLAYS A SOUND USING THE WINDSOUND MODULE. THIS APPLIES TO ALL OF THE FOLLOWING IF STATEMENTS.

    if ball.ycor() <- 290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("audio/bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() >400:
        ball.goto(0, 0)
        ball.dx *= -1
        player1_score += 1 #UPDATES THE SCORE.
        pen.clear()
        pen.write("P1: {}                          P2: {}".format(player1_score, player2_score), align = "center", font = ("Courier", 24, "bold")) #UPDATES THE SCOREBOARD DISPLAY.
        winsound.PlaySound("audio/goal.wav", winsound.SND_ASYNC)

    if ball.xcor() <- 400:
        ball.goto(0, 0)
        ball.dx *= -1
        player2_score += 1 #UPDATES THE SCORE.
        pen.clear()
        pen.write("P1: {}                          P2: {}".format(player1_score, player2_score), align = "center", font = ("Courier", 24, "bold")) #UPDATES THE SCOREBOARD DISPLAY.
        winsound.PlaySound("audio/goal.wav", winsound.SND_ASYNC)

    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < player2_paddle.ycor() + 40 and ball.ycor() > player2_paddle.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("audio/bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() < -340 and ball.xcor() >- 350 and (ball.ycor() < player1_paddle.ycor() + 40 and ball.ycor() > player1_paddle.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("audio/bounce.wav", winsound.SND_ASYNC)