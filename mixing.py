from tkinter import *
from tkinter import messagebox
import sqlite3
from PIL import ImageTk,Image

root=Tk()

root.geometry("1650x1000")
root.title("Sighn up page")
root.config(bg="grey")

my_Image=ImageTk.PhotoImage(Image.open("/Users/ujjwalpariyar/Downloads/Rectangle 21.png"))
myLabel=Label(root,image=my_Image)
myLabel.place(x=0,y=0)

conn=sqlite3.connect("new.db")

c=conn.cursor()
# c.execute(""" CREATE TABLE User(
#     first_name text,
#     last_name text,
#     email text,
#     password text,
#     confirm_password text

#   )""")

# print("Data stored Succesfully")

def next():
    global loog
    loog=Toplevel()
    loog.title("Login")
    conn=sqlite3.connect("new.db")
    
    conn.commit()
    conn.close()

def submit():
    conn=sqlite3.connect("new.db")
    
    c=conn.cursor()
    
    c.execute("INSERT INTO user values(:first_name, :last_name, :email, :password, :confirm_password)",{
        "first_name":first_name.get(),
        "last_name":last_name.get(),
        "email":email.get(),
        "password":password.get(),
        "confirm_password":confirm_password.get()
        
    })
   
    messagebox.showinfo("user" , "Data Saved successfully")
    conn.commit()
    conn.close()      

def login():
    root.destroy()
    roots=Tk()
    roots.title("Login")
    roots.geometry("1650x1000")
    # conn=sqlite3.connect("new.db")
    my_mage=ImageTk.PhotoImage(Image.open("/Users/ujjwalpariyar/Downloads/5608BAD8-7FA8-4234-A337-039BD3B859DD 1.png"))
    myLabel=Label(roots,image=my_mage)
    myLabel.place(x=0,y=0)

    logo=Label(roots,text="SUMS FOOD",bg="dark orange", font="Inter""50""BOLD")
    logo.place(x=610,y=0)

    log=Label(roots,text="LOGIN TO SUMS FOOD",font="Inter""50")
    log.place(x=750,y=0)

    #labeling
    email=Label(roots,text="Email:",font="36")
    email.place(x=610,y=200)

    password=Label(roots,text="Password:",font="36")
    password.place(x=610,y=300)

    #entry
    email_img=PhotoImage(file="/Users/ujjwalpariyar/Downloads/289762887_443851223922231_8306552022131947821_n.png")
    email_label=Label(roots,image=email_img,border=0)
    email_label.place(x=710,y=200)

    email_entry = Entry(roots,border=0,font="20")
    email_entry.place(x=717,y=206)

    password_img=PhotoImage(file="/Users/ujjwalpariyar/Downloads/289762887_443851223922231_8306552022131947821_n.png")
    password_label=Label(roots,image=password_img,border=0)
    password_label.place(x=710,y=300)

    password_entry = Entry(roots,border=0,font="20")
    password_entry.place(x=717,y=306)

    #login button
    login_img=PhotoImage(file="/Users/ujjwalpariyar/Downloads/289762887_443851223922231_8306552022131947821_n.png")
    login_label=Label(roots,image=login_img,border=0)
    login_label.place(x=750,y=400)


    login_entry = Button(roots,width=20,border=0,text="Login",bg="white")
    login_entry.place(x=757,y=401)
                                           
    tex=Label(roots,text="Don't have an account?",font="BOLD")
    tex.place(x=750,y=450)

    #signup
    up_img=PhotoImage(file="/Users/ujjwalpariyar/Downloads/289835981_546513673818548_8080905862144376496_n.png")
    up_label=Label(roots,image=up_img,border=0)
    up_label.place(x=930,y=450)

    up_entry = Button(roots,border=0,text="Sign up",bg="dark orange")
    up_entry.place(x=935,y=454)

    conn.commit()
    conn.close()   


#Creating the labels.
# text. configure(font=("Times New Roman", 20, "italic"))

first_name=Label(root,text="First Name",fg="Black",bg="White",font=("Times New Roman",20,"italic"))
first_name.place(x=600,y=100)

last_name=Label(root,text="Last Name",fg="Black",bg="White",font=("Times New Roman",20,"italic"))
last_name.place(x=600,y=150)

email=Label(root,text="Email",fg="Black",bg="White",font=("Times New Roman",20,"italic"))
email.place(x=600,y=200)

password=Label(root,text="Password",fg="Black",bg="White",font=("Times New Roman",20,"italic"))
password.place(x=600,y=250)

confirm_password=Label(root,text="Confirm Password",fg="Black",bg="White",font=("Times New Roman",20,"italic"))
confirm_password.place(x=600,y=300)

sighntext=Label(root,text="SIGN UP TO SUMS FOOD",fg="Black",bg="White",font=("Times New Roman",30,"italic"))
sighntext.place(x=750,y=0)

#Creating an empty label for input/entry for the labels.
first_name=Entry(root,width=30,bd=3)
first_name.place(x=760,y=100)

email=Entry(root,width=30,bd=3)
email.place(x=760,y=150)

last_name=Entry(root,width=30,bd=3)
last_name.place(x=760,y=200)

password=Entry(root,width=30,bd=3)
password.place(x=760,y=250)

confirm_password=Entry(root,width=30,bd=3)
confirm_password.place(x=760,y=300)

# Now Create buttons to login or for sighnup.
Sighnup=Button(root,text='Sign up',bd=2,fg="Black",bg="White",command=submit,padx=5,pady=5)
Sighnup.place(x=860,y=360)

# Button to pass into login page
login_btn=Button(root,text="Login",bd=2,bg="White",fg="Black",command=login,padx=5,pady=5)
login_btn.place(x=867,y=400)

facebok=Button(root,text="Facebook",padx=5,pady=5)
facebok.place(x=810,y=440)

google=Button(root,text="GOOGLE",bg="White",fg="Black",padx=5,pady=5)
google.place(x=920,y=440)

conn.commit()
conn.close()

root.mainloop()