# Set the player name (7 chars) for Minecraft PI Edition
# Written by Richard Garsthagen - richard@coderdojo-zoetermeer.nl
# Updated to python3 by mini-ray
#
# Use at own risk. Please make a backup of minecraft-pi first!

namestart= 1026250

try:

 fh = open("/opt/minecraft-pi/minecraft-pi", "r+b")
 fh.seek(namestart)

 print ("Current name: {} ".format(fh.read(7)))

 piname = input("New player name: ")

 if len(piname) > 1:
  if len(piname) > 7: piname = piname[:7]
  if len(piname) < 7:
   extraspaces = 7 - len(piname)
   for x in range(0,extraspaces):
     piname = piname + " "
  print ("Changed name to:" + piname + " - " + str(len(piname)))
  fh.seek(namestart)
  fh.write(piname.encode())
 else:
  print ("No new name given")

 fh.close()

except:
 print ("Can not change name, is minecraft running? Please close the app first")
