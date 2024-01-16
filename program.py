from tkinter import *

root=Tk()
root.title('Student Registration')
root.geometry('775x330+300+200')
root.configure(bg="#fff")
root.resizable(False,False)

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

searchbtn = Button(root,
                   text="Search",
                   font=('Times',12),
                   fg="Black",
                   bg="White",
                   width=15,
                   border=3,
                   cursor="hand2").place(x=600,y=70)

updatebtn = Button(root,
                   text="Update",
                   font=('Times',12),
                   fg="Black",
                   bg="White",
                   width=15,
                   border=3,
                   cursor="hand2").place(x=600,y=120)

savebtn = Button(root,
                   text="Save",
                   font=('Times',12),
                   fg="Black",
                   bg="White",
                   width=15,
                   border=3,
                   cursor="hand2").place(x=600,y=170)

exitbtn = Button(root,
                   text="Exit",
                   font=('Times',12),
                   fg="Black",
                   bg="White",
                   width=15,
                   border=3,
                   cursor="hand2",
                   command=root.destroy).place(x=600,y=260)


root.mainloop()