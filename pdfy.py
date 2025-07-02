#!/opt/homebrew/bin/python3

import os
import img2pdf
import sys
import contextlib

book_name = "book.pdf"
if len(sys.argv) == 2:
    book_name = sys.argv[1]
# Replace the directory path with the folder containing PNG images to be converted
directory_path = "./book"

# Get full paths of PNG files and sort them
image_files = [os.path.join(directory_path, filename) 
               for filename in sorted(os.listdir(directory_path)) 
               if filename.endswith(".png")]

print("Converting images to pdf...", end="\r", flush=True)
# Convert the list of PNG images to a single PDF file
with open(os.devnull, 'w') as devnull, contextlib.redirect_stderr(devnull):
    with open(f"{book_name}.pdf", "wb") as file:
        file.write(img2pdf.convert(image_files))
print("Converting Completed", end="\r", flush=True)
