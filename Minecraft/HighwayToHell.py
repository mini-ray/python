from mcpi.minecraft import Minecraft
import random

mc = Minecraft.create("10.183.3.38",4711)



x, y, z = mc.player.getPos()

def fire(x,y,z,total):
	mc.setBlocks(x+98,y,z-5, x+110,y,z+5,0)
	done = 0
	while(done < total):
		h = random.randint(98,110)
		l = random.randint(-5,5)
		mc.setBlock(x+h,y,z+l, 87)
		done = done + 1

def road():
	mc.setBlocks(x+a,y-1,z-3, x+a,y-1,z+3, 35,8)
	mc.setBlocks(x+a,y-1,z-2, x+a,y-1,z+2, 35,7)
	mc.setBlock(x+a,y-1,z, 35,4)
	mc.setBlocks(x+a,y,z-3, x+a,y+2,z+3, 0)
	
def hell():
	mc.setBlocks(x+98,y-1,z-5, x+110,y-1,z+5, 87)
	

if __name__ == "__main__":
	hell()
	fire(x,y,z,15)
	a = 0
	for i in range(0,100):
		road()
		a = a + 1
	a = 0
	for i in range(0,25):
		road()
		a= a - 1
	mc.postToChat("HighwayToHell")
