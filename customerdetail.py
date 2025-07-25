from tkinter import *
from tkinter import ttk
import mariadb

def data_get():
    customer = com.get()
    conn = mariadb.connect(
        host ="localhost",
        user ="root",
        password ="",
        database ="chatraclg"
    )
    mycursor = conn.cursor()
    mycursor.execute("SELECT name,email,mobile,address FROM customer WHERE name='"+customer+"'")
    result = mycursor.fetchone()
   
    if result:
        name, email, mobile, address = result
        w_label1.config(text = name)
        wb_label1.config(text = email)
        temp_label1.config(text = mobile)
        per_label1.config(text = address)
    else:
        w_label1.config(text = "Not Found")
        wb_label1.config(text = "")
        temp_label1.config(text = "")
        per_label1.config(text = "")

    conn.close()

win = Tk() 
win.title("Customer Details")
win.config(bg= 'blue')
win.geometry("500x570")

title_label = Label(win, text='Customer Details', font=("Time Nee Roman",30,"bold"))
title_label.place(x=25,y=50,height=50,width=450)

customer = StringVar()
com = ttk.Combobox(win, font=("Times Nee Roman" , 20, "bold"), textvariable = customer)
com.place(x=25, y=120, height=50, width=450)

def load_customers():
    try:
        conn = mariadb.connect(
            host="localhost",
            user="root",
            password="",
            database="chatraclg"
        )
        mycursor = conn.cursor()
        mycursor.execute("SELECT name FROM customer")
        names = [row[0] for row in mycursor.fetchall()]
        com['values'] = names
        conn.close()
    except Exception as e:
        print("Error loading customer names", e)

load_customers()

w_label = Label(win, text="Name", font=("Time Nee Roman",20,"bold"))
w_label.place(x=25,y=250,height=50,width=220)
w_label1 = Label(win, text="", font=("Time Nee Roman",20,"bold"))
w_label1.place(x=250,y=250,height=50,width=220)

wb_label = Label(win, text="Email", font=("Time Nee Roman",20,"bold"))
wb_label.place(x=25,y=330,height=50,width=220)
wb_label1 = Label(win, text="", font=("Time Nee Roman",20,"bold"))
wb_label1.place(x=250,y=330,height=50,width=220)

temp_label = Label(win,text="Mobile", font=("Time Nee Roman",20,"bold"))
temp_label.place(x=25, y=400, height=50,width=220)
temp_label1 = Label(win,text="", font=("Time Nee Roman",20,"bold"))
temp_label1.place(x=250, y=400, height=50,width=220)

per_label = Label(win,text="Address", font=("Time Nee Roman",20,"bold"))
per_label.place(x=25, y=470, height=50,width=220)
per_label1 = Label(win,text="", font=("Time Nee Roman",20,"bold"))
per_label1.place(x=250, y=470, height=50,width=220)

done_button = Button(win,text="Customer Details", font=("Time Nee Roman",20,"bold"), command = data_get)
done_button.place(x=150, y=190, height=50,width=250)

win.mainloop()
