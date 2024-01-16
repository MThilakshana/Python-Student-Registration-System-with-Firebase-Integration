from tkinter import *
import pyrebase
from tkinter import messagebox

#connect to the firebae
config = {
    "apiKey": "AIzaSyAC-wVs1ByMhmK-xRYYCg6_uPtPilf-Ek4",
    "authDomain": "studentregistration-89577.firebaseapp.com",
    "projectId": "studentregistration-89577",
    "databaseURL":"https://studentregistration-89577-default-rtdb.firebaseio.com/",
    "storageBucket": "studentregistration-89577.appspot.com",
    "messagingSenderId": "903546180662",
    "appId": "1:903546180662:web:e23983e5c9a5bd8f0e3497",
    "measurementId": "G-SWRQ508XDQ"
}

firebase = pyrebase.initialize_app(config)
database = firebase.database()

#save data 
def savedata():
    idV = id.get()
    nameV = name.get()
    emailV = email.get()
    departV = department.get()
    facV = faculty.get()
    uniV = university.get()
    
    if (idV=="" or nameV=="" or emailV=="" or departV=="" or facV=="" or uniV==""):
        messagebox.showinfo("Warning","All fields required!")
    else:
        data = {"ID":idV,"Name":nameV,"Email":emailV,"Department":departV,"Faculty":facV,"University":uniV}
        
        database.child("Students").child(idV).set(data)
        messagebox.showinfo("Message","Data saved successfully!")
        id.delete(0,END)
        name.delete(0,END)
        email.delete(0,END)
        department.delete(0,END)
        faculty.delete(0,END)
        university.delete(0,END)
        
#search data
def searchdata():
    idV = id.get()
    if (idV==""):
        messagebox.showinfo("Warning","Enter ID")
    else:
        dataVal = database.child("Students").child(idV).get().val()
        name.insert(0,dataVal.get('Name'))
        email.insert(0,dataVal.get('Email'))
        department.insert(0,dataVal.get('Department'))
        faculty.insert(0,dataVal.get('Faculty'))
        university.insert(0,dataVal.get('University'))
        
#update Data
def updateData():
    idV = id.get()
    nameV = name.get()
    emailV = email.get()
    departV = department.get()
    facV = faculty.get()
    uniV = university.get()
        
    if (idV=="" or nameV=="" or emailV=="" or departV=="" or facV=="" or uniV==""):
        messagebox.showinfo("Warning","All fields required!")
    else:
        data = {"ID":idV,"Name":nameV,"Email":emailV,"Department":departV,"Faculty":facV,"University":uniV}
        database.child("Students").child(idV).update(data)
        messagebox.showinfo("Message","Data Updated Successfully!")
        id.delete(0,END)
        name.delete(0,END)
        email.delete(0,END)
        department.delete(0,END)
        faculty.delete(0,END)
        university.delete(0,END)
        
#delete btn
def deleteData():
    idV = id.get()
    if (idV==""):
        messagebox.showinfo("Warning","Enter ID")
    else:
        database.child("Students").child(idV).remove()
        messagebox.showinfo("Message","Data Deleted Successfully!")
        id.delete(0,END)
        name.delete(0,END)
        email.delete(0,END)
        department.delete(0,END)
        faculty.delete(0,END)
        university.delete(0,END)
        

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
      width=40)
id.place(x=200,y=70)

Label(root,
      text="Student Name",
      font=('Times',12),
      fg='Black',
      bg="white").place(x=20,y=110)

name = Entry(root,
      font=('Times',12),
      fg='Black',
      bg='white',
      width=40)
name.place(x=200,y=110)

Label(root,
      text="E-mail",
      font=('Times',12),
      fg='Black',
      bg="white").place(x=20,y=150)

email = Entry(root,
      font=('Times',12),
      fg='Black',
      bg='white',
      width=40)
email.place(x=200,y=150)

Label(root,
      text="Department",
      font=('Times',12),
      fg='Black',
      bg="white").place(x=20,y=190)

department = Entry(root,
      font=('Times',12),
      fg='Black',
      bg='white',
      width=40)
department.place(x=200,y=190)

Label(root,
      text="Faculty",
      font=('Times',12),
      fg='Black',
      bg="white").place(x=20,y=230)

faculty = Entry(root,
      font=('Times',12),
      fg='Black',
      bg='white',
      width=40)
faculty.place(x=200,y=230)

Label(root,
      text="University",
      font=('Times',12),
      fg='Black',
      bg="white").place(x=20,y=270)

university = Entry(root,
      font=('Times',12),
      fg='Black',
      bg='white',
      width=40)
university.place(x=200,y=270)

searchbtn = Button(root,
                   text="Search",
                   font=('Times',12),
                   fg="Black",
                   bg="White",
                   width=15,
                   border=3,
                   cursor="hand2",
                   command=searchdata).place(x=600,y=70)

updatebtn = Button(root,
                   text="Update",
                   font=('Times',12),
                   fg="Black",
                   bg="White",
                   width=15,
                   border=3,
                   cursor="hand2",
                   command=updateData).place(x=600,y=120)

savebtn = Button(root,
                   text="Save",
                   font=('Times',12),
                   fg="Black",
                   bg="White",
                   width=15,
                   border=3,
                   cursor="hand2",
                   command=savedata).place(x=600,y=170)

deletebtn = Button(root,
                   text="Delete",
                   font=('Times',12),
                   fg="Black",
                   bg="White",
                   width=15,
                   border=3,
                   cursor="hand2",
                   command=deleteData).place(x=600,y=220)

exitbtn = Button(root,
                   text="Exit",
                   font=('Times',12),
                   fg="Black",
                   bg="White",
                   width=15,
                   border=3,
                   cursor="hand2",
                   command=root.destroy).place(x=600,y=270)


root.mainloop()