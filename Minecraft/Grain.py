from mcpi.minecraft import Minecraft

mc = Minecraft.create("10.183.0.32",4711)



x, y, z = mc.player.getPos()

x = x+5

mc.setBlocks(x,y,z, x+9,y+8,z+9, 0)
mc.setBlocks(x+1,y,z+1, x+8,y+7,z+8, 24,2)
mc.setBlocks(x+1,y+7,z+1, x+8,y+7,z+8, 35,12)
mc.setBlocks(x+2,y+7,z+2, x+7,y+7,z+7, 5)
mc.setBlocks(x+1,y+6,z+1, x+8,y+6,z+1, 35,12)
mc.setBlocks(x+8,y+6,z+1, x+8,y+6,z+8, 35,12)
mc.setBlocks(x+1,y+6,z+8, x+8,y+6,z+8, 35,12)
mc.setBlocks(x+1,y+6,z+2, x+1,y+5,z+7, 5)
mc.setBlock(x+1,y+6,z+5, 35,12)
mc.setBlocks(x+1,y+6,z+1, x+1,y+4,z+1, 35,12)
mc.setBlocks(x+1,y+6,z+8, x+1,y+4,z+8, 35,12)
mc.setBlocks(x+1,y+2,z+2, x+1,y+3,z+2, 35,15)
mc.setBlocks(x+1,y+2,z+7, x+1,y+3,z+7, 35,15)

mc.setBlocks(x+8,y,z+1, x+8,y+7,z+8, 35,12)
mc.setBlocks(x+2,y+1,z+1, x+7,y+6,z+1, 5)
mc.setBlocks(x+2,y+1,z+8, x+7,y+6,z+8, 5)

mc.setBlock(x+6,y+6,z+1, 35,12)
mc.setBlock(x+5,y+1,z+1, 35,12)

mc.setBlock(x+6,y+6,z+8, 35,12)
mc.setBlock(x+5,y+1,z+8, 35,12)
mc.setBlock(x+4,y+6,z+8, 35,12)
mc.setBlock(x+3,y+3,z+8, 35,12)
mc.setBlocks(x+2,y+5,z+8, x+3,y+5,z+8, 35,12)

mc.setBlocks(x+3,y,z+1, x+7,y,z+1, 35,12)
mc.setBlocks(x+2,y,z+1, x+2,y+3,z+8, 24,2)
mc.setBlocks(x+3,y+1,z+1, x+3,y+2,z+8, 24,2)
mc.setBlocks(x+3,y+3,z+1, x+3,y+7,z+1, 35,12)
mc.setBlocks(x+8,y+3,z+1, x+8,y+4,z+8, 5)
mc.setBlocks(x+6,y+2,z+8, x+8,y+2,z+8, 35,12)
mc.setBlocks(x+6,y+1,z+8, x+8,y,z+8, 35,12)
mc.setBlocks(x+6,y+1,z+8, x+7,y+2,z+8, 5)
mc.setBlocks(x+8,y+1,z+2, x+8,y+6,z+7, 5)
mc.setBlock(x+8,y+1,z+3, 35,12)
mc.setBlock(x+8,y+1,z+6, 35,12)
mc.setBlock(x+8,y+6,z+3, 35,12)
mc.setBlock(x+8,y+6,z+6, 35,12)

mc.postToChat("Hello, lets build something.")
