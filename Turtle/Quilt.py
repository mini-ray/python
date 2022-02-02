import turtle
import random
from random import randint
from turtle import *

def snowflake():
	t.pencolor("#ADD8E6")
	t.goto(random.randint(-485,-15),random.randint(15,485))
	t.pendown()
	t.rt(90)
	for i in range(6):
		t.fd(10)
		t.bk(10)
		t.rt(60)
	t.penup()
	
def Seth():
	t.fillcolor("purple")
	t.goto(0,0)
	t.width()
	t.begin_fill()
	for i in range(4):
		t.lt(90)
		t.fd(500)
	t.end_fill()
	t.penup()
	for i in range(250):
			snowflake()

def Alex():
	t.fillcolor("#FF69B4")
	t.goto(0,0)
	t.begin_fill()
	t.rt(180)
	for i in range(4):
		t.fd(500)
		t.lt(90)
	t.end_fill()
	
	#t.pencolor("#ff0000")#red
	#t.width(1)
	
	# fill poly start
	t.goto(250,250)
	t.pendown()
	t.pencolor("#00ffff")#cyan
	for i in range (110):
		t.fd(5)
		t.rt(10)
		t.circle(i)

def part( total, length, breadth, col ):
    angleInc = 360/total
    width( breadth )
    color( col )
    for i in range(total):
        forward( length )
        left( angleInc )

def rosette( total, length, width, color, angleInc ):
	for i in range( int(360/angleInc) ):
		part( total, length, width, color )
		left( angleInc )

def rossette():
	t.goto(-250,-250)
	for i in range(36):
		t.pencolor("red")
		for i in range(10):
			t.fd(40)
			t.lt(36)
		t.lt(10)
	for i in range(36):
		t.pencolor("white")
		for i in range(5):
			t.fd(60)
			t.lt(72)
		t.lt(10)

def Levi():
	t.goto(0,0)
	t.pendown()
	#turtle.speed(1)
	t.pencolor("#000000")
	t.fillcolor("#000000")
	t.rt(160)
	t.begin_fill()
	for i in range(4):
		t.fd(500)
		t.lt(90)
	t.end_fill()
	t.goto(-250,-250)
	rossette()
	#rosette(10,40,1,"red",10)
	#rosette(5,80,1,"white",10)




#turtle.setup( 500, 500, 500, 500 ) 
#turtle.speed(50) 


#title("turtle-basics.py")

def Dante():
	t.goto(250,-250)
	t.pencolor("black")
	t.fillcolor("black")
	t.pendown()
	n = 0
	for i in range(13):
		t.fd(100)
		t.begin_fill()
		for i in range(3):
			t.fd(100)
			t.lt(90)
		t.end_fill()
		t.goto(250,-250)
		t.seth(n)
		n = n + 30
	


if __name__ == "__main__":
	screen = turtle.Screen()
	turtle.screensize(1000,1000)
	t = turtle.Turtle()
	turtle.tracer(10, 0)
	Seth()
	t.penup()
	Alex()
	t.penup()
	Levi()
	t.penup()
	Dante()
	
	


	screen.exitonclick()