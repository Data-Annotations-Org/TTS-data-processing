from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

def scrape_articles(url):
  # Configure Chrome options for headless mode
  chrome_options = Options()
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--disable-gpu')

  # Initialize the Chrome webdriver with headless mode
  driver = webdriver.Chrome(options=chrome_options)

  # Open the URL in the Chrome browser
  driver.get(url)

  # Wait for the page to load completely
  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'td-theme-wrap')))

  # Get the HTML content of the entire webpage
  html_content = driver.page_source

  # Parse the HTML content to extract the article titles and links
  soup = BeautifulSoup(html_content, 'html.parser')

  # Find all articles on the webpage
  articles = soup.find_all('h3', class_='entry-title')

  # Initialize an empty list to store the titles and stories
  article_data = []

  # Iterate over each article
  for article in articles:
    # Extract the article title
    title = article.a.text.strip()

    # Extract the article link
    article_link = article.a['href']

    # Visit the article link to extract the story
    driver.get(article_link)

    # Wait for the article page to load completely
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'td-post-content')))

    # Get the HTML content of the article page
    article_html_content = driver.page_source

    # Parse the HTML content of the article page
    article_soup = BeautifulSoup(article_html_content, 'html.parser')

    # Extract the story content (all <p> tags within the article content)
    story = '\n'.join([p.text.strip() for p in article_soup.find_all('p')])

    # Append the title and story to the article_data list
    article_data.append({'title': title, 'story': story})

  # Close the webdriver
  driver.quit()

  return article_data

# URL of the webpage to scrape
url = "https://www.isolezwelesixhosa.co.za/ezemidlalo/"

# Call the function to scrape articles from the URL
articles = scrape_articles(url)

# Open a text file for writing in append mode
with open("scraped_articles.txt", "a", encoding="utf-8") as text_file:
  # Iterate over each article and write to the file
  for article in articles:
    text_file.write("Title: " + article['title'] + "\n")
    text_file.write("Story:\n" + article['story'] + "\n")
    text_file.write("=" * 50 + "\n")

print("Articles scraped and saved to scraped_articles.txt")
