import re

def clean_text(text):
    # Removing everything before the colon
    cleaned_text = re.sub(r'^.*?:\s*', '', text)
    # Removing all types of quotation marks
    cleaned_text = re.sub(r'[\'\"‘’“”„]', '', cleaned_text)
    # Spliting the text into lines
    cleaned_lines = cleaned_text.splitlines()
    # List to store cleaned lines with more than two words
    cleaned_text_lines = []

    # Iterate through each line
    for line in cleaned_lines:
        # Split the line into words
        words = line.strip().split()
        # Check if the line has more than two words
        if len(words) > 2:
            # Align the line by joining the words with spaces
            cleaned_text_lines.append(' '.join(words))

    return cleaned_text_lines

def clean_file(input_file, output_file):
    # Read input file
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()

    # Clean the text
    cleaned_text = clean_text(text)

    # Write cleaned text to output file
    with open(output_file, 'w', encoding='utf-8') as file:
        for line in cleaned_text:
            file.write(line + '\n')

# Input and output file paths
input_file_path = r'C:\Users\thand\OneDrive\Documents\Botlale Ai\Data_Processing\TTS-data-processing\Clean_data\SeSotho\clean_sentences_Drama_Sotho.txt'
output_file_path = r'C:\Users\thand\OneDrive\Documents\Botlale Ai\Data_Processing\TTS-data-processing\Clean_data\SeSotho\clean_sentences_Drama_Sotho.txt'

# Clean the file
clean_file(input_file_path, output_file_path)
