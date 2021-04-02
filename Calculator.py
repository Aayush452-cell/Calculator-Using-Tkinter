from tkinter import *


def click(event):
    global strv
    text=event.widget.cget("text")
    print(text)
    if(text=="="):
        if strv.get().isdigit():
            value=int(strv.get())
        else:
            try:
                value=eval(screen.get())
            except Exception as e:
                print("Error")
                value="Error"
        strv.set(value)
        screen.update()
    elif text=="c":
        strv.set("")
        screen.update()
    else:
        strv.set(strv.get()+text)
        screen.update()


root=Tk()
root.geometry("444x644")
root.configure(background="orange")
root.title("Calculator")

strv=StringVar()
strv.set("")

screen=Entry(root,textvar=strv,font="lucidia 40 bold")
screen.pack(fill=X,ipadx=8,pady=10,padx=10)

image_1=PhotoImage(file='num1.png')
image_2=PhotoImage(file='num2.png')
image_3=PhotoImage(file='num3.png')
image_4=PhotoImage(file='num4.png')
image_5=PhotoImage(file='num5.png')
image_6=PhotoImage(file='num6.png')
image_7=PhotoImage(file='num7.png')
image_8=PhotoImage(file='num8.png')
image_9=PhotoImage(file='num9.png')
image_0=PhotoImage(file='num0.png')
image_divide=PhotoImage(file='numdivide.png')

f=Frame(root,bg="orange")
b=Button(f,image=image_9,text="9", bg="orange",borderwidth=0,font="lucidia 30 bold")
b.pack(side=LEFT,padx=2,pady=2)
b.bind("<Button-1>",click)

b=Button(f,image=image_8,text="8", bg="orange",borderwidth=0,font="lucidia 30 bold")
b.pack(side=LEFT,padx=2,pady=2)
b.bind("<Button-1>",click)

b=Button(f,image=image_7,text="7", bg="orange",borderwidth=0,font="lucidia 30 bold")
b.pack(side=LEFT,padx=0,pady=0)
b.bind("<Button-1>",click)


f.pack()

f=Frame(root,bg="orange")
b=Button(f,image=image_6,text="6", bg="orange",borderwidth=0,font="lucidia 30 bold")
b.pack(side=LEFT,padx=0,pady=0)
b.bind("<Button-1>",click)

b=Button(f,image=image_5,text="5", bg="orange",borderwidth=0,font="lucidia 30 bold")
b.pack(side=LEFT,padx=0,pady=0)
b.bind("<Button-1>",click)

b=Button(f,image=image_4,text="4", bg="orange",borderwidth=0,font="lucidia 30 bold")
b.pack(side=LEFT,padx=0,pady=0)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg="orange")
b=Button(f,image=image_3,text="3", bg="orange",borderwidth=0,font="lucidia 30 bold")
b.pack(side=LEFT,padx=0,pady=0)
b.bind("<Button-1>",click)

b=Button(f,image=image_2,text="2", bg="orange",borderwidth=0,font="lucidia 30 bold")
b.pack(side=LEFT,padx=0,pady=0)
b.bind("<Button-1>",click)

b=Button(f,image=image_1,text="1", bg="orange",borderwidth=0,font="lucidia 30 bold")
b.pack(side=LEFT,padx=0,pady=0)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg="orange")
b=Button(f,image=image_0,text="0", bg="orange",borderwidth=0,font="lucidia 30 bold")
b.pack(side=LEFT,padx=0,pady=0)
b.bind("<Button-1>",click)

b=Button(f,text="+",padx=4,pady=4,font="lucidia 30 bold")
b.pack(side=LEFT,padx=3,pady=2)
b.bind("<Button-1>",click)

b=Button(f,text="-",padx=4,pady=4,font="lucidia 30 bold")
b.pack(side=LEFT,padx=4,pady=2)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg="orange")
b=Button(f,text="*",padx=6,pady=4,font="lucidia 30 bold")
b.pack(side=LEFT,padx=3,pady=2)
b.bind("<Button-1>",click)

b=Button(f,text="/",padx=6,pady=4,font="lucidia 30 bold")
b.pack(side=LEFT,padx=3,pady=2)
b.bind("<Button-1>",click)

f.pack()

f=Frame(root,bg="grey")
b=Button(f,text="=",padx=4,pady=4,font="lucidia 30 bold")
b.pack(side=LEFT,padx=2,pady=2)
b.bind("<Button-1>",click)

b=Button(f,text="c",padx=4,pady=4,font="lucidia 30 bold")
b.pack(side=LEFT,padx=2,pady=2)
b.bind("<Button-1>",click)


b=Button(f,text=".",padx=4,pady=4,font="lucidia 30 bold")
b.pack(side=LEFT,padx=2,pady=2)
b.bind("<Button-1>",click)

f.pack()

root.mainloop()