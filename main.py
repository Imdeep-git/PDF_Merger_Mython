#used external module-->PyPDF2
from PyPDF2 import PdfMerger
pdfs = []
num = int(input("enter the no of pdf files you want to merge\n"))
for i in range(num):
    x = input(f"Enter the {i+1}th pdf file path: \n ")
    pdfs.append(x)

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()
