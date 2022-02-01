from mcpi.minecraft import Minecraft
import random
import time

mc = Minecraft.create("10.183.3.38",4711)


a = 1

while(a == 1):
	x,y,z = mc.player.getPos()
	y = 63
	mc.setBlock(x,y,z, 12)
	time.sleep(1)
