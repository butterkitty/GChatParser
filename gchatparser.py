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
            formatted_string += f'<a href="{url}" target=”_blank”>{url}</a> '
        except Exception as e:  # If invalid, ignore and continue
            print(f"Error processing URL {url}: {str(e)}")
    
    # Extract all image URLs from the string (assuming they're HTTP or HTTPS)
    images = re.findall('https?://\\S+(?:jpg|jpeg|png|gif)$', s)

    for img in images:
        try:  # Try to add URL as an HTML image
            formatted_string += f'<details><summary class=collapsible>LOAD IMAGE</summary><img loading="lazy" src="{img}" alt="image"></details> '
        except Exception as e:  # If invalid, ignore and continue
            print(f"Error processing image {img}: {str(e)}")

    return s if not formatted_string.strip() else formatted_string.strip()

def insert_media(s):
    if (re.search('(?:jpg|jpeg|png|gif)$', s)):
        s = f'<details><summary class=collapsible>LOAD IMAGE</summary><img loading="lazy" src="{Path(sys.argv[1]).parent}/{s}" alt="image"></details> '
    elif (re.search('(?:mp4|mov|avi|mkv)$', s)):
        s = f'<a href="{Path(sys.argv[1]).parent}/{s}">{Path(sys.argv[1]).parent}/{s}</a>'
    return s



# Load the JSON data from a file or string
with open(sys.argv[1], 'r') as f:
    data = json.load(f)

# Print all messages
f = open(f"{Path(sys.argv[1]).stem}.html", "w")
f.write('<style>\n'  \
'/* Style the button that is used to open and close the collapsible content */\n' \
'.collapsible {\n' \
'  background-color: #eee;\n' \
'  color: #444;\n' \
'  cursor: pointer;\n' \
'  padding: 18px;\n' \
'  width: 100%;\n' \
'  border: none;\n' \
'  text-align: left;\n' \
'  outline: none;\n' \
'  font-size: 15px;\n' \
'}\n' \
'\n' \
'/* Add a background color to the button if it is clicked on (add the .active class with JS), and when you move the mouse over it (hover) */\n' \
'.active, .collapsible:hover {\n' \
'  background-color: #ccc;\n' \
'}\n'\
'\n' \
'/* Style the collapsible content. Note: hidden by default */\n' \
'.content {\n' \
'  padding: 0 18px;\n' \
'  display: none;\n' \
'  overflow: hidden;\n' \
'  background-color: #f1f1f1;\n' \
'}\n' \
'</style>\n') 
f.write(f"<Title>{Path(sys.argv[1]).stem} Google Messages</Title>\n")

for message in data['messages']:
    try:
        if (message.get('text',False)):
            f.write(f"<h4>Sent by: {message['creator']['name']}, {message['created_date']} </h4> Text: {format_string(message['text'])}<br/>\n")
        else:
            for attached_file in message['attached_files']:
                f.write(f"<h4>Sent by: {message['creator']['name']}, {message['created_date']} </h4> Text: {insert_media(attached_file['export_name'])}<br/>\n")
    except Exception as e:
        print(f"Error processing json section: {str(e)} Date: {message['created_date']}")

