import os
import urllib.request

URL = 'http://www.nandomuzi.net/Dropbox/clienti/springsummer2017/'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, 'output')

def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()
    
def parse(html):
    pass

def get_images(html):
    pass
    
def save(data):
    pass

def main():
    get_html(URL)

if __name__ == '__main__':
    main()
