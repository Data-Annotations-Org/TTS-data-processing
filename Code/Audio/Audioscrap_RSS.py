import os
import requests
from urllib.parse import urlparse
import re
import xml.etree.ElementTree as ET

def extract_audio_urls_from_rss(rss_url):
    response = requests.get(rss_url)
    if response.status_code == 200:
        # Parse the XML response
        root = ET.fromstring(response.content)
        audio_urls = []
        # Find all <item> elements which represent podcast episodes
        for item in root.findall('.//item'):
            # Find <enclosure> elements which typically contain audio URLs
            enclosure = item.find('enclosure')
            if enclosure is not None:
                audio_url = enclosure.get('url')
                audio_urls.append(audio_url)
        return audio_urls
    else:
        print("Failed to fetch RSS feed:", response.status_code)
        return []

def download_audio_from_rss(rss_feed_url, output_folder):
    # Extract audio URLs from the RSS feed
    audio_urls = extract_audio_urls_from_rss(rss_feed_url)

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

# Example usage with RSS feed URL
rss_feed_url = 'https://omny.fm/shows/moremogolo/playlists/podcast.rss'
output_folder = r"C:\Users\thand\OneDrive\Documents\Botlale Ai\Data_Processing\TTS-data-processing\Audio"
download_audio_from_rss(rss_feed_url, output_folder)
