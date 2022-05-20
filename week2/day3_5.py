from tkinter import *
class moveBall:
    def __init__(self, app):
        self.canvas = Canvas(app, width=400, height=400)
        self.canvas.pack()
        self.app = app
        self.canvas.create_oval(100, 150, 150, 200, fill='red', tags='redball')
        self.canvas.pack()
    def move_left(self, event):
        self.canvas.move('redball', -10, 0)
        self.canvas.after(20)
        self.canvas.update()
    def move_right(self, event):
        self.canvas.move('redball', 10, 0)
        self.canvas.after(20)
        self.canvas.update()
    def move_top(self, event):
        self.canvas.move('redball', 0, -10)
        self.canvas.after(20)
        self.canvas.update()
    def move_bottom(self, event):
        self.canvas.move('redball', 0, 10)
        self.canvas.after(20)
        self.canvas.update()

app = Tk()
mov = moveBall(app)
mov.canvas.bind('<Left>', mov.move_left)
mov.canvas.bind('<Right>', mov.move_right)
mov.canvas.bind('<Up>', mov.move_top)
mov.canvas.bind('<Down>', mov.move_bottom)
mov.canvas.focus_set()
mov.canvas.pack()
app.mainloop()