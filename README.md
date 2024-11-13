# web2markdown
A Python tool for scraping websites with Markdown pages, recursively downloading and organizing content into local .md files.


**Description:**

This repository contains a Python script designed to scrape websites that publish pages in Markdown format. It crawls through all internal links, retrieves Markdown content, and saves each page as a `.md` file, maintaining the structure of the website locally. This tool is useful for backing up Markdown-based documentation sites, blogs, or any site where content is published in Markdown.

**Features:**
- **Automated Crawling:** Recursively scrapes all internal links, capturing each page with Markdown content.
- **Markdown Extraction:** Detects and extracts Markdown from `<pre>`, `<code>`, or `<article>` tags, depending on the site structure.
- **File Organization:** Saves each page as a `.md` file named after its URL path, creating a structured and accessible local copy.
- **Politeness:** Includes request delay to prevent overloading the server, following good scraping practices.

**Requirements:**
- Python 3.x
- `requests` and `beautifulsoup4` libraries

**Usage:**
Clone the repository, modify the `BASE_URL` to target the desired website, and run the script. Markdown files will be saved in the `scraped_markdown_pages` folder.

---

This description is both concise and thorough, making it easy for users to understand the purpose and capabilities of the tool. Let me know if you'd like to add any specific details!
