import re

def clean_text(input_file, output_dir):
    with open(input_file, 'r', encoding='latin-1') as file:
        content = file.read()
    
    # Spliting content into sentences
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', content)

    # Lists to hold different types of sentences
    nonsensical_sentences = []
    sentences_with_numbers = []
    quoted_sentences = []
    clean_sentences = []

    for sentence in sentences:
        # Remove leading and trailing whitespaces and punctuation
        cleaned_sentence = sentence.strip().strip(',:;')
        
        word_count = len(cleaned_sentence.split())

        if word_count < 3 or not cleaned_sentence:
            nonsensical_sentences.append(cleaned_sentence)
        elif any(char.isdigit() for char in cleaned_sentence):
            sentences_with_numbers.append(cleaned_sentence)
        elif cleaned_sentence.startswith('"') and cleaned_sentence.endswith('"'):
            quoted_sentences.append(cleaned_sentence)
        else:
            clean_sentences.append(cleaned_sentence)

    # Separate output files
    with open(output_dir + '/nonsensical_StudyGuide_Sotho.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join(nonsensical_sentences))

    with open(output_dir + '/sentences_with_numbers_StudyGuide_Sotho.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join(sentences_with_numbers))

    with open(output_dir + '/clean_sentences_StudyGuide_Sotho.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join(clean_sentences))

    print("Files created successfully!")

input_file = r"C:\Users\thand\OneDrive\Documents\Botlale Ai\Data_Processing\TTS-data-processing\Scrapped_data\Studyguide_Sotho.txt"
output_directory = r"C:\Users\thand\OneDrive\Documents\Botlale Ai\Data_Processing\TTS-data-processing\Clean_data\SeSotho"

clean_text(input_file, output_directory)
