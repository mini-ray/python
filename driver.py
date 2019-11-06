import turtle
import turt
#import turt1
import olympicrings

def main():
	w = turtle.Screen()
	w.setup(1500, 1000)
	w.clear()
	w.bgcolor("#ffffff")
	t = turtle.Turtle()
	print("main")
	turt.rainbow(t)
	olympicrings.rings(t)
	w.exitonclick()
	
	
if __name__ == "__main__":
	main()

