from tkinter import *
from tkinter import messagebox
import sqlite3


root=Tk()
root.title("SUMS Food")
root.geometry("1650x1000")

try:
    con=sqlite3.connect("hi.db")
    c=con.cursor()
    c.execute(""" CREATE TABLE datas(
        first_name text,
        last_name text,
        email text,
        password text,
        confirm_password text

    )""")
except:
    pass
#print("data stored successfully")


bg=PhotoImage(file="hh.png")
mylabel=Label(root,image=bg)
mylabel.place(x=0,y=0)


logo=Label(root,text="SUMS FOOD",bg="dark orange", font="Inter""50""BOLD")
logo.place(x=610,y=0)

log=Label(root,text="LOGIN TO SUMS FOOD",font="Inter""50")
log.place(x=750,y=0)

#labeling
email=Label(root,text="Email:",font="36")
email.place(x=610,y=200)

password=Label(root,text="Password:",font="36")
password.place(x=610,y=300)

#entry
email_img=PhotoImage(file="rectangle 1.png")
email_label=Label(root,image=email_img,border=0)
email_label.place(x=710,y=200)

email_entry = Entry(root,border=0,font="20")
email_entry.place(x=717,y=206)


password_img=PhotoImage(file="rectangle 1.png")
password_label=Label(root,image=password_img,border=0)
password_label.place(x=710,y=300)


password_entry = Entry(root,border=0,font="20")
password_entry.place(x=717,y=306)

#login button
login_img=PhotoImage(file="rectangle 2.png")
login_label=Label(root,image=login_img,border=0)
login_label.place(x=750,y=400)


login_entry = Button(root,border=0,text="Login",bg="white")
login_entry.place(x=810,y=401)

tex=Label(root,text="Don't have an account?",font="BOLD")
tex.place(x=750,y=450)

#signup
up_img=PhotoImage(file="rec.png")
up_label=Label(root,image=up_img,border=0)
up_label.place(x=955,y=450)


up_entry = Button(root,border=0,text="Sign up",bg="dark orange")
up_entry.place(x=962,y=453)

root.mainloop()

