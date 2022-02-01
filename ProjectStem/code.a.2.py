A = int(input("Enter side A: "))
B = int(input("Enter side B: "))
C = int(input("Enter side C: "))
D = int(input("Enter side D: "))
E = int(input("Enter side E: "))

import math

Area = (A * B)
h = (A - C)
l = (D - B)
s = ((l - E) * (h))
Area = (Area + s)
t = ((h * E)/2)
Area = (Area + t)

print("Room Area: " + str(float(Area)))
