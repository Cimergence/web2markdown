from pydantic import BaseModel, Field
from markdownify import markdownify
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException
from selenium.webdriver.common.action_chains import ActionChains

# Move the mouse to simulate user interaction
 # Simulate random mouse movement


import time

def configure_driver():
    chrome_options = Options()
    # chrome_options.add_argument('--headless')  # Run in headless mode
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')

    
    # Make sure this path is correct for your environment
    chrome_options.binary_location = "/home/bibiicekill/code-projects/CVgenerator/chrome-linux/chrome"
    
    # Create the WebDriver instance
    driver = webdriver.Chrome(options=chrome_options)
    
    return driver

# Example of scraping function
def scrap_selenium(url, path_filename, website):
    driver = configure_driver()
    actions = ActionChains(driver)
    actions.move_by_offset(100, 100).perform() 



    job_description_md = ""


    print("URL: ", url)
    print("path: ", path_filename)
    print("website: ", website)

    try:
        driver.get(url)
        print(f"Accessing {url}...")

        # Wait for the page to load completely by targeting a reliable element
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        print("Page loaded successfully.")
        
        # DEBUG: Print the entire page source to verify the content is there
        page_source = driver.page_source
        print("DEBUG: Printing page source...")
        print(page_source[:100])  # Print first 1000 characters for inspection

        # Find the job description element based on the website
        if website == "linkedin.com":
            # job_description_element = driver.find_element(By.CLASS_NAME, 'detail--drop-shadow')  # Adjust this selector as needed
            # job_description_element = driver.find_element(By.CLASS_NAME, 'job-view-layout')
            job_description_element = driver.find_element(By.CLASS_NAME, 'details')
        elif website == "jobs.ch":
            job_description_element = driver.find_element(By.XPATH, "//div[@data-cy='vacancy-layout-standard']")
        elif website == "indeed.com":
            # Use WebDriverWait for dynamic page loading
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "challenge-container"))
            )
            job_description_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "main__content"))
            )
        elif website == "generic":
            job_description_element = driver.find_element(By.TAG_NAME, "body")
        else:
            raise ValueError(f"Unknown website: {website}")

        # Get the HTML content of the job description element
        job_description_html = job_description_element.get_attribute('outerHTML')

        # DEBUG: Print the job description HTML to verify correctness
        print("DEBUG: Job description HTML:")
        print(job_description_html)  # Print first 1000 characters for inspection

        # Convert the HTML content to Markdown
        job_description_md = markdownify(job_description_html)

        # Save the Markdown content to a file if specified
        if path_filename:
            with open(f'{path_filename}.md', 'w', encoding='utf-8') as file:
                file.write(job_description_md)
            print(f"Job description successfully saved as {path_filename}.md")
        else:
            print("Job description successfully obtained but not saved as file.")

    except (TimeoutException, NoSuchElementException) as e:
        print(f"Error: The job description element was not found or page timed out. {str(e)}")
    except WebDriverException as e:
        print(f"WebDriverException occurred: {str(e)}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        # Close the WebDriver instance
        driver.quit()

    return job_description_md



