import itopfuncs
import tkinter as itop
from tkinter import filedialog
from tkinter import ttk

parentFolder = "Select the parent folder"
output = "Select the output folder"

root = itop.Tk()

root.title("iTop (hot girls)")

label = itop.Label(root, text="Welcome to the image to pdf python script!")
label.pack()

parentFolderButton = itop.Button(root, text=parentFolder, command=itopfuncs.selectParentFolder)
parentFolderButton.pack()

outputFolderButton = itop.Button(root, text=output, command=itopfuncs.selectOuputFolder)
outputFolderButton.pack()

button = itop.Button(root, text="Images to PDF!", command=itopfuncs.start_button_click)
button.pack()

root.mainloop()