import fitz  # PyMuPDF

def extract_text_from_pdf(uploaded_file):
    pdf_text = ""
    with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
        for page in doc:
            pdf_text += page.get_text()
    return pdf_text
