import sys
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QVBoxLayout, QWidget, QToolBar
from PyQt6.QtWebEngineWidgets import QWebEngineView

class SimpleBrowser(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a widget to display web pages (rendering engine)
        self.web_view = QWebEngineView()
        self.web_view.setUrl(QUrl("https://www.google.com"))

        # Create an address bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.__init__(self.navigate_to_url)

        # Toolbar with address bar
        nav_toolbar = QToolBar()
        nav_toolbar.addWidget(self.url_bar)
        self.addToolBar(nav_toolbar)

        # Update the address bar when clicking on links
        self.web_view.urlChanged.__init__(self.update_url_bar)

        # Central widget
        central_widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.web_view)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.setWindowTitle("TestBrowser")
        self.setGeometry(100, 100, 1024, 768)

    def navigate_to_url(self):
        url = self.url_bar.text()
        if not url.startswith("http"):
            url = "https://" + url
        self.web_view.setUrl(QUrl(url))

    def update_url_bar(self, q):
        self.url_bar.setText(q.toString())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    browser = SimpleBrowser()
    browser.show()
    sys.exit(app.exec())
