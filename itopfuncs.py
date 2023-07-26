import os
import img2pdf
from PIL import Image
import re
from sys import stdout as terminal
from time import sleep
import math
from tkinter import filedialog

def is_valid_folder(folder_path):
    return os.path.isdir(folder_path)

def get_child_folders(parent_folder):
    return [folder for folder in os.listdir(parent_folder) if os.path.isdir(os.path.join(parent_folder, folder))]

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

def adjust_pdf_name(pdf_name):
    pdf_name = re.sub(r'^.*?(Chapter)', r'\1', pdf_name)
    match = re.search(r'\d+', pdf_name)
    if match:
        number = int(match.group())
        pdf_name = str(number).zfill(4) + " " + pdf_name
    else:
        print("Couldn't Find Number")
    return pdf_name

def get_child_folder_path(parent_folder, folder_name):
    return os.path.join(parent_folder, folder_name)

def get_output_file_path(pdf_placement, pdf_name):
    return os.path.join(pdf_placement, pdf_name)