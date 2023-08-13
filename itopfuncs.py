import os
import img2pdf
from PIL import Image
import re
from sys import stdout as terminal
from time import sleep

def is_valid_folder(folder_path):
    return os.path.isdir(folder_path)

def get_child_folders(parent_folder):
    try:
        child_folders = [folder for folder in os.listdir(parent_folder) if os.path.isdir(os.path.join(parent_folder, folder))]
        return child_folders
    except FileNotFoundError:
        print(f"Parent folder '{parent_folder}' not found.")
        return []

def convert_images_to_pdf(folder_path, output_file):
    image_files = [file for file in os.listdir(folder_path) if file.lower().endswith(('.jpg', '.png'))]
    image_files.sort()  # Sort the files to maintain order

    with open(output_file, 'wb') as pdf_file:
        images = []
        
        for index, image in enumerate(image_files):
            image_path = os.path.join(folder_path, image)
            with open(image_path, 'rb') as img:
                images.append(img.read())

        pdf_file.write(img2pdf.convert(images))

def get_child_folder_path(parent_folder, folder_name):
    return os.path.join(parent_folder, folder_name)

def get_output_file_path(pdf_placement, pdf_name):
    return os.path.join(pdf_placement, pdf_name)