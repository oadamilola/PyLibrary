# F227110
#the following section imports all modules needed for menu
from tkinter import*
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from booksearch import search
from bookCheckout import checking
from bookReturn import retur
from datetime import date
from bookSelect import bookselect
import matplotlib.pyplot as plt #imports matplotlib module and calls it plt 

def win():
    '''
     function that creates the window Library Database
    '''
    window=tk.Tk()
    window.title("Library Database")
    window.geometry("1000x785+250+0")
    window.configure(bg='#C19A6B')
    men()
    window.mainloop()

def men(): 
    '''
    function that creates the main menu frame and displays buttons that link to the other frames
    '''
    frame= Frame(bg ="#C19A6B")
    frame.grid(row=0,column=0, padx=0, pady=0)
    frame.config(bg="#C19A6B", width=1000, height=785)

    title=Label(frame, text="Library Management System",font=("times new roman",13,"bold"),fg="black",bg="#C19A6B")
    title.place(x=400, y=180)

    b1=Button(frame,text="Search For a Book",font=("times new roman",11,"bold"),command=lambda:search(men),bd=3,relief=RAISED,
    borderwidth=1,bg="#C19A6B",activebackground="#C19A6B",cursor="hand2")
    b1.place(x=430,y=250,width=140,height=30)

    b2=Button(frame,text="Return a Book",font=("times new roman",11,"bold"),command=lambda:retur(men),bd=3,relief=RAISED,
    borderwidth=1,bg="#C19A6B",activebackground="#C19A6B",cursor="hand2")
    b2.place(x=430,y=300,width=140,height=30)

    b3=Button(frame,text="Checkout a Book",font=("times new roman",11,"bold"),command=lambda:checking(men),bd=3,relief=RAISED,
    borderwidth=1,bg="#C19A6B",activebackground="#C19A6B",cursor="hand2")
    b3.place(x=430,y=350,width=140,height=30)

    b3=Button(frame,text="Purchase Books",font=("times new roman",11,"bold"),command=lambda:bookselect(men),bd=3,relief=RAISED,
    borderwidth=1,bg="#C19A6B",activebackground="#C19A6B",cursor="hand2")
    b3.place(x=430,y=400,width=140,height=30)

win() #calls the function that defines the main window
