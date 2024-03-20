import requests
from bs4 import BeautifulSoup

# URL of the website
page = ["lifestyle", "health","news","sports"]
url = "https://www.nthavela.co.za/category"

# Initialize a counter for the number of articles scrapped
article_count = 0
target_artice = 30
url_index = 0
# Create a text file to store the output
output_file_path = "./xitsonga_data_scrapping/scrapped_article.txt"

with open(output_file_path, "w", encoding="utf-8") as output_file:
 while article_count < target_artice:
       base_url = f"{url}/{page[url_index]}/"
       # Make a GET request to fetch the web page
       response = requests.get(base_url)
       soup = BeautifulSoup(response.content, 'html.parser')
       # Find all article containers 
       article_containers = soup.find_all('article')
        # Iterate through each article
       for article in article_containers:
            # Checking if there is a "Read More" button
            read_more_button = article.find('a', class_='more-link')
            if read_more_button:
                # Increment the article counter
                article_count += 1
                # Getting article details link
                read_more_url = read_more_button['href']
                # Read article info
                read_more_response = requests.get(read_more_url)
                read_more_soup = BeautifulSoup(read_more_response.content, 'html.parser')
                #Read all paragraphs inside entry-content 
                paragraphs = read_more_soup.find_all('div', class_='entry-content')[0].find_all('p')
                for paragraph in paragraphs:
                    output_file.write(paragraph.text.strip() + "\n")

                output_file.write("\n" + "=" * 50 + "\n")
       url_index += 1

print("Output saved to:", output_file_path)
