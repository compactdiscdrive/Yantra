import fitz

def read_pdf(filepath):
    doc = fitz.open(filepath)
    
    text = ""
    for page in doc:
        text += page.get_text()
    
    lines = text.split("\n")
    lines = [line for line in lines if len(line) > 50]
    text = "\n".join(lines)
    
    return text[:5000]