from tkinter import *
import tkinter.messagebox
# ===================================setting=======================
root = Tk()
root.geometry('400x200')
root.title('Calculator')
root.resizable(width=False, height=False)  # we set the resizable false
color = 'gray'
root.configure(bg=color)
# ==============================Variables==============================
num1 = StringVar()
num2 = StringVar()
res_value = StringVar  ()
# ==============================Frames==============================
top_first = Frame(root, width=400, height=50, bg=color)
top_first.pack(side=TOP)

top_second = Frame(root, width=400, height=50, bg=color)
top_second.pack(side=TOP)

top_third = Frame(root, width=400, height=50, bg=color)
top_third.pack(side=TOP)

top_forth = Frame(root, width=400, height=50, bg=color)
top_forth.pack(side=TOP)

# ===============================Functions=============================
def errorMsg(ms):
    if ms == 'error':
        tkinter.messagebox.showerror('Error','something went wrong')
    elif ms == 'divide on zero error':
        tkinter.messagebox.showerror('Division Zero', 'Can not divide on zero')

def plus():
    try:
        value = float(num1.get()) + float(num2.get())
        res_value.set(value)
    except:
        errorMsg('error')


def minuse():
    try:
        value = float(num1.get()) - float(num2.get())
        res_value.set(value)
    except:
        errorMsg('error')


def mul():
    try:
        value = float(num1.get()) * float(num2.get())
        res_value.set(value)
    except:
        errorMsg('error')



def divide():
    if num2.get() == '0':
        errorMsg('divide on zero error')
    elif num2.get() != '0':
        try:
            value = float(num1.get()) / float(num2.get())
            res_value.set(value)
        except:
            errorMsg('error')


# ===============================Buttons=============================
btn_plus = Button(top_third, text='+', width=10, command=lambda: plus(),
                  highlightbackground=color)
btn_plus.pack(side=LEFT,padx=10,pady=10)

btn_minus = Button(top_third, text='-',width=10, command= lambda: minuse(),
                   highlightbackground=color)
btn_minus.pack(side=LEFT,padx=10,pady=10)

btn_multi = Button(top_third, text='*',width=10, command= lambda: mul(),
                   highlightbackground=color)
btn_multi.pack(side=LEFT,padx=10,pady=10)

btn_divide = Button(top_third, text='/',width=10, command= lambda: divide(),
                    highlightbackground=color)
btn_divide.pack(side=LEFT,padx=10,pady=10)
# ===============================Inputs and labels=============================
label_first_num = Label(top_first, text='input number 1:', bg=color)
label_first_num.pack(side=LEFT, pady=10)

first_num = Entry(top_first, highlightbackground=color, textvariable=num1)
first_num.pack(side=LEFT, padx=10)

label_second_num = Label(top_second, text='input number 2:', bg=color)
label_second_num.pack(side=LEFT, pady=10)

second_num = Entry(top_second, highlightbackground=color, textvariable=num2)
second_num.pack(side=LEFT, padx=10)

res_first_num = Label(top_forth, text='result:', bg=color)
res_first_num.pack(side=LEFT, pady=10)

res_num = Entry(top_forth, highlightbackground=color, textvariable=res_value)
res_num.pack(side=LEFT, padx=10)
root.mainloop()