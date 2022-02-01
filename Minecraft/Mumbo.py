from mcpi.minecraft import Minecraft

mc = Minecraft.create("192.168.7.97",4711)



x, y, z = mc.player.getPos()

x = x+5

mc.setBlocks(x,y,z, x+9,y+8,z+9, 0)
mc.setBlocks(x+1,y,z+1, x+8,y+7,z+8, 24,2)
mc.setBlocks(x+1,y+7,z+1, x+8,y+7,z+8, 35,15)
mc.setBlocks(x+1,y+6,z+1, x+8,y+6,z+1, 35,15)
mc.setBlocks(x+8,y+6,z+1, x+8,y+6,z+8, 35,15)
mc.setBlocks(x+1,y+6,z+8, x+8,y+6,z+8, 35,15)
mc.setBlocks(x+1,y+5,z+2, x+1,y+5,z+3, 5)
mc.setBlocks(x+1,y+5,z+6, x+1,y+5,z+7, 5)
mc.setBlock(x+1,y+4,z+3, 35,15)
mc.setBlock(x+1,y+4,z+6, 35,15)
mc.setBlocks(x+1,y+1,z+2, x+1,y+1,z+3, 35,15)
mc.setBlocks(x+1,y+2,z+3, x+1,y+2,z+6, 35,15)
mc.setBlocks(x+1,y+1,z+6, x+1,y+1,z+7, 35,15)
mc.setBlocks(x+8,y,z+1, x+8,y+7,z+8, 35,15)
mc.setBlocks(x+2,y+5,z+1, x+7,y+4,z+1, 35,15)
mc.setBlocks(x+4,y+3,z+1, x+7,y+3,z+1, 35,15)
mc.setBlocks(x+5,y+2,z+1, x+7,y,z+1, 35,15)
mc.setBlocks(x+2,y+5,z+8, x+8,y+4,z+8, 35,15)
mc.setBlocks(x+4,y+3,z+8, x+8,y+3,z+8, 35,15)
mc.setBlocks(x+5,y+2,z+8, x+8,y+2,z+8, 35,15)
mc.setBlocks(x+6,y+1,z+8, x+8,y,z+8, 35,15)

mc.postToChat("Hello, wanna do some redstone?")
