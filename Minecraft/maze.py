# cwc 200121
from mcpi.minecraft import Minecraft
from mcpi import block    
from array import *

mc = Minecraft.create()
#mc.setting("world_immutable",True)
x, y, z = mc.player.getPos()  

'''
mc.setBlocks(x,y, zz, x+4, y+4, zz, block.IRON_BLOCK.id)
mc.setBlocks(x-1,y, zz, x-1, y+4, zz+4, block.SANDSTONE .id)
mc.setBlocks(x-1,y, zz+4, x+4, y+4, zz+4, block.GOLD_ORE.id)
mc.setBlocks(x+4,y, zz+1, x+4, y+4, zz+4, block.STONE.id)
'''



m = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
     [1,0,0,0,0,1,0,0,0,1,1,1,1,1,0,0,0,0,1],
     [1,0,1,1,0,1,0,1,1,0,0,0,0,1,0,1,1,0,1],
     [1,1,1,1,0,1,0,0,0,0,1,1,0,1,1,1,1,0,1],
     [1,0,0,0,0,0,1,1,1,0,0,1,0,0,0,0,1,0,1],
     [1,0,1,1,1,0,1,1,1,1,1,1,0,1,1,0,1,0,1],
     [1,0,1,0,0,0,1,0,0,0,0,0,0,1,1,0,1,0,0],
     [1,0,1,0,1,0,1,0,1,1,1,1,0,1,1,0,1,0,1],
     [1,0,1,1,1,0,1,0,1,1,1,1,0,0,1,0,0,0,1],
     [0,0,0,0,0,0,1,0,1,1,1,1,1,1,1,1,1,0,1],
     [1,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,1,0,1],
     [1,1,0,1,1,1,0,1,1,1,1,1,1,0,1,0,1,0,1],
     [1,1,0,1,1,1,0,0,1,0,0,0,1,0,1,0,1,0,1],
     [1,1,0,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1],
     [1,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,0,1],
     [1,0,1,1,1,1,1,1,1,1,1,0,1,0,1,0,1,0,1],
     [1,0,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1],
     [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
print(m)


mc.setBlocks(x,y-2,z, x+20,y+10,z+20,0)
mc.setBlock(x,y-1,z,2)
mc.setBlocks(x,y-3,z, x+19,y-3,z+19,89)
mc.setBlocks(x+1,y+6,z+1, x+19,y+6,z+19,1)

for h in range (0,20):
	for l  in range (0,19):
		print(m[h][l],end="")
		
		mc.setBlocks(x+h+1,y-2, z+l+1, x+h+1,y+5,z+l+1,m[h][l])

	print()
mc.setBlocks(x,y-3,z, x+20,y-3,z+20, 89)
mc.setBlocks(x+1,y+5,z+1, x+19,y+5,z+19, 1)
#mc.setBlocks(x-1,y+10, z-1, x+11,y+10,z+11,89)
#mc.setBlocks(x-1,y+20, z-1, x+11,y+20,z+11,89)
#mc.player.setPos(x,y+20,z-10)

#API Blocks
#====================
#   AIR                   0
#   STONE                 1
#   GRASS                 2
#   DIRT                  3
#   COBBLESTONE           4
#   WOOD_PLANKS           5
#   SAPLING               6
#   BEDROCK               7
#   WATER_FLOWING         8
#   WATER                 8
#   WATER_STATIONARY      9
#   LAVA_FLOWING         10
#   LAVA                 10
#   LAVA_STATIONARY      11
#   SAND                 12
#   GRAVEL               13
#   GOLD_ORE             14
#   IRON_ORE             15
#   COAL_ORE             16
#   WOOD                 17
#   LEAVES               18
#   GLASS                20
#   LAPIS_LAZULI_ORE     21
#   LAPIS_LAZULI_BLOCK   22
#   SANDSTONE            24
#   BED                  26
#   COBWEB               30
#   GRASS_TALL           31
#   WOOL                 35
#   FLOWER_YELLOW        37
#   FLOWER_CYAN          38
#   MUSHROOM_BROWN       39
#   MUSHROOM_RED         40
#   GOLD_BLOCK           41
#   IRON_BLOCK           42
#   STONE_SLAB_DOUBLE    43
#   STONE_SLAB           44
#   BRICK_BLOCK          45
#   TNT                  46
#   BOOKSHELF            47
#   MOSS_STONE           48
#   OBSIDIAN             49
#   TORCH                50
#   FIRE                 51
#   STAIRS_WOOD          53
#   CHEST                54
#   DIAMOND_ORE          56
#   DIAMOND_BLOCK        57
#   CRAFTING_TABLE       58
#   FARMLAND             60
#   FURNACE_INACTIVE     61
#   FURNACE_ACTIVE       62
#   DOOR_WOOD            64
#   LADDER               65
#   STAIRS_COBBLESTONE   67
#   DOOR_IRON            71
#   REDSTONE_ORE         73
#   SNOW                 78
#   ICE                  79
#   SNOW_BLOCK           80
#   CACTUS               81
#   CLAY                 82
#   SUGAR_CANE           83
#   FENCE                85
#   GLOWSTONE_BLOCK      89
#   BEDROCK_INVISIBLE    95
#   STONE_BRICK          98
#   GLASS_PANE          102
#   MELON               103
#   FENCE_GATE          107
#   GLOWING_OBSIDIAN    246
#   NETHER_REACTOR_CORE 247
