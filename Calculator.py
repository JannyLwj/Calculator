from tkinter import*

# 创建横条型框架
def iFrame(root, side):
    storeObj = Frame(root,borderwidth=4, bd=4, bg="powder blue")
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj

# 创建按钮
def button(root, side, text, command=None):
    storeObj = Button(root, text=text, command=command)
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj


# 继承了Frame类，初始化程序界面的布局
class Calculator(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add('*Font', 'arial 20 bold')
        self.pack(expand=YES, fill=BOTH)
        self.master.title('Simple Calculater')

        display = StringVar()
        # 添加输入框
        Entry(self, relief=RIDGE,
              textvariable=display,justify='right', bd=15, bg="Powder blue").pack(side=TOP, expand=YES,
                                         fill=BOTH)
        # 添加清除按钮
        #clearF = frame(self, TOP)
        #button(clearF, LEFT, 'clear', lambda w=display: w.set(''))

        for clearBut in(["CE"],["C"]):
            keyF = iFrame(self, TOP)
            for char in clearBut:
                button(keyF, LEFT, char, lambda storeObj=display, c=char: storeObj.set(''))

        # 添加横条型框架以及里面的按钮
        for key in ('123*', '456/', '789-', '0.+'):
            keyF = iFrame(self, TOP)
            for char in key:
                button(keyF, LEFT, char, lambda storeObj=display, c=char: storeObj.set(storeObj.get() + c))

        # 添加操作符按钮
        opsF = iFrame(self, TOP)
        for char in '=':
            if char == '=':
                btn = button(opsF, LEFT, char)
                btn.bind('<ButtonRelease - 1>', lambda e, s=self, storeObj=display: s.calc(storeObj), '+')
            else:
                btn = button(opsF, LEFT, char, lambda storeObj=display, s='%s' % char: storeObj.set(storeObj.get() + s))

        # 调用eval函数计算表达式的值
    def calc(self, display):
        try:
            display.set(eval(display.get()))
        except:
            display.set("ERROR")

# 程序的入口
if __name__=='__main__':
    Calculator().mainloop()