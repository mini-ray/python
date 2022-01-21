from mcpi.minecraft import Minecraft

mc = Minecraft.create("10.183.3.67",4711)



x, y, z = mc.player.getPos()

x = x+1

mc.setBlocks(x,y,z-1, x+15,y+15,z+1, 0)
mc.setBlock(x,y,z, 1)
mc.setBlock(x+1,y+1,z, 2)
mc.setBlock(x+2,y+2,z, 3)
mc.setBlock(x+3,y+3,z, 4)
mc.setBlock(x+4,y+4,z, 5)
mc.setBlock(x+5,y+5,z, 7)
mc.setBlock(x+6,y+6,z, 14)
mc.setBlock(x+7,y+7,z, 15)
mc.setBlock(x+8,y+8,z, 16)
mc.setBlock(x+9,y+9,z, 17,0)
mc.setBlock(x+10,y+10,z, 17,1)
mc.setBlock(x+11,y+11,z, 17,2)
mc.setBlock(x+12,y+12,z, 18,0)
mc.setBlock(x+13,y+13,z, 18,1)
mc.setBlock(x+14,y+14,z, 18,2)

mc.postToChat("StariwayToHeaven")
