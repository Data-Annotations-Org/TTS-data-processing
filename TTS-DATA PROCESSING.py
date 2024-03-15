import re


# Read the input text

with open('input.txt', 'r', encoding='utf-8') as f:

    lines = f.readlines()


# Separate the sentences into 2 text files, one for isiXhosa and one for Xitsonga(TSO)

isiXhosa_lines = []

xitsonga_lines = []


for line in lines:

    lang, text, score = line.strip().split('","', 2)

    if lang == 'isiXhosa':

        isiXhosa_lines.append(text)

    elif lang == 'Xitsonga(TSO)':

        xitsonga_lines.append(text)


# Write the isiXhosa sentences to a file

with open('isiXhosa.txt', 'w', encoding='utf-8') as f:

    for line in isiXhosa_lines:

        f.write(line + '\n')


# Write the Xitsonga(TSO) sentences to a file

with open('xitsonga.txt', 'w', encoding='utf-8') as f:

    for line in xitsonga_lines:

        f.write(line + '\n')


# Separate the text that has numbers from one that doesn't have numbers for each language

isiXhosa_with_numbers = []

isiXhosa_without_numbers = []


xitsonga_with_numbers = []

xitsonga_without_numbers = []


for line in isiXhosa_lines:

    if re.search(r'\d', line):

        isiXhosa_with_numbers.append(line)

    else:

        isiXhosa_without_numbers.append(line)


for line in xitsonga_lines:

    if re.search(r'\d', line):

        xitsonga_with_numbers.append(line)

    else:

        xitsonga_without_numbers.append(line)


# Write the isiXhosa sentences with numbers 

with open('isiXhosa_with_numbers.txt', 'w', encoding='utf-8') as f:

    for line in isiXhosa_with_numbers:

        f.write(line + '\n')


# Write the isiXhosa sentences without numbers 

with open('isiXhosa_without_numbers.txt', 'w', encoding='utf-8') as f:

    for line in isiXhosa_without_numbers:

        f.write(line + '\n')


# Write the Xitsonga(TSO) sentences with numbers 

with open('xitsonga_with_numbers.txt', 'w', encoding='utf-8') as f:

    for line in xitsonga_with_numbers:

        f.write(line + '\n')


# Write the Xitsonga(TSO) sentences without numbers 

with open('xitsonga_without_numbers.txt', 'w', encoding='utf-8') as f:

    for line in xitsonga_without_numbers:

        f.write(line + '\n')

