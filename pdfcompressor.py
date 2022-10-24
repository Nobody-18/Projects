import PyPDF2 as pdf
from sys import argv
file = argv[1]
reader = pdf.PdfReader(file)
writer = pdf.PdfWriter()
for page in reader.pages:
    page.compress_content_streams()
    writer.add_page(page)

with open("compressed.pdf", "wb")as f:
    writer.write(f)
