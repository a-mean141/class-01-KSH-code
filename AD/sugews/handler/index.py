from PyQt5.QtWidgets import *
import requests
import urllib.request
import webbrowser
from modules.db import save_routes, save_title, get_title, get_recomended_destinations


class Handler:
    def __init__(self, widget):
        self.widget = widget
        self.category = ''
        self.query = False
        self.previous_query = ''
        self.start = 1
        self.links = []
        self.routes = []

    def set_category(self, category):
        self.category = category
        self.search()

    def search_news(self):
        text, ok = QInputDialog.getText(self.widget, '검색', '검색어를 입력하세요.')
        if ok:
            self.query = text
            self.search()

    def search(self):
        if self.query:
            query = self.query
            self.query = False
        else:
            query = self.category
        if query != self.previous_query:
            self.start = 1
        self.previous_query = query
        self.request(query)

    def request(self, query):
        headers = {
        }
        params = (
            ('query', urllib.parse.quote(query)),
            ('display', '8'),
            ('start', self.start),
            ('sort', 'sim')
        )
        response = requests.get(
            'https://openapi.naver.com/v1/search/news.json', headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            titles = []
            self.links = []
            for i in range(len(data['items'])):
                title = data['items'][i]['title']
                titles.append(title)
                link = data['items'][i]['originallink']
                self.links.append(link)
                save_title(title, link)
            self.widget.set_buttons_title(titles)

    def click_news(self, i):
        def handler():
            if len(self.links) <= i:
                return
            webbrowser.open_new(self.links[i])
            self.routes.append(self.links[i])
            recomended_destinations = get_recomended_destinations(self.routes)
            if len(recomended_destinations) > 0:
                reply = QMessageBox.question(self.widget, '추천 기사',
                                             '추천 기사가 있습니다. 확인하시겠어요?', QMessageBox.Yes, QMessageBox.No)

                if reply == QMessageBox.Yes:
                    titles = []
                    for link in recomended_destinations:
                        titles.append(get_title(link))
                    self.links = recomended_destinations
                    self.widget.set_buttons_title(titles)
        return handler

    def save_routes(self):
        while len(self.routes) > 1:
            save_routes(self.routes)
            self.routes.pop()
