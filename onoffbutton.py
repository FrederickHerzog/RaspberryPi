#Frederick Herzog
try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk

HEIGHT = 300
WIDTH = 400
COLOR = 'black'

def toggle():
	if btn1.config('text')[-1] == 'OFF':
		btn1.config(text='ON', bg='green')
	else:
		btn1.config(text='OFF', bg='red')
		

window = tk.Tk()

canvas = tk.Canvas(window, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(window, bg=COLOR)
frame.place(relwidth=1, relheight=1)

btn1 = tk.Button(frame, text="OFF", bg='red', command = toggle)
btn1.place(relx=.35, rely=.4, relwidth=.3, relheight=.2)

window.mainloop()
