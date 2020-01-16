import random
import string
import datetime

def getTimeString():
	x = datetime.datetime.now()
	y = x.year -2000
	timestring = str(y) + str(x.month) + str(x.day) + "-" + str(x.hour) + str(x.minute) + ".txt"
	print(timestring)
	return timestring

def randomString(stringLength=65536):
    """Generate a random string of fixed length """
    letters = string.ascii_uppercase
    return ''.join(random.choice(letters) for i in range(stringLength))

print (randomString() )
y = randomString()
tsfilename = getTimeString()
f = open(tsfilename,"w+")
for i in range(10):
     f.write(randomString())
f.close() 
