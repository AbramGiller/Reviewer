import PyPDF2
import re
import warnings
import nltk
from PyPDF2.utils import PdfReadWarning
from nltk.tokenize import word_tokenize

nltk.download('punkt')

warnings.filterwarnings("ignore", category=PdfReadWarning)

def write_chunks_to_file(chunks, output_file):
    with open(output_file, 'w') as file:
        for chunk in chunks:
            file.write(chunk)
            file.write('\n\n')  # Separate chunks with two newlines

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        text = ''
        for i in range(reader.numPages):
            page = reader.getPage(i)
            text += page.extract_text()

    return text

def preprocess_text(text, max_tokens=3000):
    text = re.sub(r'\n', ' ', text)  # Remove newlines
    text = re.sub(r'\s+', ' ', text)  # Remove extra whitespace
    
    words = word_tokenize(text)  # Tokenize the text using nltk

    chunks = []
    current_chunk = []

    for word in words:
        current_chunk.append(word)
        if len(' '.join(current_chunk)) > max_tokens:
            chunks.append(' '.join(current_chunk[:-1]))
            current_chunk = [current_chunk[-1]]

    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks

if __name__ == "__main__":
    pdf_path = '/Users/s2222119/Reviewer4/CRISPR.pdf'
    output_file = '/Users/s2222119/Reviewer4/CRISPR_output.txt'

    extracted_text = extract_text_from_pdf(pdf_path)
    preprocessed_chunks = preprocess_text(extracted_text)
    write_chunks_to_file(preprocessed_chunks, output_file)
