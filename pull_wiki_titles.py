import gzip
import os

def read_titles(file_path):
    titles = []  # List to hold all titles
    with gzip.open(file_path, 'rt', encoding='utf-8') as f:
        for line in f:
            title = line.strip().replace('_', ' ')  # Replace underscores with spaces
            titles.append(title)  # Append the title to the titles list
    return titles  # Return the list of titles

def save_titles(titles, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        for title in titles:
            f.write(title + '\n')  # Write each title on a new line

# Usage:
file_path = 'G:/My Drive/Data-Centric Solutions/07. Blog Posts\AutoGen/autogen_tutorial/wikipedia_titles/enwiki-latest-all-titles-in-ns0.gz'

# Call the function and store the list of titles
all_wikipedia_titles = read_titles(file_path)

# Determine the output file path
output_dir = os.path.dirname(file_path)  # Get the directory of the gzip file
output_file_name = 'all_wikipedia_titles.txt'
output_path = os.path.join(output_dir, output_file_name)  # Combine to form the output file path

# Save the titles to the output file
save_titles(all_wikipedia_titles, output_path)
