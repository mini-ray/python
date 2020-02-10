from mcpi.minecraft import Minecraft
import mcpi.block as block
import random

mc = Minecraft.create("192.168.7.96",4711)
#"192.168.7.226",4711

x,y,z = mc.player.getPos()

def cacti(mc,x,y,z,total):
	done = 0
	while(done < total):
		h = random.randint(-20,20)
		l = random.randint(-20,20)
		mc.setBlock(x+h,y,z+l,81)
		done = done + 1

n1 = 21
x = x+2
block = block.SANDSTONE.id
mc.setBlocks(x-20,y,z-20,x+20,y+20,z+20,0)

block = 12
mc.setBlocks(x-20,y-1,z-20,x+34,y-4,z+34,block)


def main():
	
	cacti(mc,x,y,z,25)

if __name__ == "__main__":
	main()

block = 24

for i in range(0,11):
	n1 = n1-1
	if i == 9:
		block = 41

	mc.setBlocks(x+i, y+i, z+i, x+n1, y+i, z+n1, block)

block = 24
n2 = 15
x = x+2
z = z-17
for i in range(0,8):
	n2 = n2-1
	#if i == 9:
		#block = 41

	mc.setBlocks(x+i, y+i, z+i, x+n2, y+i, z+n2, block)

n3 = 9
x = x-15
z = z+5
for i in range(0,5):
	n3 = n3-1
	#if i == 9:
		#block = 41

	mc.setBlocks(x+i, y+i, z+i, x+n3, y+i, z+n3, block)

