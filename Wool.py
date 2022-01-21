from mcpi.minecraft import Minecraft
import random
import time

mc = Minecraft.create("10.183.3.2",4711)



x, y, z = mc.player.getPos()

x = x+1

def Wool():
	b = random.randint(0,15)
	mc.setBlock(x,y,z, 35,b)

if __name__ == "__main__":
	a = 1
	#print("a")
	while a == 1:
		#print("b")
		Wool()
		time.sleep(.25)
