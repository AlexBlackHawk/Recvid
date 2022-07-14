import requests
from bs4 import BeautifulSoup as BS
import re


class MovieNews:
    def __init__(self):
        self.__url = "https://www.imdb.com/news/movie/?ref_=nv_nw_mv"
        self.__html_code = self.__code()

    def __code(self):
        r = requests.get(self.__url)
        html = BS(r.content, 'html.parser')
        return html

    def titles(self):
        second_headers = self.__html_code.find_all('h2', class_='news-article__title')
        all_titles = []
        for header in second_headers:
            all_titles.append(header.text.strip())
        return all_titles

    def images(self):
        imgs = self.__html_code.find_all('img', class_='news-article__image')
        all_images = []
        for img in imgs:
            all_images.append(img['src'])
        return all_images

    def texts(self):
        txts = self.__html_code.find_all('div', class_='news-article__content')
        all_texts = []
        for txt in txts:
            txt = txt.text
            re.sub('<a href="[a-z]*">', "", txt)
            txt.replace("</a>", "")
            all_texts.append(txt.strip())
        return all_texts
