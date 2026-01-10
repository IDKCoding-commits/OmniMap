from PIL import Image, ImageTk
import requests
from io import BytesIO
from nicegui import ui
import asyncio
from crawl4ai import *
import os

def clear_input(text_box):
    text_box.set_value('')

def handle_submit(textarea:str):
    if textarea.strip().lower() == "silksong":
        print("Due to the sheer size and complexity of Silksong, maps for that game are sorted by Act. To get maps for Silksong, simply search 'Silksong Act X'")
    return textarea
    # return lower_value


def search_curated(input, file):
    with open (file, 'r') as file:
        for line in file:
            if input.lower().strip() in line.lower().strip():
                split_line = line.split('=', maxsplit=1)
                print(split_line)
                if split_line[0].strip() == input.lower().strip():
                    print("Got: " + split_line[1])
                    return split_line[1]
                else:
                    pass
            else:
                pass


def on_submit(input_area):
    # get text from the input area
    value = input_area.value
    normalized = handle_submit(value)   # capture returned text
    clear_input(input_area)             # clear the field
    print('normalized:', normalized)
    url = search_curated(input=normalized.strip().lower(), file="currated_map_urls.txt")
    ui.image(url)
    
    # later: use normalized to look up a URL and call map_image.set_source(url)

async def image_crawl(prompt):
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url="https://www.google.com"
        )
