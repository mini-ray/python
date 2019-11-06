import turtle

def arcR(t,x,y,l,tn,h):
	#x, y, l (length) tn(turn value)
	t.down()
	t.seth(h)
	for i in range (1,10):
			t.forward(l)
			t.rt(tn)
		



def circle(t):
	print("circle")
	t.down()
	t.color("#ff0000")
	for i in range (0,10):
		t.forward(10)
		t.rt(36)



def square(t,x,y):
	t.goto(x,y)
	t.penup()
	t.begin_fill()
	tcolor = "#0000ff"
	t.color(tcolor)
	t.forward(100)
	t.rt(90)
	t.forward(90)
	t.rt(90)
	t.forward(80)
	t.rt(90)
	t.forward(70)
	t.end_fill()

def rainbow(t):
    x = -400; y = 0
    t.speed(0)
    t.penup()
    t.goto(-545,-200)
    t.goto(-600,-200)
    t.pendown()
    t.begin_fill()
    t.goto(-600,-200)
    tcolor = "#800080";t.color(tcolor)
    arcR(t,x,y,75,11.25,90)
    tcolor = "#800080";t.color(tcolor)
    arcR(t,x,y,75,11.25,0)
    t.end_fill()
    
    t.penup()
    t.begin_fill()
    t.goto(-545,-200)
    tcolor = "#0000ff";t.color(tcolor)
    arcR(t,x,y,65,11.25,90)
    tcolor = "#0000ff";t.color(tcolor)
    arcR(t,x,y,65,11.25,0)
    t.end_fill()
    
    t.penup()
    t.begin_fill()
    t.goto(-485,-200)
    tcolor = "#00ff00";t.color(tcolor)
    arcR(t,x,y,55,11.25,90)
    tcolor = "#00ff00";t.color(tcolor)
    arcR(t,x,y,55,11.25,0)
    t.end_fill()
    
    t.penup()
    t.begin_fill()
    t.goto(-425,-200)
    tcolor = "#ffff00";t.color(tcolor)
    arcR(t,x,y,45,11.25,90)
    tcolor = "#ffff00";t.color(tcolor)
    arcR(t,x,y,45,11.25,0)
    t.end_fill()
    
    t.penup()
    t.begin_fill()
    t.goto(-365,-200)
    tcolor = "#ffa500";t.color(tcolor)
    arcR(t,x,y,35,11.25,90)
    tcolor = "#ffa500";t.color(tcolor)
    arcR(t,x,y,35,11.25,0)
    t.end_fill()
    
    t.penup()
    t.begin_fill()
    t.goto(-305,-200)
    tcolor = "#ff0000";t.color(tcolor)
    arcR(t,x,y,25,11.25,90)
    tcolor = "#ff0000";t.color(tcolor)
    arcR(t,x,y,25,11.25,0)
    t.end_fill()
    
    t.penup()
    t.begin_fill()
    t.goto(-245,-200)
    tcolor = "#ffffff";t.color(tcolor)
    arcR(t,x,y,15,11.25,90)
    tcolor = "#ffffff";t.color(tcolor)
    arcR(t,x,y,15,11.25,0)
    t.end_fill()
    
    t.goto(-200,-200)
    
    '''t.speed(10)
    t.color("#000000")
    t.forward(50)
    square(t,x,y)
    circle(t)
'''	


if __name__ == '__main__':
	x = -400; y = 0
	w = turtle.Screen()
	w.setup(1500, 1000)
	w.clear()
	w.bgcolor("#ffffff")
	t = turtle.Turtle()
	rainbow(t)
	w.exitonclick()
