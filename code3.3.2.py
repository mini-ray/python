r = int(input("Enter the red: "))
g = int(input("Enter the green: "))
b = int(input("Enter the blue: "))

if(r >= 0 and r <= 255 and g >= 0 and g <= 255 and b >= 0 and b <= 255):
	print("Input accepted")
else:
	if(r < 0 or r >255):
		print("Red number is not correct.")
	if(g < 0 or g > 255):
		print("Green number is not correct.")
	if(b < 0 or b > 255):
		print("Blue number is not correct.")
