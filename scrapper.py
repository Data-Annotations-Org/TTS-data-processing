import requests
from bs4 import BeautifulSoup

def articleDataProcessingMethodOne(page,url,scrapped_article,language):
 # Initialize a counter for the number of articles scrapped
 article_count = 0
 target_artice = 30
 url_index = 0
 # Create a text file to store the output
 output_file_path = f"./Scrapped Files/{scrapped_article}"
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
 print(f"{language} Scrapped file created")


def articleDataProcessingMethodTwo(page,url,scrapped_article,language):
 # Initialize a counter for the number of articles scrapped
 article_count = 0
 target_artice = 30
 url_index = 0
 # Create a text file to store the output
 output_file_path = f"./Scrapped Files/{scrapped_article}"
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
            a_href = article.find('a')
            if a_href:
                # Increment the article counter
                article_count += 1
                read_more_response = requests.get(f"{url}{a_href['href'][3:]}")
                read_more_soup = BeautifulSoup(read_more_response.content, 'html.parser')   
                #Read all paragraphs inside entry-content 
                paragraphs = read_more_soup.find_all('div', class_='articleBodyMore')[0].find_all('p')
            for paragraph in paragraphs:
             output_file.write(paragraph.text.strip() + "\n")
             output_file.write("\n" + "=" * 50 + "\n")
       url_index += 1
 print(f"{language} Scrapped file created")

"""
def articleDataProcessingMethodThree(page,url,scrapped_article,language):
 # Initialize a counter for the number of articles scrapped
 article_count = 0
 target_artice = 30
 url_index = 0
 # Create a text file to store the output
 output_file_path = f"./Scrapped Files/{scrapped_article}"
 with open(output_file_path, "w", encoding="utf-8") as output_file:
  while article_count < target_artice:
       print(url_index)      
       base_url = f"{url}/{page[url_index]}"
       # Make a GET request to fetch the web page
       response = requests.get(base_url)
       soup = BeautifulSoup(response.content, 'html.parser')
       # Find all article containers 
       article_containers = soup.find_all('article')
       print("oh")
       print(article_containers)
        # Iterate through each article
       print("herer 00")
       for article in article_containers:
            # Checking if there is a "Read More" button
            a_href = article.find('a')
            print("herer 0")
            if a_href:
                print("herer 1")
                # Increment the article counter
                article_count += 1
                # Getting article details link
                #read_more_url = a_href['href']
                # Read article info
                read_more_response = requests.get(f"{url}{a_href['href'][3:]}")
                read_more_soup = BeautifulSoup(read_more_response.content, 'html.parser')
                #Read all paragraphs inside entry-content
                print(read_more_soup) 
                paragraphs = read_more_soup.find_all('div', class_='article--top-bar')[0].find_all('h1')
                print(paragraphs)
                if paragraphs :
                 for paragraph in paragraphs:
                    output_file.write(paragraph.text.strip() + "\n")

                 output_file.write("\n" + "=" * 50 + "\n")
       url_index += 1
       print(article_count)
 print(f"{language} Scrapped file created")
"""


def articleDataProcessingMethodFour(page,url,scrapped_article,language):
 # Initialize a counter for the number of articles scrapped
 article_count = 0
 target_artice = 30
 url_index = 0
 # Create a text file to store the output
 output_file_path = f"./Scrapped Files/{scrapped_article}"
 with open(output_file_path, "w", encoding="utf-8") as output_file:
  while article_count < target_artice:
       base_url = f"{url}/{page[url_index]}/"
       # Make a GET request to fetch the web page
       response = requests.get(base_url)
       soup = BeautifulSoup(response.content, 'html.parser')
       # Find all article containers 
       article_containers = soup.find('section', class_='content-articles style-1').find_all('h3')
       #article_containers = soup.find_all('article')     
        # Iterate through each article
       for article in article_containers:
            # Checking if there is a "Read More" button
            a_href = article.find('a')
            fixed_url = url+a_href['href']
            if a_href:
                # Increment the article counter
                article_count += 1
                read_more_response = requests.get(fixed_url)
                read_more_soup = BeautifulSoup(read_more_response.content, 'html.parser')   
                #Read all paragraphs inside entry-content 
                paragraphs = read_more_soup.find(id='content-block-details|article').find_all('p') 
            for paragraph in paragraphs:
             output_file.write(paragraph.text.strip() + "\n")
            output_file.write("\n" + "=" * 50 + "\n")
       url_index += 1
 print(f"{language} Scrapped file created")


def articleDataProcessingMethodFive(page,url,scrapped_article,language):
 # Initialize a counter for the number of articles scrapped
 article_count = 0
 target_artice = 1
 url_index = 0
 # Create a text file to store the output
 output_file_path = f"./Scrapped Files/{scrapped_article}"
 with open(output_file_path, "w", encoding="utf-8") as output_file:
  while article_count < target_artice:
       base_url = f"{url}{page[url_index]}/"
       print(base_url)
       # Make a GET request to fetch the web page
       response = requests.get(base_url)
       soup = BeautifulSoup(response.content, 'html.parser')
       # Find all article containers 
       article_containers = soup.find_all('a')
       #article_containers = soup.find_all('article')     
        # Iterate through each article
       print(article_containers)
       for article in article_containers:
            # Checking if there is a "Read More" button
            print(article)
            a_href = article.find('a')
            
            fixed_url = url+a_href['href']
            
            if a_href:
                # Increment the article counter
                article_count += 1
                read_more_response = requests.get(fixed_url)
                read_more_soup = BeautifulSoup(read_more_response.content, 'html.parser')   
                #Read all paragraphs inside entry-content 
                paragraphs = read_more_soup.find(id='content-block-details|article').find_all('p') 
            for paragraph in paragraphs:
             output_file.write(paragraph.text.strip() + "\n")
            output_file.write("\n" + "=" * 50 + "\n")
       url_index += 1
 print(f"{language} Scrapped file created")