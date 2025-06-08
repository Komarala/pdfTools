# pdfTools

## How to run
- Install dependencies
```python -m venv .venv```
```source .venv/bin/activate```
```pip install -r /path/to/requirements.txt```
- Run command in CLI for starting GUI
```streamlit run __main__.py```

## pdf2excel
- This script converts pdf file with rows and columns to a .xslx excel file.
- Change the global variable *ADD_NEW_SHEET_FOR_EACH_PAGE_IN_PDF* for a new sheet for each page in pdf

## pdfMerge
- Merge two pdf's based on given page numbers