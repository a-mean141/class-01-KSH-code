import sys
from handler.index import Handler
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import webbrowser


class Index(QWidget):
    def __init__(self):
        self.handler = Handler(self)
        super().__init__()
        self.resize(640, 380)
        self.setWindowTitle('메인')
        self.layout = QVBoxLayout()
        self.layout.addLayout(self.draw_header())
        self.layout.setAlignment(Qt.AlignTop)
        self.draw_body()
        self.setLayout(self.layout)

    def draw_header(self):
        header_layout = QHBoxLayout()
        label = QLabel('카테고리')
        header_layout.addWidget(label)

        self.category = QComboBox()
        self.category.addItems(
            ['정치', '경제', '사회', '스포츠', '날씨']
        )
        self.category.resize(100, 30)
        self.category.currentTextChanged.connect(self.handler.set_category)
        header_layout.addWidget(self.category)
        header_layout.addStretch()
        search_button = QPushButton('검색')
        header_layout.addWidget(search_button)
        search_button.clicked.connect(self.handler.search_news)
        return header_layout

    def draw_body(self):
        self.news = []
        for i in range(8):
            button = QPushButton('')
            self.news.append(button)
            self.layout.addWidget(button)
            button.clicked.connect(self.handler.click_news(i))
        self.handler.request(self.category.currentText())

    def set_buttons_title(self, titles):
        while len(titles) < 8:
            titles.append('')
        for i in range(len(titles)):
            title = titles[i]
            self.news[i].setText(title)

    def closeEvent(self, event):
        self.handler.save_routes()


app = QApplication(sys.argv)
ex = Index()
ex.show()
sys.exit(app.exec_())
