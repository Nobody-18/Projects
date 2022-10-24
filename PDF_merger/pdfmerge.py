import PyPDF2 as pdf
import os

merger = pdf.PdfFileMerger()

for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        merger.append(file) 


merger.write("combined.pdf")
# reader = pdf.PdfReader("combined.pdf")
# writer = pdf.PdfWriter()
# for page in reader.pages:
#     page.compress_content_streams()
#     writer.add_page(page)
# page = reader.pages[0]
# print(page.extract_text())
# writer.add_metadata(reader.metadata)
# writer.remove_images()


# with open("compressed.pdf", "wb") as pf:
#     writer.write(pf)