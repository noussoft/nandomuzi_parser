#!/usr/bin/env python3

import os
import sys
import urllib.request
from urllib.request import urlretrieve
from bs4 import BeautifulSoup

URL = 'http://www.nandomuzi.net/Dropbox/clienti/springsummer2017/'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, 'output')

def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()
    
def parse(html):
    soup = BeautifulSoup(html, "html.parser")
    shoes_list = soup.find('ul', class_="shoes")
    items = shoes_list.find_all('li')
    print_info("Parsing (up to {}):".format(len(items)))
    result = []
    for i, item in enumerate(items):
        print_info(i)
        links = item.find_all('a')
        images_page = get_html(URL + links[0]['href'])
        result.append({
            'images': get_images(images_page),
            'small_image': links[0].img['src'],
            'sku': links[1].text
        })
    return result

def get_images(html):
    soup = BeautifulSoup(html, "html.parser")
    image_list = soup.find('div', class_="blocco_immagini")
    image_links = image_list.find_all('a')
    result = []
    for link in image_links:
        result.append(link['href'].split("=")[1])
    return result
    
def save(data):
    print_info("\nSaving (up to {}):".format(len(data)))
    for i, item in enumerate(data):
        print_info(i)
        path = os.path.join(OUTPUT_DIR, item['sku']) 
        if not os.path.exists(path):
            os.makedirs(path)
        for image in item['images']:
            file_to_save = image.rsplit('/')[2]
            urlretrieve(URL + image, os.path.join(path, file_to_save))

def print_info(info):
    print(info, end=" ")
    sys.stdout.flush()

def main():
    save(parse(get_html(URL)))
    print("\nJob is done")

if __name__ == '__main__':
    main()
