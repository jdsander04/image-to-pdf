import itopfuncs
import os
import tkinter as itop
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
import re

parentFolder = "Select the parent folder"
output = "Select the output folder"
Errors = ""
consoleText = ""

# def newError(error):
#     ct = datetime.datetime.now()
#     if not error.endswith("\n"):
#         error += "\n"


# def newProgressUpdate(update):
#     if not update.endswith("\n"):
#         update += "\n"
#     global consoleText
#     consoleText += update
#     update_progress_console()

def update_progress_bar(value):
    progress_bar["value"] = value
    root.update_idletasks()

def update_progress_console():
    global consoleText
    # output_console.config(text=consoleText+"\n"+Errors)
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
    if parentFolder != "":
        parentFolderButton.config(text=parentFolder)
    
def selectOutputFolder():
    global output
    output = filedialog.askdirectory(title="Select the output folder")
    if output != "":
        outputFolderButton.config(text=output)

def process_child_folders(parent_folder, pdf_placement):
    global consoleText
    emptyList = []
    child_folders = itopfuncs.get_child_folders(parent_folder)
    if not child_folders:  # Check if the list is empty
        child_folders.append(parent_folder)
    num_folders = len(child_folders)

    progress_step = 100 / num_folders  # Calculate the step for each folder

    print("Processing child folders:")
    total_progress = 0
    for i, folder_name in enumerate(child_folders, start=1):
        if child_folders[0] == parent_folder:
            child_folder = parent_folder
        else:
            child_folder = itopfuncs.get_child_folder_path(parent_folder, folder_name)
        
        pdf_name = folder_name + '.pdf'

        pdf_name = adjust_pdf_name(pdf_name)

        output_file = itopfuncs.get_output_file_path(pdf_placement, pdf_name)

        if not os.path.exists(output_file):
            try:
                itopfuncs.convert_images_to_pdf(child_folder, output_file)
            except Exception as e:
                print(f"Error converting images in folder '{child_folder}': {str(e)}\n")
        else:
            print(output_file + " already exists")
        
        total_progress += progress_step
        update_progress_bar(total_progress)

    print("\nProcessing completed!")

def adjust_pdf_name(pdf_name):
    pdf_name = re.sub(r'^.*?(Chapter)', r'\1', pdf_name)
    match = re.search(r'\d+', pdf_name)
    if match:
        number = int(match.group())
        pdf_name = str(number).zfill(4) + " " + pdf_name
    return pdf_name


root = itop.Tk()

root.title("iTop (hot girls)")

root.configure(bg="#474973")

label = itop.Label(root, text="Welcome to the image to pdf python script!")
label.pack(pady=5, side="top")
label.configure(bg="#474973", state="disabled")

progress_bar = ttk.Progressbar(root, orient="horizontal", mode="determinate", length=250, maximum=100)
progress_bar.pack(pady=5, padx=5, side="bottom")

button = itop.Button(root, text="Images to PDF!", command=start_button_click, width=35)
button.pack(pady=5, padx=5, side="bottom")
button.configure(bg="#A69CAC")

outputFolderButton = itop.Button(root, text=output, command=selectOutputFolder, width=35)
outputFolderButton.pack(pady=5, padx=5, side="bottom")
outputFolderButton.configure(bg="#A69CAC")

parentFolderButton = itop.Button(root, text=parentFolder, command=selectParentFolder, width=35)
parentFolderButton.pack(pady=5, padx=5, side="bottom")
parentFolderButton.configure(bg="#A69CAC")

root.mainloop()