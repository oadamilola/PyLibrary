# F227110
from tkinter import*
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from database import searching
from database import displayresults
from database import isavailable



def searchit(frame,text):
    '''
    searchit function returns the search results if any to the user once search button has been clicked
    '''
    matches=searching(text)
    if len(matches) == 0:
        messagebox.showerror("Error","No matches found")
            
    else:
        resultsbox=ttk.Treeview(frame,columns=('Book ID', 'Title', 'Author', 'Genre', 'Purchase Price', 'Purchase Date','Availability'),selectmode="browse")
        #creates treeview and following code defines the treeview 
        resultsbox['show']='headings'
        resultsbox.column('Book ID',width=70,anchor=CENTER,stretch=tk.YES)
        resultsbox.column('Title',width=140,anchor=CENTER,stretch=tk.YES)
        resultsbox.column('Author',width=140,anchor=CENTER,stretch=tk.YES)
        resultsbox.column('Genre',width=140,anchor=CENTER,stretch=tk.YES)
        resultsbox.column('Purchase Price',anchor=CENTER,width=100,stretch=tk.YES)
        resultsbox.column('Purchase Date',anchor=CENTER,width=90,stretch=tk.YES)
        resultsbox.column('Availability',anchor=CENTER,width=90,stretch=tk.YES)
        resultsbox.heading('Book ID',text="Book ID")
        resultsbox.heading('Title',text="Title")
        resultsbox.heading('Author',text="Author")
        resultsbox.heading('Genre',text="Genre")
        resultsbox.heading('Purchase Price',text="Purchase Price(£)")
        resultsbox.heading('Purchase Date',text="Purchase Date")
        resultsbox.heading('Availability',text="Availability")
        
        resultsbox.place(x=120,y=280) #places Treeview inside current frame
        count=-1
        for i in range (0,len(matches)):
            match=matches[i]
            result=displayresults(match,count) #stores the book information on the book in variable results
            available=isavailable(result[0])
            if available == None: #checks if the book is available
                result.append("Available")
            else:
                result.append("On Loan")
            #following line inserts values into treeview to display to user
            resultsbox.insert(parent='',index=i,iid=i,values=(result[0],result[1],result[2],result[3],result[4],result[5],result[6]))

           
def search(men):
    '''
    search function defines frame for booksearch module by passing the menu function as a parameter
    '''
    frame= Frame(bg ="#C19A6B")
    frame.grid(row=0,column=0, padx=0, pady=0)
    frame.config(bg="#C19A6B", width=1000, height=785)

    searchlabel=Label(frame, text="Search For Books Here",font=("times new roman",13,"bold"),fg="black",bg="#C19A6B")
    searchlabel.place(x=410, y=170)
        
    txtsearch=ttk.Entry(frame,font=("times new roman",10,"bold"))
    txtsearch.place(x=250, y=204,width=550,height=30)

    search=Button(frame,text="search",command=lambda:searchit(frame,txtsearch.get()),font=("times new roman",11,"bold"),
    bd=3,relief=RAISED,borderwidth=1,bg="#C19A6B",activebackground="#C19A6B",cursor="hand2") #calls searchit function which will return results from user input
    search.place(x=100,y=204,width=140,height=30)

    back=Button(frame,text="Back",font=("times new roman",11,"bold"),command=lambda:men(),bd=3,relief=RAISED,borderwidth=1,
    bg="#C19A6B",activebackground="#C19A6B",cursor="hand2") #displays menu screen when clicked
    back.place(x=30,y=30,width=140,height=30)

