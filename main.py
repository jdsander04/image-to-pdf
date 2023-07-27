import itopfuncs
import tkinter as itop
from tkinter import filedialog
from tkinter import ttk

parentFolder = "Select the parent folder"
output = "Select the output folder"
Errors = ""
consoleText = ""

def newError(error):
    if not error.endswith("\n"):
        error += "\n"
    global Errors
    Errors += error
    print(Errors)
    update_progress_console()

def newProgressUpdate(update):
    if not update.endswith("\n"):
        update += "\n"
    global consoleText
    consoleText += update
    update_progress_console()

def update_progress_bar(value):
    progress_bar["value"] = value
    root.update_idletasks()

def update_progress_console():
    global consoleText
    output_console.config(text=consoleText+"\n"+Errors)
    root.update_idletasks()

def start_button_click():
    global parentFolder
    global output

    if not itopfuncs.is_valid_folder(parentFolder):
        newError("Invalid parent folder path.")
    elif not itopfuncs.is_valid_folder(output):
        newError("Invalid PDF output folder.")
    else:
        process_child_folders(parentFolder, output)

def selectParentFolder():
    global parentFolder
    parentFolder = filedialog.askdirectory(title="Select the parent folder folder")
    
def selectOuputFolder():
    global output
    output = filedialog.askdirectory(title="Select the output folder")

def process_child_folders(parent_folder, pdf_placement):
    global consoleText
    child_folders = itopfuncs.get_child_folders(parent_folder)
    num_folders = len(child_folders)

    progress_step = 100 / num_folders  # Calculate the step for each folder

    print("Processing child folders:")
    total_progress = 0

    for i, folder_name in enumerate(child_folders, start=1):
        child_folder = itopfuncs.get_child_folder_path(parent_folder, folder_name)
        pdf_name = folder_name + '.pdf'

        pdf_name = itopfuncs.adjust_pdf_name(pdf_name)

        output_file = itopfuncs.get_output_file_path(pdf_placement, pdf_name)

        try:
            itopfuncs.convert_images_to_pdf(child_folder, output_file)
        except Exception as e:
            newError("Error converting images in folder '{child_folder}': {str(e)}\n")
        
        total_progress += progress_step
        update_progress_bar(total_progress)

       

    print("\nProcessing completed!")



root = itop.Tk()

root.title("iTop (hot girls)")

label = itop.Label(root, text="Welcome to the image to pdf python script!")
label.pack()

parentFolderButton = itop.Button(root, text=parentFolder, command=selectParentFolder)
parentFolderButton.pack()

outputFolderButton = itop.Button(root, text=output, command=selectOuputFolder)
outputFolderButton.pack()

button = itop.Button(root, text="Images to PDF!", command=start_button_click)
button.pack()

output_console = itop.Label(root, text = consoleText, width=40, height=10)
output_console.pack();

progress_bar = ttk.Progressbar(root, orient="horizontal", mode="determinate", length=200, maximum=100)
progress_bar.pack(pady=20)

root.mainloop()