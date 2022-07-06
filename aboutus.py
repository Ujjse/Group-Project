from tkinter import *
from tkinter import messagebox
import sqlite3


root=Tk()
root.title("About Us")


con=sqlite3.connect("new.db")

c=con.cursor()
# c.execute(""" CREATE TABLE datas(
#     first_name text,
#     last_name text,
#     username text,
#     password text
# )""")

# print("Data stored Succesfully")

bg=PhotoImage(file="hehe.png")
mylabel=Label(root,image=bg)
mylabel.pack()

img=PhotoImage(file="rectt.png")
llabel=Label(root,image=img,border=0)
llabel.place(x=0,y=0)

sums_lab=Label(root,text="SUMS FOOD",bg="dark orange",font="14""BOLD",fg="white")
sums_lab.place(x=3,y=15)

us=Label(root,text="About us: ",bg="dark grey",fg="white",font="ITALIC""50")
us.place(x=0,y=100)

tex=Label(root,text="\n SUMS FOOD  is the finest company in Nepal that delivers \n food from hundreds of popular restaurants. As a pioneer \n food delivery service provider, we are making life easier \n through online ordering.You can stay in home and order \n food you want through ur bed.\n  We know that your time is valuable and sometimes every \n minute in the day counts. That’s why we deliver! So you can \n spend more time doing the things you love. You can get \n anything from Indian food to high French cuisine by placing \n a simple order online through our website. Then just sit \n back, relax, and wait for your order to arrive. \n Sill not connected with us? \n Log in fom the top left bar if you already have an account \n or create an account with just one click and get connected \n with us.",bg="dark grey",fg="white",font="ITALIC""50")
tex.place(x=0,y=130)

#creating buttons
login_img=PhotoImage(file="rec.png")
login_label=Label(root,image=login_img,border=0,bg="grey")
login_label.place(x=200,y=550)


login_entry = Button(root,border=0,text="Sign Up",bg="dark orange")
login_entry.place(x=205,y=554)

up_img=PhotoImage(file="rec.png")
up_label=Label(root,image=up_img,border=0,bg="grey")
up_label.place(x=270,y=550)


up_entry = Button(root,border=0,text="Login",bg="dark orange")
up_entry.place(x=282,y=553)










root.mainloop()