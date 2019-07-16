from tkinter import messagebox
from tkinter import *
import threading

print("hello world")
x = [1, 2, 3, 8, 9]
y = list()

def popup(var):
    top = Toplevel()
    top.geometry("200x200")
    top.title('Your Array')
    Message(top, text=str(var), padx=20, pady=20).pack()
    top.after(2000, top.destroy)

def ary():
    i = 0
    while i < len(x):
        try:
            print("i: {}".format(i))
            print("length of x: {}".format(len(x)))
            y.append(x[i])
            popup(y)
            threading.Timer(3,ary).start()
            i+=1
            print("i after append: {}".format(i))
        except:
            print("Not working")
            break

root = Tk()
root.geometry("300x300")
Button(root,text="Add to Array",command=ary).pack() 
root.mainloop()
    #print("array so far: {}".format(y))

print("Done!")

#messagebox.showinfo("Hello", "Hello!")