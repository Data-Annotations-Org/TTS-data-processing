import requests
from bs4 import BeautifulSoup

# URL of website
url = "https://www.nthavela.co.za/category/health/"

# Make a GET request to fetch the web page
response = requests.get(url)


soup = BeautifulSoup(response.content, 'html.parser')

# Find all article containers 
article_containers = soup.find_all('article')

# Create a text file to store the output
output_file_path = "article_context.txt"
with open(output_file_path, "w", encoding="utf-8") as output_file:
    # Iterate through each article
    for article in article_containers:
        # Check if there's a "Read More" button
        read_more_button = article.find('a', class_='more-link')
        if read_more_button:
            read_more_url = read_more_button['href']
            read_more_response = requests.get(read_more_url)
            read_more_soup = BeautifulSoup(read_more_response.content, 'html.parser')

            # Extracting the paragraphs in the article
            paragraphs = read_more_soup.find_all('p')
            for paragraph in paragraphs:
                output_file.write(paragraph.text.strip() + "\n")

            output_file.write("\n" + "=" * 50 + "\n") 

print("Output saved to:", output_file_path)
