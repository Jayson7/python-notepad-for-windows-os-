import tkinter 
import os 
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import * 

class Notepad:
    
    root = Tk()
    thisWidth = 300 
    thisHeight = 300 
    thisTextArea = Text(root)
    thisMenuBar = Menu(root)
    thisFileMenu = Menu(thisMenuBar, tearoff=0)
    thisEditMenu = Menu(thisMenuBar, tearoff=0)
    thisHelpMenu = Menu(thisMenuBar, tearoff=0)
    thisScrollBar = Scrollbar(thisTextArea)
    file = None 
    def __init__(self, **kwargs) -> None:
        #set icon 
        try:
            self.root.wm_iconbitmap('Notepad.ico')
        except:
            pass 
        # set windows size to 300 x 300 or more
        try: 
            self.thisWidth= kwargs['width']
        except KeyError:
            pass
        # set the window text 
        self.root.title('Untitled - Notepad')
        # Center the window 
        screenWidth = self.root.winfo_screenwidth()
        screenHeight = self.root.winfo_screenheight()
        # for left-align 
        left = (screenWidth / 2) - (self.thisWidth /2)
        # for right-align 
        top = (screenHeight / 2) - (self.thisWidth /2)
        # for top and bottom 
        self.root.geometry("%dx%d+%d" % (self.thisWidth, self.thisHeight, left, top))
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        #Add controls (widget)
        self.thisTextArea.grid(sticky=N + E + S + W)
        # to open new file 
        self.thisFileMenu.add_command(label='New', command=self.newFile)
        # to open existing file 
        self.thisFileMenu.add_command(label='open', command=self.openFile)
        # to save current file 
        self.thisFileMenu.add_command(label='open', command=self.saveFile)
        # to create a line in the dialog 
        self.thisFileMenu.add_separator()
        self.thisFileMenu.add_command(label='Exit', command=self.quitApplication)
        self.thisFileMenuBar.add_cascade(label='File', command=self.thisFileMenu)
        
        # to give a feature cut 
        self.thisEditMenu.add_command(label='Cut', command=self.cut)
        # to git a feature copy 
        self.thisEditMenu.add_command(label='Copy', command=self.copy)
        # To give feature of paste 
        self.thisEditMenu.add_command(label='Paste', command=self.paste)
        # To give feature of editing 
        self.thisEditMenu.add_cascade(label='Edit', command=self.edit)
        
        # to create a feature of description of the notepad 
        self.thisHelpMenu.add_command(label="About Notepad", command=self.showAbout)
        self.thisMenuBar.add_cascade(label="Help", menu=self.thisHelpMenu)
        self.root.config(menu=self.thisMenuBar)
        self.thisScrollBar.config(command=self.thisTextArea.yview)
        self.thisTextArea.config(yscrollcommand=self.thisScrollBar.set)
    # exit application 
    def quitApplication(self):
        self.root.destroy()
    
    def showAbout(self):
        showinfo('Notepad', 'Adebayo Abiodun (JaySon)')
    
    def openFile(self):
        self.file = askopenfilename(defaultextension='.txt', filetypes=[('All files', '*.*'), ('Text Documents', '*.txt')])
        
        if self.file == '':
            # no file opened 
            self.file = None
        else:
            # Try to open file 
            # set the window title 
            self.root.title(os.path.basename(self.file) + " - Notepad, Software Made by Jayson")
            self.thisTextArea.delete(1.0, END)
            file = open(self.file, 'r')
            self.thisTextArea.insert(1.0, file.read())
            file.close()
    def newFile(self):
        self.root.title('Untitled - Notepad')
        self.file = None
        self.thisTextArea.delete(1.0, END)
    def saveFile(self):
        if self.file == None:
            # save as new file 
            self.file = asksaveasfilename(initialfile='Untitled.txt', defaultextension='.txt', filetypes=[('All files', '*.*'), ('Text Documents', '*.txt')])
            if self.file == '':
                self.file = None
            else:
                # Try to save file 
                file = open(self.file, 'w')
                file.write(self.thisTextArea.get(1.0, END))
                file.close()
                self.root.title(os.path.basename(self.file) + " - Notepad, Software Made by Jayson")
        else:
            file = open(self.file, 'w')
            file.write(self.thisTextArea.get(1.0, END))
            file.close()
    def cut(self):
        self.thisTextArea.event_generate("<<Cut>>")
        
    def copy(self):
            self.thisTextArea.event_generate("<<Copy>>")
    def paste(self):
        self.thisTextArea.event_generate("<<Paste>>")
    def edit(self): 
        try:
            self.thisTextArea.edit_modified(0)
        except:
            pass
    def run(self):
        # run the application 
        self.root.mainloop()
    
# run the application
notepad = Notepad(width=600, height=400)
notepad.run()

        
        
            
    
    
    