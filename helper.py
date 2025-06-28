import fitz  # PyMuPDF

def extract_text_from_pdf(uploaded_file):
    text = ""
    try:
        with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
            if len(doc) == 0:
                raise ValueError("Uploaded PDF has no pages.")

            for page in doc:
                page_text = page.get_text()
                if page_text:
                    text += page_text
            if not text.strip():
                raise ValueError("No readable text found in the PDF.")
    except Exception as e:
        raise RuntimeError(f"Failed to extract text from PDF: {e}")
    return text
