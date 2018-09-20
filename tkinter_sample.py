#!/usr/bin/env python

import Tkinter
from Tkconstants import *

# Creates a Tk Class.
tk = Tkinter.Tk()

# Creates a frame Class

frame = Tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH, expand=True)
label = Tkinter.Label(frame, text="Hello World")
label.pack(fill=X, expand=True)
button = Tkinter.Button(frame, text="Exit", command=tk.destroy)
button.pack(side=BOTTOM)
tk.mainloop()
