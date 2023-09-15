import PyPDF2

def merge_pdfs(input_pdfs, output_pdf):
    pdf_merger = PyPDF2.PdfMerger()
    
    for pdf in input_pdfs:
        pdf_merger.append(pdf)
    
    with open(output_pdf, 'wb') as output_file:
        pdf_merger.write(output_file)

# List of input PDFs to merge
input_pdfs = ['A.pdf', 'B.pdf', 'C.pdf', 'D.pdf', 'E.pdf', 'F.pdf']  # Add the correct paths to your input PDF files

# Output PDF file
output_pdf = 'merged_output.pdf'

merge_pdfs(input_pdfs, output_pdf)
