def read_text_file(file_path):
    lines = []
    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            lines = file.readlines()
    except IOError as e:
        print("Error reading file:", e)
    return lines


def clean_text(text):
    # Remove special characters except for punctuation
    text = ''.join([c if c.isalnum() or c in '.,?!' else ' ' for c in text])

    # Separate sentences based on punctuation marks
    text = text.replace('. ', '.\n')
    text = text.replace('? ', '?\n')
    text = text.replace('! ', '!\n')

    return text


def categorize_sentences(sentences):
    clean_text = []
    text_with_numbers = []

    for sentence in sentences:
        sentence = sentence.strip()
        if sentence:
            if any(char.isdigit() for char in sentence) and any(char.isalpha() for char in sentence):
                text_with_numbers.append(sentence)
            elif is_coherent(sentence):
                clean_text.append(sentence)

    categorized_text = []
    categorized_text.append("Clean Text:")
    categorized_text.extend(clean_text)
    categorized_text.append("\nText with Numbers:")
    categorized_text.extend(text_with_numbers)

    return categorized_text


def is_coherent(sentence):
    # For simplicity, let's assume any sentence with less than 3 words is nonsensical
    words = sentence.split()
    return len(words) >= 3


def create_text_file(file_path, lines):
    try:
        with open(file_path, 'w', encoding="utf-8") as file:
            for line in lines:
                file.write(line + '\n')
    except IOError as e:
        print("Error writing to file:", e)


def main():
    input_file = "C:\\Users\\Dell CPU\\Documents\\data-annotations-tasks\\sepedi\\Sepedi.txt"
    clean_text_file = "clean_text.txt"
    text_with_numbers_file = "text_with_numbers.txt"

    # Step 1: Data Reading
    input_lines = read_text_file(input_file)

    # Step 2: Cleaning
    cleaned_lines = [clean_text(line) for line in input_lines]

    # Step 3: Organization
    categorized_text = categorize_sentences(cleaned_lines)

    # Step 4: File Creation
    create_text_file(clean_text_file, categorized_text[1:categorized_text.index("\nText with Numbers:")])
    create_text_file(text_with_numbers_file, categorized_text[categorized_text.index("\nText with Numbers:") + 1:])

    print("Files created successfully.")


if __name__ == "__main__":
    main()
