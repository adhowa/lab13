#########################################
#
#         70-100pt - Making a game
#
#########################################


# 70pt - Add buttons for left, right and down that move the player circle
# 100pt - using lab 11 as an example, add in three horizontally scrolling "enemies"
# Make them scroll at different speeds and directions.



from Tkinter import *
root = Tk()

drawpad = Canvas(root, width=800,height=600, background='white')
player = drawpad.create_oval(390,580,410,600, fill="red")

# Create your "enemies" here, before the class

circle = drawpad.create_oval(10,10,50,50, fill='green')
direction = 1

enimy1 = drawpad.create_oval(100,100,50,50, fill='green')
direction = 1 

enimy2 = drawpad.create_oval(200,200,50,50, fill='green')
direction = 1 

class MyApp:
	def __init__(self, parent):
       	    global drawpad
       	    self.myParent = parent  
       	    self.myContainer1 = Frame(parent)
       	    self.myContainer1.pack()
       	    
       	    self.up = Button(self.myContainer1)
       	    self.up.configure(text="up", background= "green")
       	    self.up.grid(row=0,column=2)
       	    
       	    self.down = Button(self.myContainer1)
       	    self.down.configure(text="down",background= "green")
       	    self.down.grid(row=1,column=2)
       	    
       	    self.left = Button(self.myContainer1)
       	    self.left.configure(text="left",background= "green")
       	    self.left.grid(row=1,column=1)
       	    
       	    self.right = Button(self.myContainer1)
       	    self.right.configure(text="right",background= "green")
       	    self.right.grid(row=1,column=3)
       	    
       	    # Bind an event to the first button
       	    self.up.bind("<Button-1>", self.upClicked)
       	    self.down.bind("<Button-1>", self.downClicked) 
       	    self.left.bind("<Button-1>",self.leftClicked)
       	    self.right.bind("<Button-1>",self.rightClicked)
       	    # No need to edit this - just includes the drawpad into our frame
       	    drawpad.pack(side=BOTTOM)
       	    self.animate()
       	    
	def animate(self):
	    global drawpad
	    global player
	    global circle
	    # Remember to include your "enemies" with "global"
            x1, y1, x2, y2 = drawpad.coords(circle)
            if x2 > drawpad.winfo_width(): 
                drawpad.move(circle, -800, 0)
            elif x1 < 0:
                direction = 5
            drawpad.move(circle,20,0)
            x1, y1, x2, y2 = drawpad.coords(enimy1)
            if x2 > drawpad.winfo_width():
                drawpad.move(enimy1,-800, 0)
            elif x1 <0:
                direction = 5
            drawpad.move(enimy1,10,0)
            x1, y1, x2, y2 = drawpad.coords(enimy2)
            if x2 > drawpad.winfo_width():
                drawpad.move(enimy2,-800, 0)
            elif x1 <0:
                direction = 5 
            drawpad.move(enimy2,5,0)
            drawpad.after(1, self.animate)  
     	
	def upClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,0,-20)
	   
	def downClicked(self, event):
	    global oval 
	    global player
	    drawpad.move(player,0,20)
		
        def leftClicked(self, event):
            global oval
            global player
            drawpad.move(player,-20,0)
            
        def rightClicked(self, event):
            global oval 
            global player
            drawpad.move(player,20,0)
		
app = MyApp(root)
root.mainloop()