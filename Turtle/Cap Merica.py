import turtle

def shield():
	for i in range(36):
		t.pencolor("red")
		for i in range(10):
			t.fd(40)
			t.lt(36)
		t.lt(10)
	for i in range(36):
		t.pencolor("blue")
		for i in range(5):
			t.fd(60)
			t.lt(72)
		t.lt(10)
	for i in range(36):
		t.pencolor("red")
		for i in range(5):
			t.fd(40)
			t.lt(72)
		t.lt(10)

def star():
	t.pencolor("white")
	t.fillcolor("white")
	t.lt(90)
	t.fd(10)
	t.rt(90)
	t.bk(25)
	t.begin_fill()
	for i in range(5):
		t.fd(50)
		t.rt(144)
	t.end_fill()
	t.fd(20)
	t.begin_fill()
	for i in range(5):
		t.fd(12)
		t.rt(72)
	t.end_fill()
	

if __name__ == "__main__":
	screen = turtle.Screen()
	turtle.screensize(1000,1000)
	t = turtle.Turtle()
	turtle.tracer(10, 0)
	turtle.Screen().bgcolor("#000000")
	shield()
	star()

	screen.exitonclick()