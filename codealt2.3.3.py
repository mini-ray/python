hour = int(input("Enter the hour: "))
minute = int(input("Enter the minute: "))

totalminutes = (60*hour) + minute
totalminutes = totalminutes + 15

newhour = int(totalminutes / 60)
if newhour > 12:
		newhour = newhour % 12
newminute = totalminutes % 60

print("Hours: " + str(newhour))
print("Minutes: " + str(newminute))
