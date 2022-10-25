from cgitb import text
import PyPDF2 as pdf
from sys import argv
file = argv[1]
reader = pdf.PdfReader(file)
writer = pdf.PdfWriter()

for page in reader.pages:
    writer.add_page(page)
writer.remove_images()
writer.write(f"noimage{file}")
