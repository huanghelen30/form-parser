import pdfplumber

def parse_pdf(filepath):
    extracted_text = []

    with pdfplumber.open(filepath) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                extracted_text.append(text)

    return extracted_text
