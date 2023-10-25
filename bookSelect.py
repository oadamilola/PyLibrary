# F227110
from tkinter import*
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from database import gettitles
from database import getIDs
from database import timesborrowed
from database import getgenres
from database import getprices
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



def bookselect(men):
    '''
    bookselect defines the frame for the bookselect screen and defines widgets inside
    '''
    frame1= Frame(bg ="#C19A6B")
    frame1.grid(row=0,column=0, padx=0, pady=0)
    frame1.config(bg="#C19A6B", width=1000, height=785)

    searchlabel=Label(frame1, text="Enter Budget to Generate Book Purchase Suggestion to Nearest Whole Number",
    font=("times new roman",13,"bold"),fg="black",bg="#C19A6B")
    searchlabel.place(x=215, y=170)
        
    budget=ttk.Entry(frame1,font=("times new roman",10,"bold"))
    budget.place(x=250, y=204,width=550,height=30)

    gen=Button(frame1,text="generate",command=lambda:checkbudge(frame1,budget.get()),font=("times new roman",11,"bold"),
    bd=3,relief=RAISED,borderwidth=1,bg="#C19A6B",activebackground="#C19A6B",cursor="hand2")
    gen.place(x=100,y=204,width=140,height=30)

    back=Button(frame1,text="Back",font=("times new roman",11,"bold"),command=lambda:men(),bd=3,relief=RAISED,
    borderwidth=1,bg="#C19A6B",activebackground="#C19A6B",cursor="hand2")
    back.place(x=30,y=30,width=140,height=30)


def checkbudge(frame1,budget):
    '''
    checkbudge checks that the value inputed is a number
    '''
    if budget.isdigit() != True:
        messagebox.showerror("Error","Entry Not Valid")
    else:
        generate(frame1,float(budget))


def generate(frame,budget):
    '''
    generate is the main function in which the tables are all generated in
    '''
    IDs=getIDs() #gets a list of all book IDs
    titles=gettitles()
    numberoftimes=timesborrowed(IDs) #gets a list of number of times each book has been borrowed
    genres=getgenres() #gets a list of every singe genre 
    nfreq=genretally(numberoftimes,genres) #creates a new list of how many times each genre has been borrowed based on times book was borrowed
    ngenres=onegenre(genres,nfreq)
    ffreq=finalfreq(ngenres,genres,nfreq)

    mloaned(frame,IDs,numberoftimes,ngenres,ffreq,titles,budget) 


def mloaned(frame,IDs,numberoftimes,ngenres,ffreq,titles,budget):
    '''    
    mloaned produces a graph that shows how many times each book title has been loaned.IDs is a list of the book IDs,numberoftimes is a list the number of
    times each book has been borrowed,ngenres is a list of one occurence of all genres, ffreq is a list of the total accumulated frequency of how many times that
    genre has been borrowed
    '''
    figure=plt.figure()
    plt.barh(titles,numberoftimes,color="#86c0d1") #produces bars horizontally
    graph1= FigureCanvasTkAgg(figure,frame)
    graph1.get_tk_widget().place(x=115,y=240,width=680,height=350)
    genrebutn=Button(frame,text="Popular Genres",command=lambda:popgenres(frame,IDs,numberoftimes,ngenres,ffreq,titles,budget),
    font=("times new roman",11,"bold"),bd=3,relief=RAISED,borderwidth=1,bg="#C19A6B",activebackground="#C19A6B",cursor="hand2") 
    genrebutn.place(x=820,y=350,width=140,height=30)
    mlbutn=Button(frame,text="Most Loaned",font=("times new roman",11,"bold"),bd=3,relief=RAISED,borderwidth=1,bg="#C19A6B",
    activebackground="#C19A6B",cursor="hand2")
    mlbutn.place(x=820,y=400,width=140,height=30)
    mlbutn=Button(frame,text="Budget Split",command=lambda:budgetsplit(frame,IDs,numberoftimes,ngenres,ffreq,titles,budget),
    font=("times new roman",11,"bold"),bd=3,relief=RAISED,borderwidth=1,bg="#C19A6B",activebackground="#C19A6B",cursor="hand2")
    mlbutn.place(x=820,y=450,width=140,height=30)
    plt.tight_layout()



def popgenres(frame,IDs,numberoftimes,ngenres,ffreq,titles,budget):
    '''
    pop genres produces a graph showing how many times each genre has been borrowed
    '''

    figure=plt.figure()
    axis=plt.axes()
    plt.barh(ngenres,ffreq,color="#86c0d1")
    graph2= FigureCanvasTkAgg(figure,frame)
    graph2.get_tk_widget().place(x=115,y=240,width=680,height=350)
    genrebutn=Button(frame,text="Popular Genres",font=("times new roman",11,"bold"),bd=3,relief=RAISED,borderwidth=1,bg="#C19A6B",
    activebackground="#C19A6B",cursor="hand2")
    genrebutn.place(x=820,y=350,width=140,height=30)
    mlbutn=Button(frame,text="Most Loaned",command=lambda:mloaned(frame,IDs,numberoftimes,ngenres,ffreq,titles,budget),
    font=("times new roman",11,"bold"),bd=3,relief=RAISED,borderwidth=1,bg="#C19A6B",activebackground="#C19A6B",cursor="hand2")
    mlbutn.place(x=820,y=400,width=140,height=30)
    mlbutn=Button(frame,text="Budget Split",command=lambda:budgetsplit(frame,IDs,numberoftimes,ngenres,ffreq,titles,budget),
    font=("times new roman",11,"bold"),bd=3,relief=RAISED,borderwidth=1,bg="#C19A6B",activebackground="#C19A6B",cursor="hand2")
    mlbutn.place(x=820,y=450,width=140,height=30)
    plt.tight_layout()


   
