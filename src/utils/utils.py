import requests
from bs4 import BeautifulSoup
import os
import time
from urllib.parse import urljoin
from .parser import extract_links_from_markdown_text

from .scraper_crawl import scrape_crawl4ai
from .parser import get_last_part



async def scrape_site(base_url="",url="", folder_path="src/scraped_markdown_pages", visited=[]):

    if url in visited:
        return
    visited.append(url)

    print(f'Scraping: {url}')
    document_name  = get_last_part(url=url, base_url=base_url)
    print("document_name :",document_name)
    if not document_name or document_name.strip() == "":
        print('document does not have a name')
        document_name = "homepage"
    text = await scrape_crawl4ai(url=url, path_filename=folder_path+f"/{document_name}", website="")
    # Find all links on the page and recursively scrape
    try:
        links = extract_links_from_markdown_text(text)
        exclude_extensions = ('.jpg', '.png', '.gif', '.jpeg', '.bmp', '.svg')
        # print("links",links)
        #clean links

        links_clean = [s for s in links if s.startswith(f"{base_url}") and not s.lower().endswith(exclude_extensions)]

        for link in links_clean:

            if link not in visited:
                await scrape_site(base_url = base_url, url=link, folder_path=folder_path,visited=visited)
                time.sleep(0.1)  # Respectful delay to avoid overloading the server
    except requests.RequestException as e:
        print(f'Error fetching {url}: {e}')