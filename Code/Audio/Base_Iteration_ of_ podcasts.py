import os
import requests
from urllib.parse import urlparse
import re

def extract_audio_urls_from_source(url):
    response = requests.get(url)
    if response.status_code == 200:
        audio_urls = re.findall(r'https?://(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,6}(?:/[^/#?]+)+\.(?:mp3|wav|ogg)', response.text)
        return audio_urls
    else:
        print("Failed to fetch page source:", response.status_code)
        return []

def download_audio_from_webpage(webpage_url, output_folder):
    # Extract audio URLs from the webpage
    audio_urls = extract_audio_urls_from_source(webpage_url)

    # Download audio files from the extracted URLs
    download_audio(audio_urls, output_folder)

def download_audio(urls, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for url in urls:
        try:
            # Parse the URL to extract the filename
            title = get_title_from_url(url)
            
            # Send a GET request to download the audio content
            response = requests.get(url)

            # Check if the request was successful
            if response.status_code == 200:
                # Get the audio content
                audio_content = response.content

                # Save the audio content to a file
                output_file = os.path.join(output_folder, f"{title}.mp3")
                if os.path.exists(output_file):
                    # If the file already exists, append a number to make it unique
                    index = 1
                    while os.path.exists(output_file):
                        output_file = os.path.join(output_folder, f"{title}_{index}.mp3")
                        index += 1

                with open(output_file, "wb") as audio_file:
                    audio_file.write(audio_content)
                print(f"Audio file '{output_file}' downloaded successfully.")
            else:
                print(f"Failed to download the audio file from '{url}'. Status code: {response.status_code}")
        except Exception as e:
            print(f"Error occurred while downloading audio from '{url}': {str(e)}")

def get_title_from_url(url):
    # Parse the URL to extract the filename
    parsed_url = urlparse(url)
    # Extract the filename from the path
    filename = os.path.basename(parsed_url.path)
    # Remove file extension if present
    filename = os.path.splitext(filename)[0]
    return filename

# Example usage
webpage_url = 'https://omny.fm/shows/jabulujule-9-12'
output_folder = r"C:\Users\thand\OneDrive\Documents\Botlale Ai\Data_Processing\TTS-data-processing\Audio"
download_audio_from_webpage(webpage_url, output_folder)
