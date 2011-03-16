from Tkinter import *

def keypress(event):
	if event.keysym == 'Escape':
		root.destroy()

	print "pressed", repr(event.keysym)
	

root = Tk()

frame = Frame(root)
frame.bind_all('<Key>', keypress)
frame.pack()

root.mainloop()

