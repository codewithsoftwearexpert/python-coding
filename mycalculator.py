from tkinter import *
from tkinter import messagebox


if __name__=='__main__':
    root=Tk()
root.geometry("1000x1000")
root.title("My Calculator")
root.configure(background="violet")


lbl=Label(text='''Welcome to my Calculator''',bg="grey",fg="red",font="comicsensans 13 bold")
lbl.pack()

scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvar=scvalue,font="lucida 40 bold",fg="red")
screen.pack(fill=X,ipadx=8,pady=10,padx=10)


def but1():
    pass
def click(event):
    global scvalue
    text=event.widget.cget("text")
    print(text)
    if text=="=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            value=eval(screen.get())
        scvalue.set(value)
        screen.update()
    elif text=="c":
        scvalue.set("")
        screen.update()
        
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()




frame1=Frame(root,bg="grey")
frame1.pack()

#creating buttons
B=Button(frame1,text="9",command=but1,width=5,pady=5,padx=19,font="lucida 35 bold")
B.pack(side='left',anchor="nw",padx=10,pady=5)
B.bind("<Button-1>",click)


B=Button(frame1,text="8",command=but1,width=5,pady=5,padx=19,font="lucida 35 bold")
B.pack(side='left',anchor="nw",padx=10,pady=5)
B.bind("<Button-1>",click)

B=Button(frame1,text="7",command=but1,width=5,pady=5,padx=19,font="lucida 35 bold")
B.pack(side='left',anchor="nw",padx=10,pady=5)
B.bind("<Button-1>",click)


frame1=Frame(root,bg="grey")
frame1.pack()

#creating buttons
B=Button(frame1,text="6",command=but1,width=5,pady=5,padx=19,font="lucida 35 bold")
B.pack(side='left',anchor="nw",padx=10,pady=9)
B.bind("<Button-1>",click)


B=Button(frame1,text="5",command=but1,width=5,pady=5,padx=19,font="lucida 35 bold")
B.pack(side='left',anchor="nw",padx=10,pady=5)
B.bind("<Button-1>",click)

B=Button(frame1,text="4",command=but1,width=5,pady=5,padx=19,font="lucida 35 bold")
B.pack(side='left',anchor="nw",padx=10,pady=5)
B.bind("<Button-1>",click)


frame1=Frame(root,bg="grey")
frame1.pack()

#creating buttons
B=Button(frame1,text="3",command=but1,width=5,pady=5,padx=19,font="lucida 35 bold")
B.pack(side='left',anchor="nw",padx=10,pady=5)
B.bind("<Button-1>",click)


B=Button(frame1,text="2",command=but1,width=5,pady=5,padx=19,font="lucida 35 bold")
B.pack(side='left',anchor="nw",padx=10,pady=5)
B.bind("<Button-1>",click)

B=Button(frame1,text="1",command=but1,width=5,pady=5,padx=19,font="lucida 35 bold")
B.pack(side='left',anchor="nw",padx=10,pady=5)
B.bind("<Button-1>",click)


frame1=Frame(root,bg="grey")
frame1.pack()

#creating buttons
B=Button(frame1,text="0",command=but1,width=5,pady=5,padx=19,font="lucida 35 bold")
B.pack(side='left',anchor="nw",padx=10,pady=5)
B.bind("<Button-1>",click)


B=Button(frame1,text="+",command=but1,width=5,pady=5,padx=19,font="lucida 35 bold")
B.pack(side='left',anchor="nw",padx=10,pady=5)
B.bind("<Button-1>",click)

B=Button(frame1,text="-",command=but1,width=5,pady=5,padx=19,font="lucida 35 bold")
B.pack(side='left',anchor="nw",padx=10,pady=5)
B.bind("<Button-1>",click)


frame1=Frame(root,bg="grey")
frame1.pack()

#creating buttons
B=Button(frame1,text="*",command=but1,width=5,pady=5,padx=19,font="lucida 35 bold")
B.pack(side='left',anchor="nw",padx=10,pady=5)
B.bind("<Button-1>",click)


B=Button(frame1,text="/",command=but1,width=5,pady=5,padx=19,font="lucida 35 bold")
B.pack(side='left',anchor="nw",padx=10,pady=5)
B.bind("<Button-1>",click)

B=Button(frame1,text="=",command=but1,width=5,pady=5,padx=19,font="lucida 35 bold")
B.pack(side='left',anchor="nw",padx=10,pady=5)
B.bind("<Button-1>",click)


frame1=Frame(root,bg="grey")
frame1.pack()

#creating buttons
B=Button(frame1,text="c",command=but1,width=5,pady=5,padx=19,font="lucida 35 bold")
B.pack(side='left',anchor="nw",padx=10,pady=5)
B.bind("<Button-1>",click)







root.mainloop()
