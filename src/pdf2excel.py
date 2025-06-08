import tabula
import pandas as pd

ADD_NEW_SHEET_FOR_EACH_PAGE_IN_PDF = False #Set to True if you want each page of the PDF to be in a separate sheet in the Excel file

def pdf_to_excel(pdf_file_path, excel_file_path, pages) -> None:
    # Read PDF file
    tables = tabula.read_pdf(pdf_file_path, pages=pages, multiple_tables=True)

    if( ADD_NEW_SHEET_FOR_EACH_PAGE_IN_PDF ):
        # Write each table to a separate sheet in the Excel file
        with pd.ExcelWriter(excel_file_path) as writer:
            for i, table in enumerate(tables):
                table.to_excel(writer, sheet_name=f'Sheet{i+1}', index=False)
    else:
        # Concatenate all tables into a single DataFrame
        combined_table = pd.concat(tables, ignore_index=True)
        # Write the combined table to a single sheet in the Excel file
        combined_table.to_excel(excel_file_path, sheet_name='CombinedSheet', index=False)


#pdf_to_excel('./example.pdf', './yourExcelFileName.xlsx')