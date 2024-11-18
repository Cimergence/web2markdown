import os
import glob

# Define the folder containing the .md files
folder_path = "/home/bibiicekill/code-projects/web2markdown/src/scraped_markdown_pages/original"  # Replace with your folder path

# Define the characters to exclude
exclude_chars = set("()[][LINK](DES)")

# Initialize the total character count
total_character_count = 0

# Loop through all .md files in the folder
for file_path in glob.glob(os.path.join(folder_path, "*.md")):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        # Filter out the excluded characters
        filtered_content = ''.join(c for c in content if c not in exclude_chars)
        # Count the remaining characters
        total_character_count += len(filtered_content)

print(f"Total character count (excluding '(', ')', '[', ']'): {total_character_count}")


# Initialize the total word count
total_word_count = 0

# Loop through all .md files in the folder
for file_path in glob.glob(os.path.join(folder_path, "*.md")):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        # Remove the excluded characters
        filtered_content = ''.join(c if c not in exclude_chars else ' ' for c in content)
        # Split the content into words
        words = filtered_content.split()
        # Count the words
        total_word_count += len(words)

print(f"Total word count (excluding words containing '(', ')', '[', ']'): {total_word_count}")
