import sys
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import *
from PyQt6.QtWebEngineWidgets import QWebEngineView

from database import BrowserDB
from styles import get_styles
from utils import load_local_config, save_local_config, prepare_url
from ui_elements import SettingsWindow


class NexusBrowser(QMainWindow):
    """Core Browser Controller 2026."""

    def __init__(self):
        super().__init__()
        self.db = BrowserDB()
        self.config = load_local_config()
        self.current_user = None

        self.setWindowTitle("Nexus Browser 2026")
        self.resize(1400, 900)
        self._build_ui()
        self.add_new_tab()

    def _build_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # Toolbar Components
        self.toolbar = QToolBar()
        self.toolbar.setMovable(False)
        layout.addWidget(self.toolbar)

        self._btn("←", lambda: self.current_view().back())
        self._btn("→", lambda: self.current_view().forward())
        self._btn("↻", lambda: self.current_view().reload())

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate)
        self.toolbar.addWidget(self.url_bar)

        self._btn("⭐", self.add_bookmark)
        self._btn("+", lambda: self.add_new_tab())
        self._btn("⚙", self.open_settings)

        self.tabs = QTabWidget(documentMode=True, tabsClosable=True)
        self.tabs.tabCloseRequested.connect(self._close_tab)
        layout.addWidget(self.tabs)
        self.update_theme(self.config.get('theme', 'dark'))

    def _btn(self, text, slot):
        btn = QPushButton(text)
        btn.setFixedWidth(50)
        btn.clicked.connect(slot)
        self.toolbar.addWidget(btn)

    def current_view(self):
        return self.tabs.currentWidget()

    def add_new_tab(self, qurl=QUrl("https://google.com")):
        view = QWebEngineView()
        idx = self.tabs.addTab(view, "New Tab")
        self.tabs.setCurrentIndex(idx)
        view.setUrl(qurl)
        view.urlChanged.connect(lambda q: self.url_bar.setText(q.toString()))
        view.loadFinished.connect(lambda: self._on_page_load(view))

    def _on_page_load(self, view):
        title = view.page().title() or "Nexus"
        self.tabs.setTabText(self.tabs.indexOf(view), title[:15])
        if self.current_user:
            self.db.save_data(self.current_user['id'], title, view.url().toString(), "history")

    def navigate(self):
        target = prepare_url(self.url_bar.text())
        self.current_view().setUrl(QUrl(target))

    def add_bookmark(self):
        if not self.current_user:
            QMessageBox.warning(self, "Nexus", "Login required for cloud bookmarks!")
            return
        v = self.current_view()
        self.db.save_data(self.current_user['id'], v.page().title(), v.url().toString(), "bookmarks")
        QMessageBox.information(self, "Nexus", "Synced to cloud!")

    def open_settings(self):
        if SettingsWindow(self).exec():
            self.update_theme(self.config['theme'])

    def update_theme(self, tid):
        self.config['theme'] = tid
        save_local_config(self.config)
        self.setStyleSheet(get_styles(tid))

    def _close_tab(self, i):
        if self.tabs.count() > 1: self.tabs.removeTab(i)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    b = NexusBrowser()
    b.show()
    sys.exit(app.exec())
