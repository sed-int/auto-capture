#!/opt/homebrew/bin/python3

import os
import img2pdf
import sys
import contextlib

if len(sys.argv) != 3:
    print("Usage: python pdfy.py <book_path> <book_name>")
    sys.exit(1)

book_path = sys.argv[1]
book_name = sys.argv[2]

if os.path.exists(f'{book_path}/{book_name}.pdf'):
    book_name = book_name + "_copy"
    print(f"File {book_path}/{book_name}.pdf already exists, adding suffix to book_name")

# Replace the directory path with the folder containing PNG images to be converted

# Get full paths of PNG files and sort them
image_files = [os.path.join(book_path, filename) 
               for filename in sorted(os.listdir(book_path)) 
               if filename.endswith(".png")]

print("Converting images to pdf...", end="\r", flush=True)
# Convert the list of PNG images to a single PDF file
with open(os.devnull, 'w') as devnull, contextlib.redirect_stderr(devnull):
    with open(f"{book_name}.pdf", "wb") as file:
        file.write(img2pdf.convert(image_files))
print("Converting Completed", end="\r", flush=True)
