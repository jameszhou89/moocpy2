# Message控件的问题


## 问题

上周出现的一个情况是，花费了很多时间研究了Tkinter的Message 插件的问题，但是这个跟问题并不一定有很大程度的联系，导致浪费了很多时间。

花费时间研究的内容是：如何可以在message中写入变量参数,而不是写死的text="this is a message"（如下文所示）。

    from Tkinter import *
    master = Tk()
    w = Message(master, text="this is a message")
    w.pack()
    mainloop()
    

## 解决思路1





## 正确的解决思路



