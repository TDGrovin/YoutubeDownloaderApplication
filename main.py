#Youtube Downloader Application
#Authors:-
#Aviral Sheoran
#Bhavya Bhaskar
#Grovin Singh Atwal

#Default location for links file is in the same directory as the application under the name "links.txt"
#Default download lcocation for media is in the same directory as the application, in the folder "Downloads"


from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
import threading
import process

#Dictionary to store information about the video#
information = {
    "title" : "default_title",
    #Size is in MegaBytes
    "size" : "default_size",
    "length" : "default_length",
    #Status includes Download Successfull or Unsuccessfull
    #If status is "default_status", then download is successfull
    #For any other case, the download is unsuccessfull and status must be changed to the error generated
    "status" : "default_status",  
    "url" : "default_url"
}

myApplication = Tk()
myApplication.title('Youtube Downloader')
myApplication.geometry("")


#Heading
Label(myApplication, text="Youtube Video Downloader", font=("Arial", 25), anchor=CENTER).grid()
Label(myApplication, text="\nYou can either enter Youtube Video Link or Provide a text file with all the links mentioned in it and we will download it for you", font=("Arial", 15), anchor=CENTER).grid()
Label(myApplication, text="Video will be saved in the Downloads Folder, located in the location of this file", font=("Arial", 15), anchor=CENTER).grid()

#Interface Selector
#Function
def interfaceChange():
    currentInterface = v.get()
    if(currentInterface == 'Link'):
         fileInterface.grid_forget()
         linkInterface.grid()
    elif (currentInterface == 'File'):
        linkInterface.grid_forget()
        fileInterface.grid()
        
#GUI
interfaceSelector = Frame(myApplication)
interfaceSelector.grid()
v = StringVar()
Radiobutton(interfaceSelector, text='Provide Link', value='Link', variable=v, command=interfaceChange, ).grid(row=0, column=0)
Radiobutton(interfaceSelector, text='Provide File', value='File', variable=v, command=interfaceChange).grid(row=0, column=1)

#Interfaces
#Functions
#Creates a thread which calls the function to download the media from the given link
def createNewThread_downloadFromLink():
    status.configure(text="Downloading........")
    status.grid()
    t1 = threading.Thread(target=downloadFromLink)
    t1.start()

#Function to download media from link    
def downloadFromLink():
    link = input.get(1.0,"end-1c")
    information.update({"url" : link})
    process.Download(**information)
    status.grid_forget()
    
#Creates a thread which calls the function to download the media from the given file
def createNewThread_downloadFromFile():
    status.configure(text="Downloading........")
    status.grid()
    t2= threading.Thread(target=downloadFromFile)
    t2.start()
    
#Function to download media from file, it iterates over each link mentioned in the file
#and calls the downloadFromLink() function
def downloadFromFile():
    file = open("links.txt",)
    for link in file:
        information.update({"url" : link})
        process.Download(**information)
    status.grid_forget()
    
#Browsing Function   
def browseFile():
    fileName = filedialog.askopenfile(
                                    initialdir = "D:\Coding Projects\Python\Youtube Downloader",
                                    title = "Select a file",
                                    filetypes = ( ("Text Files", "*txt"), ("All Files", ".") ) )
    fileField.delete(1.0, "end-1c")
    fileField.insert("end-1c", fileName.name)

#Link Interface
linkInterface = Frame(myApplication)
Label(linkInterface, text="Enter link below").grid()
input=Text(linkInterface, height=1, width=30, yscrollcommand=1)
input.grid()
Button(linkInterface, text="Download", width=20, command=createNewThread_downloadFromLink).grid()

#File Interface
fileInterface = Frame(myApplication)
Label(fileInterface, text="Provide file below").grid(row=0, column=0)
fileField = Text(fileInterface, height=1, width=30, yscrollcommand=1)
fileField.insert(1.0,"Enter Location Here!")
fileField.grid(row = 1, column=0)
Button(fileInterface, text="Browse", command=browseFile).grid(row=1, column=1)
Button(fileInterface, text="Download", command=createNewThread_downloadFromFile).grid()

#Status Label
#It appears when the file/link is being processed, otherwise it stays hidden
status = Label(myApplication, text="")

myApplication.mainloop()