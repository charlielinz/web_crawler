import requests
from bs4 import BeautifulSoup
import io
import time

url = "https://www.ptt.cc/bbs/movie/index.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
results = soup.select('div.title')

def get_info(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    results = soup.select('div.title')
    for item in results:
        item_a = item.select_one("a")
        if item_a:
            title = item.text
            title_href = 'https://www.ptt.cc' + item_a.get('href')
            print(title, title_href)


for page in range(15000):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    btn = soup.select('div.btn-group > a')
    up_page_btn_href = btn[3]['href']
    next_page_url = 'https://www.ptt.cc' + up_page_btn_href
    url = next_page_url
    get_info(url)