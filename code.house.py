import simplegui


top = 300
bot = 550
rig = 400
lef = 150

def draw_handler(canvas):
    canvas.draw_polygon([(lef, top), (rig, top), (rig, bot), (lef, bot)], 3, "Black")
    canvas.draw_polygon([(250, 425), (300, 425), (300, bot), (250, bot)], 3, "Black")
    canvas.draw_polygon([(180, 440), (220, 440), (220, 480), (180, 480)], 3, "Black")
    canvas.draw_polygon([(330, 440), (370, 440), (370, 480), (330, 480)], 3, "Black")
    canvas.draw_polygon([(lef, top), (rig, top), (rig, bot), (lef, bot)], 3, "Black")
    canvas.draw_polygon([(lef, top), (rig, top), ((lef+rig)/2, 150)], 3, "Black")
    
    
    
frame = simplegui.create_frame("Home Sweet Home", 600, 600)

frame.set_canvas_background("White")
frame.set_draw_handler(draw_handler)
frame.start()
