import os, shutil
from utils.translator import translate_google, translate_deepl, lang_detection


# Define directories
# Directory containing the Markdown files
original_dir = "/home/bibiicekill/code-projects/web2markdown/src/scraped_markdown_pages/test"
test_dir = "/home/bibiicekill/code-projects/web2markdown/src/scraped_markdown_pages/translated" # Replace with the path to /test

# Ensure the /test directory exists
os.makedirs(test_dir, exist_ok=True)

# Function to split text into chunks, avoiding breaking sentences
def split_into_chunks_no_sentence_cut(text, chunk_size=5000):
    sentences = text.split('. ')  # Split the text into sentences (adjust delimiter if needed)
    chunks = []
    current_chunk = ""
    
    for sentence in sentences:
        if len(current_chunk) + len(sentence) + 1 <= chunk_size:  # +1 accounts for the space or period
            current_chunk += sentence + ". "
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence + ". "
    
    if current_chunk:
        chunks.append(current_chunk.strip())
    
    return chunks

# Copy original files to the test directory
for filename in os.listdir(original_dir):
    if filename.endswith(".md"):  # Only process Markdown files
        src_path = os.path.join(original_dir, filename)
        dest_path = os.path.join(test_dir, filename)
        shutil.copy(src_path, dest_path)

# Read and update all Markdown files in the /test directory
# for filename in os.listdir(test_dir):

# files = [
#     "homepage.md",
#     "our-approach.md",
#     "our-clients.md",
#     "our-company.md",
#     "our-values.md",
# ]

files = [
    "homepage.md",
]



# for filename in os.listdir(test_dir):
for filename in files:
    if filename.endswith(".md"):  # Only process Markdown files
        filepath = os.path.join(test_dir, filename)
        
        # Read file content
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()
        
        # Remove patterns
        # content = translate_deepl(text=content, source="en", target="fr")

        # Split content into chunks to respect API limit
        chunks = split_into_chunks_no_sentence_cut(content, chunk_size=4500)
        
        translated_content = ""
        for chunk in chunks:
            translated_content += translate_google(text=chunk, source="en", target="fr")
        filepath = os.path.join(test_dir, filename.strip(".md")+"_fr.md")
        # Write updated content back to the file
        # import pdb; pdb.set_trace()
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(translated_content)

print("Markdown files translated in /translated.")