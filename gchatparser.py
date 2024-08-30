
import json
import re
import sys
from pathlib import Path

def format_string(s):
    # Extract all URLs from the string (assuming they're HTTP or HTTPS)
    urls = re.findall('https?://\\S+', s)

    formatted_string = ''
    for url in urls:
        try:  # Try to add URL as a clickable link
            formatted_string += f'<a href="{url}">{url}</a> '
        except Exception as e:  # If invalid, ignore and continue
            print(f"Error processing URL {url}: {str(e)}")
    
    # Extract all image URLs from the string (assuming they're HTTP or HTTPS)
    images = re.findall('https?://\\S+(?:jpg|jpeg|png|gif)$', s)

    for img in images:
        try:  # Try to add URL as an HTML image
            formatted_string += f'<img src="{img}" alt="image"> '
        except Exception as e:  # If invalid, ignore and continue
            print(f"Error processing image {img}: {str(e)}")

    return s if not formatted_string.strip() else formatted_string.strip()





# Load the JSON data from a file or string
with open(sys.argv[1], 'r') as f:
    data = json.load(f)

# Print all messages
f = open(f"{Path(sys.argv[1]).stem}.html", "w")
f.write(f"<Title>{Path(sys.argv[1]).stem} Google Messages</Title>")

for message in data['messages']:
    try:
        f.write(f"<h4>Sent by: {message['creator']['name']}, {message['created_date']} </h4> Text: {format_string(message['text'])}<br/>\n")
    except Exception as e:
        print(f"Error processing json section: {str(e)}")

