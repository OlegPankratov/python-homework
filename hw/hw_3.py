import os
from pprint import pprint

directory = 'files'
file_names = os.listdir(directory)

line_counts_to_files = {}
for file_name in file_names:
    with open(f"{directory}/{file_name}", encoding='utf-8') as file:
        value = file.readlines()
        key = len(value)
        if key in line_counts_to_files:
            line_counts_to_files[key] += [value]
        else:
            line_counts_to_files[key] = [value]


line_counts = list(line_counts_to_files.keys())
line_counts.sort()
result_text = ''
for line_count in line_counts:
    for text in line_counts_to_files[line_count]:
        for line in text:
            result_text += line

with open("result.txt", "w", encoding='utf-8') as file:
    file.write(result_text)

