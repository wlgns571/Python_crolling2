from tkinter import *
class myApp:
    def __init__(self, app):
        self.app = app
        self.app.title('제목 입니다.')
        self.app.geometry('640x400')
        self.app.resizable(False, False)
        self.input = Entry(self.app)
        self.textBox = Text(self.app, relief=SUNKEN)
        self.input.grid(row =0 , column=0)
        self.textBox.grid(row =1, columnspan=100)
        self.btn = Button(self.app, text='검색', command=self.fn_search).grid(row=0, column=1)
        self.btnDel = Button(self.app, text='삭제',command=self.fn_del).grid(row=0, column=2)

    def fn_text(self,msg):
        # text 위젯에 입력
        self.textBox.insert(INSERT, msg+'\n')
    def fn_search(self):
        # textBox에 entry 입력값 가져와서 함수 호출
        msg = self.input.get()
        self.fn_text(msg)
    def fn_del(self):
        # textBox 전체 삭제
        self.textBox.delete('1.0', 'end')

app = Tk()
myApp = myApp(app)
app.mainloop()