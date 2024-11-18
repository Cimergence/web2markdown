from utils.utils import scrape_site

url = "https://www.swiss-interim-management.ch/"
folder_path="/home/bibiicekill/code-projects/web2markdown/src/scraped_markdown_pages"

import asyncio
asyncio.run(scrape_site(base_url=url, url=url, folder_path=folder_path))

# await scrape_site(base_url=url, url=url, folder_path=folder_path)