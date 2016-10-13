import os
import urllib.request
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
    
    result = []
    for i, item in enumerate(items):
        links = item.find_all('a')
        images_page = get_html(URL + links[0]['href'])
        result.append({
            'images': get_images(images_page),
            'small_image': links[0].img['src'],
            'sku': links[1].text
        })

    return result

def get_images(html):
    pass
    
def save(data):
    pass

def main():
    parse(get_html(URL))

if __name__ == '__main__':
    main()
