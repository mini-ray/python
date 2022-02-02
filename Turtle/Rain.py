import turtle
import random
from random import randint
def teardrop():
	t.pencolor("#000000")
	t.fillcolor("#ADD8E6")
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
	

if __name__ == "__main__":
	screen = turtle.Screen()
	t = turtle.Turtle()
	turtle.tracer(10, 0)
	t.rt(115)
	t.penup()
	for i in range(500):
			teardrop()


	screen.exitonclick()