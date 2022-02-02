import turtle
import random
import time




#user input function

#p = float(input('please insert the perimeter:'))

#set the track
def drawTrack(p,r):
    shortside = (p/2.0)/(r+1)
    longside = r*shortside
    turtle.setup((shortside*2)+60, longside +40)
    t.penup()
    t2.penup()
    t.setposition(-shortside-10, -longside/2)
    t2.setposition(10, -longside/2)   
    for i in range (2):
        #first track
        t.speed(1)
        t.pendown()
        t.forward(shortside)
        t.left(90)
        t.forward(longside)
        t.left(90)

        #second track
        t2.speed(1)
        t2.pendown()
        t2.forward(shortside)
        t2.left(90)
        t2.forward(longside)
        t2.left(90) 
        
def circles():
	t1.penup()
	t2.penup()
	t1.goto(300,0)
	t2.goto(300,0)
	t1.pendown()
	t2.pendown()
	t1.width(5)
	t2.width(5)
	t1.lt(90)
	t2.lt(90)
	for i in range(36):
		t2.fd(20)
		t2.lt(5)
	
	#t1.fd(100)
	#t2.fd(100)
	while(n == 0):
		t1.fd(20)
		t2.fd(20)
		t1.lt(5)
		t2.lt(5)


if __name__ == "__main__":
	wn = turtle.Screen()
	turtle.screensize(1000,1000)
	wn.bgcolor("black")

	t1 = turtle.Turtle()
	t1.shape('turtle')
	t1.color('red')

	t2 = turtle.Turtle()
	t2.shape('turtle')
	t2.color('blue')
	#drawTrack(p,2)
	turtle.tracer(1,5)
	n = 0
	circles()


wn.exitonclick()