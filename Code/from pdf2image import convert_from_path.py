from pdf2image import convert_from_path
import pytesseract

# Path to the PDF file
pdf_path = r"C:\Users\thand\OneDrive\Documents\Botlale Ai\Data_Processing\TTS-data-processing\PDF's\SeSotho Drama Lejwe la kgopiso.pdf"

# Convert PDF pages to images
pages = convert_from_path(pdf_path)

# Initialize empty text variable to store OCR results
all_text = ''

# Iterate over each page
for page_number, page in enumerate(pages, 1):
    # Perform OCR on the page image
    text = pytesseract.image_to_string(page)
    
    # Print the extracted text for this page
    print(f'Page {page_number} Text:')
    print(text)
    
    # Add extracted text to the overall text
    all_text += f'Page {page_number}:\n{text}\n\n'

# Save the extracted text to a text file
output_text_file = r"C:\Users\thand\OneDrive\Documents\Botlale Ai\Data_Processing\TTS-data-processing\Scrapped_data_Drama_Sotho.txt"
with open(output_text_file, 'w') as file:
    file.write(all_text)

print(f'Extracted text saved to {output_text_file}')
