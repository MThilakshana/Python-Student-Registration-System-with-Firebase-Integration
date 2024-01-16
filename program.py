from tkinter import *

root=Tk()
root.title('Student Registration')
root.geometry('775x400+300+200')
root.configure(bg="#fff")
root.resizable(False,False)

frame = Frame(root,
              width=200,
              height=400,
              bg='red').place(x=575,y=0)

Label(root,
      text="Student Registration",
      font=('Times',25,'bold'),
      fg='Black',
      bg='white').pack(fill=X)

Label(root,
      text="Student ID",
      font=('Times',12),
      fg='Black',
      bg="white").place(x=20,y=70)

id = Entry(root,
      font=('Times',12),
      fg='Black',
      bg='white',
      width=40).place(x=200,y=70)

Label(root,
      text="Student Name",
      font=('Times',12),
      fg='Black',
      bg="white").place(x=20,y=110)

name = Entry(root,
      font=('Times',12),
      fg='Black',
      bg='white',
      width=40).place(x=200,y=110)

Label(root,
      text="E-mail",
      font=('Times',12),
      fg='Black',
      bg="white").place(x=20,y=150)

email = Entry(root,
      font=('Times',12),
      fg='Black',
      bg='white',
      width=40).place(x=200,y=150)

Label(root,
      text="Department",
      font=('Times',12),
      fg='Black',
      bg="white").place(x=20,y=190)

department = Entry(root,
      font=('Times',12),
      fg='Black',
      bg='white',
      width=40).place(x=200,y=190)

Label(root,
      text="Faculty",
      font=('Times',12),
      fg='Black',
      bg="white").place(x=20,y=230)

faculty = Entry(root,
      font=('Times',12),
      fg='Black',
      bg='white',
      width=40).place(x=200,y=230)

Label(root,
      text="University",
      font=('Times',12),
      fg='Black',
      bg="white").place(x=20,y=270)

university = Entry(root,
      font=('Times',12),
      fg='Black',
      bg='white',
      width=40).place(x=200,y=270)


root.mainloop()