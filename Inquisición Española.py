from mcpi.minecraft import Minecraft
import mcpi.block as block

mc = Minecraft.create("192.168.7.220",4711)
#"192.168.7.226",4711

x,y,z = mc.player.getPos()

#block = block.PAINTING.id

mc.setBlocks(x+5,y,z,x+5,y+1,z,35,14)
mc.setBlocks(x+5,y,z+2,x+5,y+1,z+2,35,14)
mc.setBlocks(x+5,y,z-2,x+5,y+1,z-2,35,14)

#mc.setBlock(x+4,y+1,z-2,block)
#mc.setBlock(x+4,y+1,z-2,block)
#mc.setBlock(x+4,y+1,z-2,block)

mc.postToChat("Nadie espera la Inquisicion Espanola.")
#mc.postToChat("Nadie espera la Inquisición Española.")

