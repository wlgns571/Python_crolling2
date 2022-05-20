from tkinter import *
app = Tk()

def donoting():
    filewin = Toplevel(app)
    fileclose = Button(filewin, text='Do notthing button')
    fileclose.config(command=app.quit)
    fileclose.pack()
def fn_edit():
    print('에디트')
def fn_saving():
    print('저장')
def fn_close():
    app.quit()

menubar = Menu(app)
filemenu = Menu(menubar, tearoff=0)
editmenu = Menu(menubar, tearoff=0)

filemenu.add_command(label='Open', command=donoting)
filemenu.add_command(label='Save', command=fn_saving)
filemenu.add_command(label='Edit', command=fn_edit)
filemenu.add_command(label='Close', command=fn_close)

filemenu.add_separator()

editmenu.add_command(label='Delete')

filemenu.add_command(label='Exit', command=fn_close)
menubar.add_cascade(label='File', menu=filemenu)
app.config(menu=menubar)
app.mainloop()