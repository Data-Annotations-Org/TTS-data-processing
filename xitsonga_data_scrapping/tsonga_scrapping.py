import requests
from bs4 import BeautifulSoup

def scrape_article_content(article_url):
    try:
        # Send a GET request to the article URL
        response = requests.get(article_url)
        response.raise_for_status()

        # Parse the HTML content of the article
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the main content of the article
        main_content = soup.find('div', class_='article-content')  # Adjust class name as per the website's HTML structure

        # Extract text from the main content
        article_text = main_content.get_text(separator='\n')

        return article_text
    except Exception as e:
        print(f"Error scraping article content: {e}")
        return None

def write_to_file(article_text, file_name):
    try:
        # Write the article text to a new text file
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(article_text)
        print(f"Article content has been written to '{file_name}' successfully.")
    except Exception as e:
        print(f"Error writing to file: {e}")

def main():
    # URL of the article to scrape
    article_url = "https://www.nthavela.co.za/category/health/"  # Replace with the actual URL of the article

    # Name of the output text file
    file_name = "article_content.txt"

    # Scrape article content
    article_text = scrape_article_content(article_url)

    if article_text:
        # Write article content to a text file
        write_to_file(article_text, file_name)

if __name__ == "__main__":
    main()
