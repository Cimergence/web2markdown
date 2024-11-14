import requests
from bs4 import BeautifulSoup
import os
import time
from urllib.parse import urljoin

# Define the base URL of the website
BASE_URL = 'https://www.swiss-interim-management.ch/'  # Replace with the actual website URL

# Define the directory where to save the Markdown files
SAVE_DIR = 'scraped_markdown_pages'
if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)

# Function to save the content of a page as a Markdown file
def save_markdown(url, content):
    # Derive filename from URL
    filename = url.replace(BASE_URL, '').replace('/', '_').strip('_') + '.md'
    filepath = os.path.join(SAVE_DIR, filename)
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f'Saved: {filepath}')

# Function to scrape a page and save its content if it is in markdown
def scrape_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Assume markdown content is inside <pre><code> or <article> tags
        markdown_content = None
        code_block = soup.find('pre')
        if code_block:
            markdown_content = code_block.get_text()
        else:
            article_block = soup.find('article')
            if article_block:
                markdown_content = article_block.get_text()

        if markdown_content:
            save_markdown(url, markdown_content)
    except requests.RequestException as e:
        print(f'Error fetching {url}: {e}')

# Function to scrape a page and save its content using crawl4ai or selenium
def scrape_page_crawl(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Assume markdown content is inside <pre><code> or <article> tags
        markdown_content = None
        code_block = soup.find('pre')
        if code_block:
            markdown_content = code_block.get_text()
        else:
            article_block = soup.find('article')
            if article_block:
                markdown_content = article_block.get_text()

        if markdown_content:
            save_markdown(url, markdown_content)
    except requests.RequestException as e:
        print(f'Error fetching {url}: {e}')

# Recursive function to traverse and scrape all links
def scrape_site(url, visited=set()):
    if url in visited:
        return
    visited.add(url)

    print(f'Scraping: {url}')
    scrape_page(url)

    # Find all links on the page and recursively scrape
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all internal links
        for link in soup.find_all('a', href=True):
            full_url = urljoin(BASE_URL, link['href'])
            if full_url.startswith(BASE_URL) and full_url not in visited:
                scrape_site(full_url, visited)
                time.sleep(1)  # Respectful delay to avoid overloading the server
    except requests.RequestException as e:
        print(f'Error fetching {url}: {e}')

# Start scraping from the home page
scrape_site(BASE_URL)
