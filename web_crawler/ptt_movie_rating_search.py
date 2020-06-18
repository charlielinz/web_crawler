import requests
from bs4 import BeautifulSoup
import io
import time
import unicodedata


def chr_width(c):
    if unicodedata.east_asian_width(c) in ('F', 'W', 'A'):
        return 2
    else:
        return 1


url = "https://www.ptt.cc/bbs/movie/index.html"
nice_movie_list = []
nice_movie_link_list = []
normal_movie_list = []
normal_movie_link_list = []
bad_movie_list = []
bad_movie_link_list = []


def get_info(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    results = soup.select('div.title')

    for item in results:
        item_a = item.select_one("a")
        if item_a:

            title = item.text
            title_href = 'https://www.ptt.cc' + item_a.get('href')
            title_fixed = title.replace("\n", "")

            if title_fixed[1:3] == '好雷':
                nice_movie_list.append(title_fixed)
                nice_movie_link_list.append(title_href)
            elif title_fixed[1:3] == '普雷':
                normal_movie_list.append(title_fixed)
                normal_movie_link_list.append(title_href)
            elif title_fixed[1:3] == '負雷':
                bad_movie_list.append(title_fixed)
                bad_movie_link_list.append(title_href)


"""
enter how many pages of latest articles you want to grab below
"""

number_of_pages = 3

for page in range(number_of_pages):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    btn = soup.select('div.btn-group > a')
    up_page_btn_href = btn[3]['href']
    next_page_url = 'https://www.ptt.cc' + up_page_btn_href
    url = next_page_url
    get_info(url)


print("")

for num in range(len(nice_movie_list)):
    length = 0 
    for word in nice_movie_list[num]:
        length += chr_width(word)
    nice_movie_list[num] += ' '*(70-length)
    print(nice_movie_list[num],nice_movie_link_list[num])
    print("")
    num += num

print("-"*60)

for num in range(len(normal_movie_list)):
    length = 0 
    for word in normal_movie_list[num]:
        length += chr_width(word)
    normal_movie_list[num] += ' '*(70-length)
    print(normal_movie_list[num],normal_movie_link_list[num])
    print("")
    num += num

print("-"*60)

for num in range(len(bad_movie_list)):
    length = 0 
    for word in bad_movie_list[num]:
        length += chr_width(word)
    bad_movie_list[num] += ' '*(70-length)
    print(bad_movie_list[num],bad_movie_link_list[num])
    print(""*60)
    num += num
