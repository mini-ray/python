import turtle
import random
from random import randint
import time
def teardrop():
	t.pencolor("#000000")
	t.fillcolor("#ADD8E6")
	turtle.tracer(50, 0)
	for i in range(75):
		t.penup()
		t.goto(random.randint(-400,400),random.randint(-400,400))
		t.width(3)
		t.pendown()
		t.begin_fill()
		t.fd(38)
		for i in range(14):
			t.lt(15)
			t.fd(4)
		t.lt(15)
		t.fd(38)
		t.lt(135)
		t.end_fill()
		t.penup()
	
def blood():
	t.pencolor("#000000")
	t.fillcolor("red")
	turtle.tracer(0, 0)
	t.goto(random.randint(-400,400),random.randint(-400,400))
	t.width(3)
	t.pendown()
	t.begin_fill()
	t.fd(38)
	for i in range(14):
		t.lt(15)
		t.fd(4)
	t.lt(15)
	t.fd(38)
	t.lt(135)
	t.end_fill()
	t.penup()
	
def clear():
	t.goto(-500,-500)
	turtle.tracer(10, 0)
	t.width(1)
	t.pencolor("black")
	t.fillcolor("white")
	t.pendown()
	t.seth(0)
	t.begin_fill()
	for i in range(4):
		t.fd(1000)
		t.lt(90)
	t.end_fill()
	t.penup()

def Frame():
	for i in range(500):
			teardrop()
		#time.sleep(2)
			#blood()
	clear()

if __name__ == "__main__":
	screen = turtle.Screen()
	t = turtle.Turtle()
	#turtle.screensize(1000,1000)
	t.penup()
	n = 0
	while(n == 0):
		#Frame()
		t.rt(115)
		teardrop()
		#clear()
		t.reset()

	screen.exitonclick()