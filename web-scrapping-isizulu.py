import requests
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = 'https://www.swazilandnews.co.za/news/'

# Send a GET request to the URL
response = requests.get(url, timeout=(10, 10))

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find all elements with class 'row m-40-0'
articles = soup.find_all(class_='row m-40-0')

# Open a text file to write the extracted information
with open('extracted_articles.txt', 'w', encoding='utf-8') as file:
    # Iterate through each article
    for article in articles:
        # Extract date
        date = article.find(class_='NewsDate').text.strip()
        
        # Extract title
        title = article.find(class_='font-pt').text.strip()
        
        # Extract author
        author = article.find(class_='font-pt').find_next_sibling('p').text.strip()
        
        # Extract link
        link = article.find('a', class_='news-btn')['href']
        
        # Check if the link is relative, if so, append the domain
        if not link.startswith('http'):
            link = url + link
        
        # Send a GET request to the article link
        article_response = requests.get(link)
        article_soup = BeautifulSoup(article_response.text, 'html.parser')
        
        # Extract story
        story = article_soup.find(class_='fundza-post-text').text.strip()
        
        # Extract author from the linked page
        author_from_linked_page = article_soup.find(class_='fundza-post-author').text.strip()
        
        # Write the extracted information to the text file
        file.write("Date: {}\n".format(date))
        file.write("Title: {}\n".format(title))
        file.write("Author: {}\n".format(author))
        file.write("Story: {}\n".format(story))
        file.write("Author from linked page: {}\n".format(author_from_linked_page))
        file.write("Link: {}\n\n".format(link))

# Confirmation message
print("Extraction completed. The extracted articles have been saved to 'extracted_articles.txt'.")
