from mcpi.minecraft import Minecraft
import mcpi.block as block

mc = Minecraft.create("192.168.7.226",4711)

x, y, z = mc.player.getPos()

mc.player.setTilePos(0, 30, 0)
