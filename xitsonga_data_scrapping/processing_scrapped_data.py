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


def create_text_file(file_path, lines):
    try:
        with open(file_path, 'w', encoding="utf-8") as file:
            for line in lines:
                file.write(line + '\n')
    except IOError as e:
        print("Error writing to file:", e)


def main():
    input_file = "./xitsonga_data_scrapping/scrapped_article.txt"
    xitsonga_clean_text_file = "./xitsonga_data_scrapping/xitsonga_clean_text.txt"

    # Step 1: Data Reading
    input_lines = read_text_file(input_file)

    # Step 2: Cleaning
    cleaned_lines = [clean_text(line) for line in input_lines]

    # Step 3: File Creation
    create_text_file(xitsonga_clean_text_file, cleaned_lines)

    print("Clean text file created successfully.")


if __name__ == "__main__":
    main()
