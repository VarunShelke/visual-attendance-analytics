# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 21:56:55 2018

@author: SHREE
"""

from tkinter import *
from tkinter import messagebox 
import subprocess as sub
window = Tk()
window.title("For Login")
 
window.geometry('500x300')
window.configure(background='skyblue')
list=['monday','Monday','tuesday','Tuesday','wednesday','Wednesday','thursday','Thursday','friday','Friday']
welcomelabel=Label(window,text="WELCOME",bg="skyblue",justify=CENTER,fg="red",font="Helvetica 30 bold")
welcomelabel.place(x=250,y=50,anchor="center")
#welcomelabel.grid(column=50,row=50)
txt1=Entry(window,width=30)
txt1.place(x=270,y=100,anchor="center")
txt2=Entry(window,width=30,show="*")
txt2.place(x=270,y=160,anchor="center")
txt3=Entry(window,width=30)
txt3.place(x=270,y=220,anchor="center")
lbl1=Label(window,text="Authority",bg="skyblue",justify=CENTER,fg="black",font="Arial 10 bold")
lbl1.place(x=130,y=100,anchor="center")
lbl2=Label(window,text="Password",bg="skyblue",justify=CENTER,fg="black",font="Arial 10 bold")
lbl2.place(x=130,y=160,anchor="center")
lbl3=Label(window,text="Day",bg="skyblue",justify=CENTER,fg="black",font="Arial 10 bold")
lbl3.place(x=130,y=220,anchor="center")


def clicked():
    
    if txt1.get()=="gaurav" and txt2.get()=="imgaurav":
        flag=0
        for item in list:
            if item==txt3.get():
                day=item
                print(day)
                flag=1
        
        if flag==1:
            window.destroy()
            yes=Tk()
            yes.title("Attendance System")
            yes.geometry('500x300')
            yes.configure(background='lightgreen')
            def xyz():
                print(day)
                
                
            test=Button(yes,text="Go For Attendance",relief=RAISED,bg="grey",fg="black",font="Helvetica 8 bold",command=xyz)
            test.place(x=250,y=250,anchor="center")
            test.config(height=2,width=20)
            def fixed1():#student login
                student=Tk()
                student.title("Student Login")
                student.geometry('500x200')
                student.configure(background='fuchsia')
                
                rolllabel=Label(student,text="Enter Roll No.",bg="fuchsia",justify=CENTER,fg="black",font="Arial 10 bold")
                rolllabel.place(x=110,y=100,anchor="center")

                roll=Entry(student,width=30)
                roll.place(x=310,y=100,anchor="center")

                rollbutton=Button(student,text="Show Attendance",relief=RAISED,bg="grey",fg="black",font="Helvetica 8 bold",command=xyz)
               # rollbutton.place(x=250,y=200,anchor="center")
                rollbutton.pack(side="bottom") 
                rollbutton.config(height=2,width=20)
            
                student.mainloop()
            studentlogin=Button(yes,text="Student Login",relief=RAISED,bg="grey",fg="black",font="Helvetica 8 bold",command=fixed1)
            studentlogin.place(x=150,y=130,anchor="center")
            studentlogin.config(height=2,width=15)    
            def fixed2():#teacher login
                teacher=Tk()
                teacher.title("Teacher Login")
                teacher.geometry('500x200')
                teacher.configure(background='fuchsia')
                
                rl=Label(teacher,text="Enter Subject Name",bg="fuchsia",justify=CENTER,fg="black",font="Arial 10 bold")
                rl.place(x=110,y=100,anchor="center")

                rol=Entry(teacher,width=30)
                rol.place(x=310,y=100,anchor="center")

                tbutton=Button(teacher,text="Show ",relief=RAISED,bg="grey",fg="black",font="Helvetica 8 bold",command=xyz)
               # rollbutton.place(x=250,y=200,anchor="center")
                tbutton.pack(side="bottom") 
                tbutton.config(height=2,width=20)
            
                teacher.mainloop()
                
            teacherlogin=Button(yes,text="Teacher Login",relief=RAISED,bg="grey",fg="black",font="Helvetica 8 bold",command=fixed2)
            teacherlogin.place(x=300,y=130,anchor="center")
            teacherlogin.config(height=2,width=15)
            
            def fixed3():
                
            presenty=Button(yes,text="Go For Attendance",relief=RAISED,bg="grey",fg="black",font="Helvetica 8 bold",command=fixed3)
            presenty.place(x=250,y=250,anchor="center")
            presenty.config(height=2,width=20)               
            #studentlogin=Button(w1,text="Student Login",relief=RAISED,bg="grey",fg="black",font="Helvetica 8 bold",command=fixed1)
            #studentlogin.place(x=150,y=130,anchor="center")
            #studentlogin.config(height=2,width=15)
                           
            #teacherlogin=Button(w1,text="Teacher Login",relief=RAISED,bg="grey",fg="black",font="Helvetica 8 bold",command=fixed2)
            #teacherlogin.place(x=300,y=130,anchor="center")
            #teacherlogin.config(height=2,width=15)
                           
            #adminlogin=Button(w1,text="Admin Login",relief=RAISED,bg="grey",fg="black",font="Helvetica 8 bold",command=fixed)
            #adminlogin.place(x=350,y=150,anchor="center")
            #adminlogin.config(height=2,width=10)        
        else:
             messagebox.showerror("Invalid","Enter Valid day")
             messagebox.showinfo("Information","Enter The day In proper Cases eg.,monday,Monday")
    else:
           messagebox.showerror("Login Error","Check Admin Name or Password")
gobtn=Button(window,text="Go To Main Window",bg="grey",fg="black",font="Helvetica 8 bold",command=clicked)
gobtn.place(x=250,y=275,anchor="center")


window.mainloop()