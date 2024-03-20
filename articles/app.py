import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Function to extract paragraphs from the article URL
def extract_paragraphs_from_article(article_url):
    try:
        # Send a GET request to the article URL
        article_response = requests.get(article_url)

        # Check if the request was successful
        if article_response.status_code == 200:
            # Parse the HTML content of the article
            article_soup = BeautifulSoup(article_response.content, "html.parser")

            # Find the section with class "span10 content-area"
            content_section = article_soup.find("div", class_="span10 content-area")
            if content_section:
                # Extract title
                title_element = content_section.find("h2")
                title = title_element.get_text(strip=True) if title_element else "Title not found"

                # Extract paragraphs
                paragraphs = content_section.find_all("p")

                # Combine title and story into the same text
                story_text = f"{title}\n\n"
                for paragraph in paragraphs:
                    story_text += paragraph.get_text(strip=True) + "\n"

                return story_text
            else:
                print(f"Content section not found in article: {article_url}")
                return None
        else:
            print(f"Failed to retrieve article: {article_url}")
            return None
    except Exception as e:
        print(f"Error occurred while processing article: {article_url}")
        print(e)
        return None

# URL of the webpage
url = "https://www.limpopomirror.co.za/articles/venda/search?search=mutsho"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Find all <a> tags within the content divs with class "span9 content-area" and "span7 content-area"
    a_tags_span9 = soup.select("div.span9.content-area a")
    a_tags_span7 = soup.select("div.span7.content-area a")

    # Combine all <a> tags from both content areas
    all_a_tags = a_tags_span9 + a_tags_span7

    # Extract and process the articles linked by <a> tags
    with open("new.txt", "w", encoding="utf-8") as file:
        for a_tag in all_a_tags:
            # Get the URL of the article
            article_url = a_tag.get("href")
            # Make sure the URL is complete
            article_url = urljoin(url, article_url)
            # Extract paragraphs from the article
            story_text = extract_paragraphs_from_article(article_url)
            if story_text:
                # Write the combined title and story text to the file
                file.write(story_text + "\n\n")
                file.write("="*50 + "\n")  # Separator for clarity
else:
    print("Failed to retrieve the webpage")