def budgetsplit(frame,IDs,numberoftimes,ngenres,ffreq,titles,budget):
    '''
    budgetsplit is a function that produces a suggestion on how to split the budget and buy more copies of popular books. it provides this in the form of
    a Treeview
    '''
    bsplit=topbooks(titles,numberoftimes)
    num=int(len(bsplit)/2)
    toptitles=[]
    topfreqs=[]
    total=0
    for i in range(0,num):
        toptitles.append(bsplit[i])
    for i in range(num,len(bsplit)):
        topfreqs.append(bsplit[i])
        total=total+bsplit[i]
    prices=getprices(toptitles)
    genrebutn=Button(frame,text="Popular Genres",command=lambda:popgenres(frame,IDs,numberoftimes,ngenres,ffreq,titles,budget),
    font=("times new roman",11,"bold"),bd=3,relief=RAISED,borderwidth=1,bg="#C19A6B",activebackground="#C19A6B",cursor="hand2")
    genrebutn.place(x=820,y=350,width=140,height=30)
    mlbutn=Button(frame,text="Most Loaned",command=lambda:mloaned(frame,IDs,numberoftimes,ngenres,ffreq,titles,budget),
    font=("times new roman",11,"bold"),bd=3,relief=RAISED,borderwidth=1,bg="#C19A6B",activebackground="#C19A6B",cursor="hand2")
    mlbutn.place(x=820,y=400,width=140,height=30)
    mlbutn=Button(frame,text="Budget Split",font=("times new roman",11,"bold"),bd=3,relief=RAISED,borderwidth=1,bg="#C19A6B",
    activebackground="#C19A6B",cursor="hand2")
    mlbutn.place(x=820,y=450,width=140,height=30)
    budgetdisplay(frame,toptitles,topfreqs,total,prices,budget)


def budgetdisplay(frame,toptitles,topfreqs,total,prices,budget):
    '''
    budgetdisplay defines the treeview which displays the suggestions on books to purchase more copies of and how many to buy of each based on the Budget
    variable total is used to calculate a percentage of budget for each book
    '''
    resultsbox=ttk.Treeview(frame,columns=('Title', 'No. of Copies', 'Total Price'),selectmode="browse")
    resultsbox['show']='headings'
    resultsbox.column('Title',width=140,anchor=CENTER,stretch=tk.YES)
    resultsbox.column('No. of Copies',width=140,anchor=CENTER,stretch=tk.YES)
    resultsbox.column('Total Price',anchor=CENTER,width=100,stretch=tk.YES)
    resultsbox.heading('Title',text="Title")
    resultsbox.heading('No. of Copies',text="No. of Copies")
    resultsbox.heading('Total Price',text="Total Price")
    resultsbox.place(x=320,y=600,height=140)
    for i in range(0,len(toptitles)):
        totalval=budgett(total,budget,topfreqs[i])
        copies=copynum(totalval,prices[i])
        resultsbox.insert(parent='',index=i,iid=i,values=(toptitles[i],copies,totalval))



def budgett(total,budgetinp,freq):
    '''
    function that calculates a percentage of the budget to be spent on the given book
    '''
    percent= round((freq/total),2)
    value=round((float(percent)*float(budgetinp)),2)
    return value
 

def copynum(value,price):
    '''
    function that calculates the number of copies that can be afforded with the alocated percentage of the budget
    '''
    copies=round(float(value)/float(price))
    return copies
    

def genretally(freq,genres):
    '''
    function that duplicates the number of times borrowed for each book and stores it in a list to correlate to their two genres
    '''
    newfreq=[]
    count=0
    for i in range(0,len(genres)):
        if i == 0 :
            newfreq.append(freq[i])
        elif i%2 ==0: #checks if the index is even
            newfreq.append(freq[count])   
        else:
            newfreq.append(freq[count])
            count=count+1 #count increase whenever the index is odd
    return newfreq
        

def onegenre(genres,freq):
    '''
    function that creates a list of all the genres of books, with no repeats
    '''
    ngenres=[]
    for i in range(0,len(genres)):
        found=False
        for c in range(0,len(ngenres)):
            if genres[i]==ngenres[c]:
                found=True
            else:
                ()
        if found==False:
            ngenres.append(genres[i])
        else:
            ()
    return ngenres




def finalfreq(onegenre,genres,freq):
    '''
    function that adds up the sum of how many times eac instance of every genre has been borrowed and creates
    '''
    nfreq=[]
    for i in range(0,len(onegenre)):
        count=0
        for c in range(0,len(genres)):
            if onegenre[i]==genres[c]:
                count= count+freq[c]
            else:
                ()
        nfreq.append(count)
    return nfreq




def topbooks(lists,freq):
    '''
    topbooks takes a two lists the first a list of titles and the second a list of integers and then checks the integer list to find the biggest
    value and then creates a new list of a minimum length of 4 with the titles of the books with the highest corresponding integers (timesborrowed)
    it then concatenates the two lists and returns them as one
    '''

    top=[]
    topfreqs=[]
    max=freq[0]
    place=0
    for i in range(0,len(freq)):
        if freq[i]>=max:
            max=freq[i]
            place=i
        else:
            ()
    while len(top) <4:
        for i in range(0,len(freq)):
            if freq[i]==max:
                top.append(lists[i])
                topfreqs.append(max)
            else:
                ()
        max=max-1
    for i in range(0,len(topfreqs)):
        top.append(topfreqs[i])
    return top
        

