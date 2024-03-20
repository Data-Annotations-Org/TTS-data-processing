def read_text_file(filename):
    file_path = f"./Scrapped Files/{filename}"
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
    text = text.replace('. ', '" "')
    text = text.replace('? ', '" "')
    text = text.replace('! ', '" "')
    text = text.replace('! ', '" "')
    text = text.rstrip()
    return text


def create_text_file(filename, lines):
    # Create a text file to store the output
    file_path = f"./Cleaned Files/{filename}"
    try:
        with open(file_path, 'w', encoding="utf-8") as file:
            for line in lines:
                line = line.strip()
                file.write(line)
    except IOError as e:
        print("Error writing to file:", e)


