import os, re, json, tiktoken

# Function to extract links from markdown content
def extract_links_from_markdown_text(text):
    # Regex to match markdown links
    link_pattern = r'\[.*?\]\((.*?)\)'
    links = re.findall(link_pattern, text)
    
    return links

# Function to save the content of a page as a Markdown file
def save_markdown(base_url, url, content, save_directory):
    # Derive filename from URL
    filename = url.replace(base_url, '').replace('/', '_').strip('_') + '.md'
    filepath = os.path.join(save_directory, filename)
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f'Saved: {filepath}')


def save_text_as_markdown(
        text:str = "", 
        filename:str = "", 
        duplicate:bool = False
        ):
    """
    The function `save_text_as_markdown` saves a given text as a Markdown file with a specified filename
    and mode, ensuring no file is overwritten by incrementing the filename if necessary.

    filename is the full path with the filename included
    duplicate: True = create a new file with a counter // False, replace the existing file
    
    """

    # Get the name and extension of the file
    base, ext = os.path.splitext(filename)
    
    # If file exists, append a number to the filename
    counter = 1
    new_filename = filename

    if duplicate:
        while os.path.exists(new_filename):
            new_filename = f"{base}_{counter}{ext}"
            counter += 1
    
    # Save the file
    with open(new_filename, 'w') as file:
        file.write(text)
        
    return new_filename

def get_last_part(url= "", base_url="https://" ):
    print(base_url,base_url)
    print("url",url)
    if not url == base_url:
        path = url.split(f"{base_url}")[-1]  # Remove "https://" part
        parts = path.split('/')           # Split by "/"
        exclude_extensions = ('.jpg', '.png', '.gif', '.jpeg', '.bmp', '.svg')
        last_parts = [part for part in parts if part and not part.lower().endswith(exclude_extensions)]
        name = '-'.join(last_parts) if last_parts else None
    else:
        name=""
    return name