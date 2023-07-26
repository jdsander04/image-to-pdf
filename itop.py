import tkinter as itop
import os
import img2pdf
from PIL import Image
import re
from sys import stdout as terminal
from time import sleep
import math

def convert_images_to_pdf(folder_path, output_file):
    image_files = [file for file in os.listdir(folder_path) if file.lower().endswith(('.jpg', '.png'))]
    image_files.sort()  # Sort the files to maintain order

    with open(output_file, 'wb') as pdf_file:
        images = []
        for image in image_files:
            image_path = os.path.join(folder_path, image)
            with open(image_path, 'rb') as img:
                images.append(img.read())

        pdf_file.write(img2pdf.convert(images))

def process_child_folders(parent_folder, pdf_placement):
    child_folders = [folder for folder in os.listdir(parent_folder) if os.path.isdir(os.path.join(parent_folder, folder))]
    num_folders = len(child_folders)

    print("Processing child folders:")
    for i, folder_name in enumerate(child_folders, start=1):
        child_folder = os.path.join(parent_folder, folder_name)
        pdf_name = folder_name + '.pdf'

        pdf_name = re.sub(r'^.*?(Chapter)', r'\1', pdf_name)

        match = re.search(r'\d+', pdf_name)
        if match:
            number = int(match.group())
            pdf_name = str(number).zfill(4) + " " + pdf_name
        else:
            print("Couldn't Find Number")

        output_file = os.path.join(pdf_placement, pdf_name)

        Progress = math.floor((i/num_folders)*20)
        bar = Progress*chr(9619)+'_'*(20-Progress)
        terminal.write("\r["+bar+"]  " + str(i) + "/" + str(num_folders))

        try:
            convert_images_to_pdf(child_folder, output_file)
        except Exception as e:
            print(f"Error converting images in folder '{child_folder}': {str(e)}")

    print("\nProcessing completed!")

    input("Press Enter to Continue")



def button_click():
    parent = parent_folder.get()
    output = output_folder.get()
    if not os.path.isdir(parent):
        print("Invalid parent folder path.")
    elif not os.path.isdir(output):
        print("invalid pdf output folder.")
    else:
        process_child_folders(parent, output)
    

root = itop.Tk()

root.title("iTop (hot girls)")

label = itop.Label(root, text="Welcome to the image to pdf python script!")
label.pack()

input_label = itop.Label(root, text="Parent Directory")
input_label.pack()

parent_folder = itop.Entry(root)
parent_folder.pack()

output_label = itop.Label(root, text="Output Directory")
output_label.pack()

output_folder = itop.Entry(root)
output_folder.pack()

button = itop.Button(root, text="Images to PDF!", command=button_click)
button.pack()


root.mainloop()