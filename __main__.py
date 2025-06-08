import streamlit as st
from src.pdfMerge import merge_pdfs
from src.pdf2excel import pdf_to_excel

# Streamlit GUI
st.title("PDF Tools")

# File uploader for PDF files
uploaded_files = st.file_uploader("Upload PDF files", type="pdf", accept_multiple_files=True)

# Output file name input
output_file_name = st.text_input("Enter output file name", "merged_output.pdf")

# Function selection
pdf_Tool = st.selectbox(
    "Select action to perform on PDFs",
    ["Merge", "Convert to Excel"]
)

if pdf_Tool == "Merge":
    First_page = st.number_input("Enter the page number to start merging from (for the first PDF)", min_value=1, step=1)
    Second_page = st.number_input("Enter the page number to start merging from (for the second PDF)", min_value=1, step=1)
elif pdf_Tool == "Convert to Excel":
    specific_page = st.text_input("Enter the page numbers to convert (1 for first page, 1-2 for two page, etc., or 'all' for all pages)", "all")
# Merge button
if st.button("Run"):
    if uploaded_files and output_file_name:
        # Save uploaded files temporarily
        pdf_paths = []
        for uploaded_file in uploaded_files:
            temp_path = f"./{uploaded_file.name}"
            with open(temp_path, "wb") as f:
                f.write(uploaded_file.read())
            pdf_paths.append(temp_path)

        # Call the selected merge function
            if pdf_Tool == "Merge":
                merge_pdfs(pdf_paths, output_file_name, First_page or None, Second_page or None)
            elif pdf_Tool == "Convert to Excel":
                if len(pdf_paths) == 1:
                    pdf_to_excel(pdf_paths[0], output_file_name.replace('.pdf', '.xlsx'), specific_page)
                else:
                    st.error("Please select only one PDF file for conversion to Excel.")
            else:
                st.error("Invalid function selected.")

        st.success(f"PDFs {pdf_Tool} successfully into {output_file_name}")
    else:
        st.error("Please upload PDF files and specify an output file name.")