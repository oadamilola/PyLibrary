# F227110
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from datetime import date
from database import returning
from database import isavailable
from database import isvalid

                     
def returnbook(text):
    '''
    the function called when the returnbutton is clicked.This function updates the logfile if the input is valid and the book is not available 
    '''
    if text=="":
        messagebox.showerror("Error","Please enter the Book's ID to return a book")
    elif isvalid(text) != True:
        messagebox.showerror("Error","Invalid Book ID")
    else:
        row= isavailable(text) 
        if row == None:
            messagebox.showerror("Error","Book is already available")
        else: 
            datee=date.today() 
            datee=datee.strftime("%d-%m-%Y") #formats the date
            reserved=returning(text,datee,row) #returns the book by updating the logfile and checks if book is reserved
            sentence="The system has been updated.\nThis book has been reserved by "+ reserved 
            if reserved != '\n':
                messagebox.showinfo("Success",sentence) #displays message to user saying which memeber ID has reserved the book
            else:
                messagebox.showinfo("Success","The system has been updated")



def retur(men):
    '''
    defines the frame for the returnbooks screen 
    '''
    frame= Frame(bg ="#C19A6B")
    frame.grid(row=0,column=0, padx=0, pady=0)
    frame.config(bg="#C19A6B", width=1000, height=785)

    returnlabel=Label(frame, text="Enter Book ID to Return a Book",font=("times new roman",13,"bold"),fg="black",bg="#C19A6B")
    returnlabel.place(x=400, y=170)
        
    box=ttk.Entry(frame,font=("times new roman",10,"bold"))
    box.place(x=250, y=204,width=550,height=30)

    returnb=Button(frame,text="Return Book",command=lambda:returnbook(box.get()),font=("times new roman",11,"bold"),
    bd=3,relief=RAISED,borderwidth=1,bg="#C19A6B",activebackground="#C19A6B",cursor="hand2")
    returnb.place(x=440,y=350,width=140,height=30)

    back=Button(frame,text="Back",font=("times new roman",11,"bold"),command=lambda:men(),bd=3,relief=RAISED,borderwidth=1,
    bg="#C19A6B",activebackground="#C19A6B",cursor="hand2")
    back.place(x=30,y=30,width=140,height=30)



if __name__=="__main__":
    returnbook("10256")
    returnbook("10")
    returnbook("Me")
    returnbook("10257")
    print("book return tested")
                            
