#F227110
from tkinter import*
from tkinter import ttk
from tkinter import messagebox

def isavailable(title): 
    '''
    function that checks if book is available
    '''
    a=open(r"logfile.txt","r")
    row=0
    a.seek(0)
    for line in a:
        templist=line.split(',') #splits the line in the text file and stores it in a variable called templist
        if len(templist) > 1:
            if templist[0]== title:
                if templist[3]=="          ": #checks if the book has been returned
                    a.close()
                    return row #if book has not been returned the line index 'row' is returned
                else:
                    row=row+1
            else:
                row=row+1
        else:
             a.close()
             return None #if the ID did not match any of the ones in logfile or all logs of the book are shown to be returned, this means the
                #the book is available
            
def isvalid(bookid): 
    '''
    function that checks if bookid is valid, by checking it is in Book_info textfile
    '''
    a=open(r"Book_info.txt","r")
    a.seek(0)
    for line in a:
        templist=line.split(',')
        if len(templist) != 1:
            if templist[0]== bookid:
                a.close()
                return True #once the book has been found the value True is returned
            else:
                ()
    a.close()

def searching(text):
    '''
    function that finds the records matching the users search
    '''
    if text =="": #checks the user has entered a value
        messagebox.showerror("Error","Nothing Entered") 
    else:
        word=text
        word=word.lower() #makes every letter in variable word lowercase,allows for user input to not need to be case Sensitive
        matches=[]
        a=open(r"Book_info.txt","r")
        a.seek(0)
        for line in a:
            templist=line.split(',')
            if len(templist) == 6:
                if templist[2] != 'Author': #checks it is not the first line
                    author=templist[2].split(' ') 
                    authorfn=author[0].lower() #stores the authors firstname in variable fname
                    authorsn=author[1].lower() #stores the authors surname in variable sname
                    author = authorfn+" "+authorsn #concatenates author first and surname back together 
                    genres=templist[3].split(':')
                    if templist[1].lower()== word or author == word: #checks if title or author matches input
                        matches.append(templist[0])
                    elif word == authorfn or word == authorsn: #checks if author first or surname matches input
                        matches.append(templist[0])
                    elif genres[0].lower() == word or genres[1].lower() == word: #checks both genres
                        matches.append(templist[0])
                    else:
                        ()
                else:
                    ()
                    
            else:
                break
    return matches  # returns array of book IDs that matched user input         

def checkingout(bookid,membid,date): 
    '''
    function that updates logfile and checks out a book
    '''
    a=open(r"logfile.txt","a")
    a.write(bookid+","+membid+","+date+",          ,\n") #writes new record to end of logfile with checkout details
    a.close()

def returning(bookid,date,row): 
    '''
    function that returns a book by updating logfile by taking ID the current date and the row to be updated as parameters
    '''
    a=open(r"logfile.txt","r")
    file=a.readlines() 
    word=''
    a.close()
    old=file[row].split(',') #stores line to be updated in variable old
    old[3]=str(date) #appends the date to correct position in line
    reserved=old[4] #stores value held in reserved_by column in logfile
    for i in range(0,len(old)):
        if old[i] == "\n":
            word= word + str(old[i]) #if end of the line is reached no comma is written after value
        else:
            word= word + str(old[i])+"," #comma is written after value to seperate values in the record
    file[row]=word
    a=open(r"logfile.txt","w")
    a.writelines(file) #writes updated text back into logfile
    a.close()
    return reserved #returns value held in reserved_by column

def reservebook(memberid,row):
    '''
    function that reserves a book by updating logfile
    '''
    a=open(r"logfile.txt","r")
    file=a.readlines() 
    word=''
    a.close()
    old=file[row].split(',')
    if old[4] !='': #if book is not already reserved 
        old[4]=str(memberid) #appends the memberid to reserved_by column
        for i in range(0,len(old)):
            if i ==4:
                word= word + str(old[i])+"\n"
            else:
                word= word + str(old[i])+","
        file[row]=word
        a=open(r"logfile.txt","w")
        a.writelines(file) #updates logfile
        a.close()
        return True
    else:
        return False
    
def displayresults(match,count):
    '''
    function that displays all the matching results from the text file, it takes the row of the book as a parameter and a count that marks the last row where a match was found
    '''
    a=open(r"Book_info.txt","r")
    file=a.readlines()

    for c in range(1,len(file)): #loop that checks all lines of file
        line=file[c].split(',')
        if str(line[0]) == match and count<c :# checks if the book id of that line is the same as the one inputed to the function and if the line being
                                              # checked is a lower line than the last found match, to avoid repeats
            count=c #count is set to current line value for next search
            a.close()
            return line
        else: 
            ()
    a.close()

def getIDs(): 
    '''
    function that returns all the book ID's in the database
    '''
    IDs=[]
    a=open(r"Book_info.txt","r")
    for line in a:
        templist=line.split(',')
        if len(templist) == 6 and templist[2] != 'Author': #checks that the line is not empty and if it is the first line
            IDs.append(templist[0])
        else:
            ()
    return IDs    
    
def gettitles(): 
    '''
    function that returns all the book ID's in the database
    '''
    titles=[]
    a=open(r"Book_info.txt","r")
    for line in a:
        templist=line.split(',')
        if len(templist) == 6 and templist[2] != 'Author':
            titles.append(templist[1])
        else:
            ()
    return titles       

def timesborrowed(titles): 
    '''
    function that calculates how many times each book in the list titles has been borrowed
    '''
    number=[]
    for i in range (0,len(titles)): #checks the whole file line by line and reppeats for each value in titles
        count=0
        a=open(r"logfile.txt","r")
        for line in a:
            templist=line.split(',')
            if len(templist) >1:
                if templist[0]==titles[i]: #checks that the IDs match and if they do it adds one to the count
                    count=count+1
                else:
                    ()
            else:
                break
        number.append(count)
    return number

def getgenres(): 
    '''
    function that returns the genres of each book
    '''
    genres=[]
    a=open(r"Book_info.txt","r")
    for line in a:
        templist=line.split(',')
        if len(templist) == 6 and templist[2] != 'Author':
            genre=templist[3].split(':') #splits the sublist of genres into two
            genres.append(genre[0]) #adds each genre in order to new array of genres
            genres.append(genre[1])
        else:
            ()
    return genres        

def getprices(book):
    '''
    function that finds the purchase price of given
    '''
    a=open(r"Book_info.txt","r")
    a.seek(0) #sets the cursor to the beginning of the file
    prices=[]
    for line in a:
        templist=line.split(',')
        if len(templist) != 1:
            for i in range(0,len(book)):
                if templist[1]== book[i]: #checks that the book IDs match
                    prices.append(templist[4]) #adds the price stored in that value to the new array prices
                else:
                    ()
        else:
            ()
    a.close()
    return prices
