from PyPDF2 import PdfMerger

def merge_pdfs(pdf_list, output_path, First_page, Second_page):
    merger = PdfMerger()
    # Validate and handle page inputs
    if First_page is not None:
        merger.append(pdf_list[0], pages=(int(First_page) - 1,))  # Convert to zero-based index
    else:
        merger.append(pdf_list[0])  # Append the entire first PDF if no page is specified

    if Second_page is not None:
        merger.append(pdf_list[1], pages=(int(Second_page) - 1,))  # Convert to zero-based index
    else:
        merger.append(pdf_list[1])  # Append the entire second PDF if no page is specified

    merger.write(output_path)
    merger.close()

# Example usage
#merge_pdfs(['list-of-candidates-2025_26.pdf', 'Sainik School Seat Matrix VI Residential - Google Sheets.pdf'], 'merged_output.pdf')