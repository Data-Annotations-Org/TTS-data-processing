import csv

def separate_text(input_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        setswana_with_num = []
        setswana_without_num = []
        sepedi_with_num = []
        sepedi_without_num = []

        for row in reader:
            src_text = row[0].strip()
            tgt_text = row[1].strip()

            # setswana sentences (first sentence)
            if row[0].startswith('"') and row[1].startswith('"'):
                # setswana with numbers
                if any(char.isdigit() for char in src_text):
                    setswana_with_num.append(src_text)
                else:
                    setswana_without_num.append(src_text)
            # Sepedi sentences (second sentence)
            else:
                # Sepedi with numbers
                if any(char.isdigit() for char in tgt_text):
                    sepedi_with_num.append(tgt_text)
                else:
                    sepedi_without_num.append(tgt_text)

        # Write to separate files
        with open("setswana_with_num.txt", "w", encoding="utf-8") as setswana_with_num_file:
            setswana_with_num_file.write('\n'.join(setswana_with_num))

        with open("setswana_without_num.txt", "w", encoding="utf-8") as setswana_without_num_file:
            setswana_without_num_file.write('\n'.join(setswana_without_num))

        with open("sepedi_with_num.txt", "w", encoding="utf-8") as sepedi_with_num_file:
            sepedi_with_num_file.write('\n'.join(sepedi_with_num))

        with open("sepedi_without_num.txt", "w", encoding="utf-8") as sepedi_without_num_file:
            sepedi_without_num_file.write('\n'.join(sepedi_without_num))

input_file = "aligned_nso_tsn.csv"
separate_text(input_file)
