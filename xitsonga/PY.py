import requests
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = 'https://www.nthavela.co.za/category/sports/'

# Send a GET request to the URL
response = requests.get(url)

# File path to save the extracted paragraphs
output_file_path = 'newspaper.txt'

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the webpage
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all paragraphs on the webpage
    paragraphs = soup.find_all('p')
    
    # Open the output file in write mode
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        # Write the text content of each paragraph to the file
        for paragraph in paragraphs:
            output_file.write(paragraph.get_text() + '\n')
    
    print("Paragraphs extracted and saved to", output_file_path)
else:
    print("Failed to fetch the webpage. Status code:", response.status_code)
