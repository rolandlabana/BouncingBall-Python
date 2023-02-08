#first change after syncing to local mac repo and commiting within visual code studio - just this comment
#import needed libraries   
import turtle
from turtle import *

#Define constants
RIGHT_EDGE= 400
LEFT_EDGE = -400
BOTTOM_EDGE = -400
TOP_EDGE = 400

GRAVITY = .1
DAMPING = .8

#This function will update the location of the ball
def moveBall():
    global xVel, yVel

    #update the postiion of the ball
    x = ball.xcor()
    ball.setx(x + xVel)
        
    y = ball.ycor()
    yVel = yVel - GRAVITY   #only y is impacted by gravity
    ball.sety(y + yVel)

    #Check for collisons and reverse the direction if so
    if (x >= RIGHT_EDGE):
        xVel *= -1
        ball.setx(x + xVel-5)

    if (x <= LEFT_EDGE):
        xVel *= -1
        ball.setx(x + xVel+5)
   
    if (y <= BOTTOM_EDGE):
        yVel *= -1
        yVel = yVel * DAMPING #damping effect
        ball.sety(y + yVel+5)

    if (y >= TOP_EDGE):
        yVel *= -1
        ball.sety(y + yVel-5)

    

#Global variables
screen = Screen()
screen.title("My window")
screen.bgcolor("green")

ball = Turtle()
ball.clear()
ball.penup()

ball.shape("circle")
ball.color("blue")
ball.position()
ball.speed(0)
ball.sety(0)
ball.setheading(20)

#Define initial position and speed of the ball
ballX = 0
ballY = 0
xVel = 5
yVel = 3

screen.tracer(0) #turn off auto screen updates to make it faster


while True:
    moveBall()
    screen.update()
   
