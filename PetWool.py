from mcpi.minecraft import Minecraft
import random
import time

mc = Minecraft.create("10.183.3.38",4711)




def Wool(a,b,c):
	x, y, z = mc.player.getPos()
	b = random.randint(0,15)
	mc.setBlock(x,y,z, 35,b)
	time.sleep(.25)
	mc.setBlock(x,y,z, 0)

if __name__ == "__main__":
	x, y, z = mc.player.getPos()
	a = 1
	while a == 1:
		Wool(x,y,z)
		time.sleep(.001)
