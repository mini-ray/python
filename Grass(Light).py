from mcpi.minecraft import Minecraft

mc = Minecraft.create("10.183.3.38",4711)



x, y, z = mc.player.getPos()

x = x+10
z = z-7

mc.setBlocks(x-6,y,z-6, x+21,y+21,z+21, 0)
#mc.setBlocks(x,y,z, x+15,y+15,z+15, 35,12)
mc.setBlocks(x,y,z, x+15,y+15,z+15, 5)
#mc.setBlocks(x,y+13,z, x+15,y+15,z+15, 35,13)
mc.setBlocks(x,y+13,z, x+15,y+15,z+15, 35,5)

#mc.setBlock(x,y+13,z+1, 35,12)
mc.setBlock(x,y+13,z+1, 5)
#mc.setBlock(x+1,y+13,z+15, 35,12)
mc.setBlock(x+1,y+13,z+15, 5)
#mc.setBlock(x+15,y+13,z+14, 35,12)
mc.setBlock(x+15,y+13,z+14, 5)
#mc.setBlock(x+14,y+13,z, 35,12)
mc.setBlock(x+14,y+13,z, 5)

#mc.setBlock(x,y+12,z+4, 35,13)
mc.setBlock(x,y+12,z+4, 35,5)
#mc.setBlock(x+4,y+12,z+15, 35,13)
mc.setBlock(x+4,y+12,z+15, 35,5)
#mc.setBlock(x+15,y+12,z+11, 35,13)
mc.setBlock(x+15,y+12,z+11, 35,5)
#mc.setBlock(x+11,y+12,z, 35,13)
mc.setBlock(x+11,y+12,z, 35,5)

#mc.setBlocks(x,y+13,z+5, x,y+14,z+5, 35,12)
mc.setBlocks(x,y+13,z+5, x,y+14,z+5, 5)
#mc.setBlocks(x+5,y+13,z+15, x+5,y+14,z+15, 35,12)
mc.setBlocks(x+5,y+13,z+15, x+5,y+14,z+15, 5)
#mc.setBlocks(x+15,y+13,z+10, x+15,y+14,z+10, 35,12)
mc.setBlocks(x+15,y+13,z+10, x+15,y+14,z+10, 5)
#mc.setBlocks(x+10,y+13,z, x+10,y+14,z, 35,12)
mc.setBlocks(x+10,y+13,z, x+10,y+14,z, 5)

#mc.setBlock(x,y+13,z+7, 35,12)
mc.setBlock(x,y+13,z+7, 5)
#mc.setBlock(x+7,y+13,z+15, 35,12)
mc.setBlock(x+7,y+13,z+15, 5)
#mc.setBlock(x+15,y+13,z+8, 35,12)
mc.setBlock(x+15,y+13,z+8, 5)
#mc.setBlock(x+8,y+13,z, 35,12)
mc.setBlock(x+8,y+13,z, 5)

#mc.setBlock(x,y+12,z+8, 35,13)
mc.setBlock(x,y+12,z+8, 35,5)
#mc.setBlock(x+8,y+12,z+15, 35,13)
mc.setBlock(x+8,y+12,z+15, 35,5)
#mc.setBlock(x+15,y+12,z+7, 35,13)
mc.setBlock(x+15,y+12,z+7, 35,5)
#mc.setBlock(x+7,y+12,z, 35,13)
mc.setBlock(x+7,y+12,z, 35,5)

#mc.setBlock(x,y+12,z+10, 35,13)
mc.setBlock(x,y+12,z+10, 35,5)
#mc.setBlock(x+10,y+12,z+15, 35,13)
mc.setBlock(x+10,y+12,z+15, 35,5)
#mc.setBlock(x+15,y+12,z+5, 35,13)
mc.setBlock(x+15,y+12,z+5, 35,5)
#mc.setBlock(x+5,y+12,z, 35,13)
mc.setBlock(x+5,y+12,z, 35,5)

#mc.setBlock(x,y+13,z+12, 35,12)
mc.setBlock(x,y+13,z+12, 5)
#mc.setBlock(x+12,y+13,z+15, 35,12)
mc.setBlock(x+12,y+13,z+15, 5)
#mc.setBlock(x+15,y+13,z+3, 35,12)
mc.setBlock(x+15,y+13,z+3, 5)
#mc.setBlock(x+3,y+13,z, 35,12)
mc.setBlock(x+3,y+13,z, 5)

