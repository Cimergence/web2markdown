import requests
from bs4 import BeautifulSoup
import os
import time
from urllib.parse import urljoin
# from utils.parser import save_markdown
from utils.scraper_crawl import scrape_crawl4ai
# from utils.scraper_selenium import scrap_selenium

# Define the base URL of the website
BASE_URL = 'https://www.swiss-interim-management.ch/'  # Replace with the actual website URL

# Define the directory where to save the Markdown files
SAVE_DIR = 'scraped_markdown_pages'
if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)



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
async def scrape_page_crawl(url: str, path: str = "", website: str = "",scraper_type: str = "selenium"):
    try:
        # if scraper_type == "selenium":
        #     text = scrap_selenium(url=url, path_filename=path, website=website)
        # elif scraper_type == "crawl4ai":
        #     text = await scrape_crawl4ai(url=url, path_filename=path, website=website)
        # else:
        #     text = ""


        text = await scrape_crawl4ai(url=url, path_filename=path, website=website)

    except requests.RequestException as e:
        print(f'Error fetching {url}: {e}')
        text = ""

        return text


# Recursive function to traverse and scrape all links
async def scrape_site(url, visited=set()):
    if url in visited:
        return
    visited.add(url)

    print(f'Scraping: {url}')
    await scrape_page_crawl(url=url, path=SAVE_DIR, website="", scraper_type="crawl4ai")

    # Find all links on the page and recursively scrape
    # try:
    #     response = requests.get(url)
    #     response.raise_for_status()
    #     soup = BeautifulSoup(response.text, 'html.parser')

    #     # Find all internal links
    #     for link in soup.find_all('a', href=True):
    #         full_url = urljoin(BASE_URL, link['href'])
    #         if full_url.startswith(BASE_URL) and full_url not in visited:
    #             scrape_site(full_url, visited)
    #             time.sleep(1)  # Respectful delay to avoid overloading the server
    # except requests.RequestException as e:
    #     print(f'Error fetching {url}: {e}')

# Start scraping from the home page
if __name__ == "__main__":
    text = scrape_site(BASE_URL)
