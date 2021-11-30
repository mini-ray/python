import turtle
import random
from random import randint
# main function
def main():
	
	t.pencolor("#ff0000")#red
	t.fd(50)
	t.lt(45)
	t.pencolor("#00ff00")#green
	t.width(4)
	t.bk(100)
	t.rt(45)
	t.pencolor("#0000ff")#blue
	t.width(10)
	t.goto(0,0)
	#t.penup()

	# fill poly start
	t.goto(100,100)
	t.pendown()
	t.pencolor("#00ffff")#cyan
	t.begin_fill()
	t.fd(100)
	t.rt(90)
	t.fd(100)
	t.rt(90)
	t.fd(100)
	t.rt(90)
	t.fd(100)
	t.end_fill()
	
	#t.penup()
	t.goto(-100,100)
	t.pendown()
	t.pencolor("#ff00ff")#magenta
	t.fillcolor("#ff7f00")#orange
	t.begin_fill()
	t.fd(100)
	t.rt(90)
	t.fd(100)
	t.rt(90)
	t.fd(100)
	t.rt(90)
	t.fd(100)
	t.end_fill()
	t.circle(10)
	t.pencolor("#ffff00")
	t.circle(20)
	t.pendown()
	t.goto(-200,-200)
	t.fillcolor("#00cc7f")
	t.begin_fill()
	t.circle(30)
	t.end_fill()
	
		

def snowflake():
	t.pencolor("#ADD8E6")
	t.goto(random.randint(-500,500),random.randint(-500,500))
	t.pendown()
	t.rt(90)
	for i in range(6):
		t.fd(10)
		t.bk(10)
		t.rt(60)
	t.penup()
	

if __name__ == "__main__":
	screen = turtle.Screen()
	t = turtle.Turtle()
	turtle.tracer(10, 0)
	#main()
	t.penup()
	for i in range(1000):
			snowflake()


	screen.exitonclick()