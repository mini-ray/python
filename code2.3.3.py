h1 = int(input("Enter the hour: "))
m1 = int(input("Enter the minute: "))
m2 = int(m1 % 60)
m3 = int(m2 + 15)
h2 = int(m1 / 60)
h3 = int(h1 + h2)
print("Hours: " + str(h3))
print("Minutes: " + str(m3))
