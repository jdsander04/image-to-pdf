import itopfuncs
import tkinter as itop
from tkinter import filedialog
from tkinter import ttk

parentFolder = "Select the parent folder"
output = "Select the output folder"
progress = 0;

def update_progress_bar(value):
    progress_bar["value"] = value
    root.update_idletasks()

def start_button_click():
    global parentFolder
    global output

    if not itopfuncs.is_valid_folder(parentFolder):
        print("Invalid parent folder path.")
    elif not itopfuncs.is_valid_folder(output):
        print("Invalid PDF output folder.")
    else:
        process_child_folders(parentFolder, output)

def selectParentFolder():
    global parentFolder
    parentFolder = filedialog.askdirectory(title="Select the parent folder folder")
    
def selectOuputFolder():
    global output
    output = filedialog.askdirectory(title="Select the output folder")

def process_child_folders(parent_folder, pdf_placement):
    global progress
    child_folders = itopfuncs.get_child_folders(parent_folder)
    num_folders = len(child_folders)

    print("Processing child folders:")
    for i, folder_name in enumerate(child_folders, start=1):
        child_folder = itopfuncs.get_child_folder_path(parent_folder, folder_name)
        pdf_name = folder_name + '.pdf'

        pdf_name = itopfuncs.adjust_pdf_name(pdf_name)

        output_file = itopfuncs.get_output_file_path(pdf_placement, pdf_name)
        
        progress = (i/num_folders)*100

        #Progress = math.floor((i/num_folders)*20)
        #bar = Progress*chr(9619)+'_'*(20-Progress)
        #terminal.write("\r["+bar+"]  " + str(i) + "/" + str(num_folders))

        try:
            itopfuncs.convert_images_to_pdf(child_folder, output_file)
        except Exception as e:
            print(f"Error converting images in folder '{child_folder}': {str(e)}")

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

progress_bar = ttk.Progressbar(root, orient="horizontal", mode="determinate", length=300)
progress_bar.pack(pady=20)

root.mainloop()