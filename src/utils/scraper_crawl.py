import asyncio
import nest_asyncio
import json
import time

from crawl4ai import AsyncWebCrawler
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy, LLMExtractionStrategy

nest_asyncio.apply()

async def scrape_crawl4ai(url, path_filename, website):
    async with AsyncWebCrawler(verbose=True) as crawler:
        html = await crawler.arun(url=url)
        print(len(html.markdown))
        # print(html)
        if path_filename:
            with open(f'{path_filename}.md', 'w', encoding='utf-8') as file:
                file.write(html.markdown)
            print(f"Job description successfully saved as {path_filename}.md")
        else:
            print("Job description successfully obtained but not saved as file.")  
    return html.markdown