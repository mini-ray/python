import turtle
import random
import time


def SetUp():
	t1.penup()
	t2.penup()
	t3.penup()
	t4.penup()
	
	t1.goto(300,0)
	t2.goto(300,0)
	t3.goto(300,0)
	t4.goto(300,0)
	
	t1.pendown()
	t2.pendown()
	t3.pendown()
	t4.pendown()
	
	t1.width(5)
	t2.width(5)
	t3.width(5)
	t4.width(5)
	
	t1.lt(90)
	t2.lt(90)
	t3.lt(90)
	t4.lt(90)
	
	for i in range(270):
		t2.fd(5)
		t2.lt(1)
	
	for i in range(180):
		t3.fd(5)
		t3.lt(1)
	
	for i in range(90):
		t4.fd(5)
		t4.lt(1)
		
		
def circles(n):
	n = 0
	while(n <= 2500):
		t1.fd(5)
		t2.fd(5)
		t3.fd(5)
		t4.fd(5)
		t1.lt(1)
		t2.lt(1)
		t3.lt(1)
		t4.lt(1)
		n = n + 1
		


if __name__ == "__main__":
	screen = turtle.Screen()
	turtle.screensize(1000,1000)
	screen.bgcolor("black")

	#t1 = turtle.Turtle()
	#t1.shape('turtle')
	#t1.color('red')

	#t2 = turtle.Turtle()
	#t2.shape('turtle')
	#t2.color('blue')
	
	#t3 = turtle.Turtle()
	#t3.shape('turtle')
	#t3.color('green')
	
	#t4 = turtle.Turtle()
	#t4.shape('turtle')
	#t4.color('yellow')
	
	#drawTrack(p,2)
	turtle.tracer(1,0)
	n = 0
	
	for i in range(100):
		t1 = turtle.Turtle()
		t1.shape('turtle')
		t1.color('red')

		t2 = turtle.Turtle()
		t2.shape('turtle')
		t2.color('blue')
	
		t3 = turtle.Turtle()
		t3.shape('turtle')
		t3.color('green')
	
		t4 = turtle.Turtle()
		t4.shape('turtle')
		t4.color('yellow')
		SetUp()
		for j in range(1):
			circles(n)
		#screen.bgcolor("white")
		turtle.reset()
		t1.reset()
		t2.reset()
		t3.reset()
		t4.reset()
		#SetUp()
		n = 0


wn.exitonclick()