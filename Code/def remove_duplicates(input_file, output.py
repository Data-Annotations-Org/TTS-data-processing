def remove_duplicates(input_file, output_file):
    try:
        # Read the contents of the input file
        with open(input_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # Remove duplicate lines by converting to a set
        unique_lines = set(lines)

        # Write the unique lines to the output file
        with open(output_file, 'w', encoding='utf-8') as outfile:
            outfile.writelines(unique_lines)

        print(f"Duplicate lines removed. Unique content saved to '{output_file}'")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage:
input_file = r'C:\Users\thand\OneDrive\Documents\Botlale Ai\Data_Processing\TTS-data-processing\Clean_data\SeSotho\clean_sentences_Drama_Sotho.txt'
output_file = r'C:\Users\thand\OneDrive\Documents\Botlale Ai\Data_Processing\TTS-data-processing\Clean_data\SeSotho\clean_sentences_Drama_Sotho.txt'
remove_duplicates(input_file, output_file)
