# F227110
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from datetime import date
from database import isavailable
from database import isvalid
from database import checkingout
from database import reservebook


def check(bookid,memb):
    '''
    the function called when the checkout button is clicked.This function updates the logfile only if a valid memeber and book ID have been entered and
    the book is available
    '''
    if bookid=="" and memb=="": #checks if input is empty
        messagebox.showerror("Error","Please enter the Member's ID and the book ID")
    elif bookid=="":
        messagebox.showerror("Error","Please enter the book's ID")
    elif memb=="":
        messagebox.showerror("Error","Please enter the Member's ID")
    elif len(memb) != 4 or memb.isdigit()==False: #checks that member ID is valid
        messagebox.showerror("Error","Invalid Member ID")
    else:
        if isvalid(bookid) == True: #checks if the book ID is valid
            row=isavailable(bookid) #checks if the book is available or out on loan
            if row == None :
                messagebox.showinfo("Valid","Book Checkout Successful")
                datee=date.today()
                datee=datee.strftime("%d-%m-%Y")
                checkingout(bookid,memb,datee) #updates the logfile and checks out the book
            else:
                reserve=messagebox.askyesno("This Book Is Not Available","Would you like to reserve it instead?") 
                if reserve == True:
                    reserved=reservebook(memb,row) #calls reservebook function which reserves book if not already reserved
                    if reserved == True:
                        messagebox.showinfo("Success","Book Has been Reserved")
                    else:
                        messagebox.showerror("Error","This Book has already been reserved")
                else:
                    ()
        else:
            messagebox.showerror("Error","Invalid Book ID")

 
def checking(men):  
    '''
    defines the frame for the returnbooks screen
    '''
    frame= Frame(bg ="#C19A6B")
    frame.grid(row=0,column=0, padx=0, pady=0)
    frame.config(bg="#C19A6B", width=1000, height=785)

    titlelabel=Label(frame, text="Enter Book ID and Member ID to Checkout Book",font=("times new roman",13,"bold"),fg="black",bg="#C19A6B")
    titlelabel.place(x=300, y=170)

    idlabel=Label(frame, text="Book ID",font=("times new roman",13,"bold"),fg="black",bg="#C19A6B")
    idlabel.place(x=300, y=208)

    bookid=ttk.Entry(frame,font=("times new roman",10,"bold"))
    bookid.place(x=400, y=204,width=200,height=30)

    
    memblabel=Label(frame, text="Member ID",font=("times new roman",13,"bold"),fg="black",bg="#C19A6B")
    memblabel.place(x=300, y=256)
        
    memb=ttk.Entry(frame,font=("times new roman",10,"bold"))
    memb.place(x=400, y=254,width=200,height=30)

    checkoutbtn=Button(frame,text="checkout",command=lambda:check(bookid.get(),memb.get()),font=("times new roman",11,"bold"),bd=3,relief=RAISED,borderwidth=1,bg="#C19A6B",activebackground="#C19A6B",cursor="hand2")
    checkoutbtn.place(x=420,y=400,width=140,height=30)

    back=Button(frame,text="Back",font=("times new roman",11,"bold"),command=lambda:men(),bd=3,relief=RAISED,borderwidth=1,bg="#C19A6B",activebackground="#C19A6B",cursor="hand2")
    back.place(x=30,y=30,width=140,height=30)

    

if __name__=="__main__":
    check("10257","4550") #valid input
    check("10","4550") #invalid book ID
    check("10257","hh9f") #invalid Member ID
    check("","") #Empty
    print("checkout tested")



