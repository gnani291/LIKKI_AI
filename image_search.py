from duckduckgo_search import DDGS
import time

def search_images(query):

    images = []

    time.sleep(2)

    with DDGS() as ddgs:
        for img in ddgs.images(query, max_results=6):
            images.append(img["image"])

    return images

