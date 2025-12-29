import sys
import os
from PyQt6.QtCore import QUrl, Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QWidget,
                             QTabWidget, QProgressBar, QDialog, QListWidget)
from PyQt6.QtWebEngineWidgets import QWebEngineView

# Chromium 2025 Optimization
os.environ["QTWEBENGINE_CHROMIUM_FLAGS"] = "--disable-gpu --no-sandbox --enable-smooth-scrolling"

from UIElements import BrowserToolBar
from styles import get_styles


class ModernBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nexus Browser 2025")
        self.setGeometry(100, 100, 1280, 850)

        self.history = []
        self.current_theme = "dark"

        # UI Initialization
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        self.toolbar = BrowserToolBar()
        self.layout.addWidget(self.toolbar)

        self.progress_bar = QProgressBar()
        self.progress_bar.setFixedHeight(2)
        self.progress_bar.setTextVisible(False)
        self.progress_bar.hide()
        self.layout.addWidget(self.progress_bar)

        self.tabs = QTabWidget()
        self.tabs.setDocumentMode(True)
        self.tabs.setTabsClosable(True)
        self.layout.addWidget(self.tabs)

        # Signals
        self._connect_signals()

        # Start State
        self.add_new_tab(QUrl("https://www.google.com"), "Google")
        self.apply_styles()

    def _connect_signals(self):
        self.toolbar.url_entered.connect(self.navigate_to_url)
        self.toolbar.new_tab_requested.connect(lambda: self.add_new_tab(QUrl("https://google.com")))
        self.toolbar.toggle_theme_requested.connect(self.toggle_theme)
        self.toolbar.show_history_requested.connect(self.show_history_window)

        self.tabs.tabCloseRequested.connect(self.close_tab)
        self.tabs.currentChanged.connect(self.sync_ui_with_tab)

        self.toolbar.back_btn.clicked.connect(lambda: self.current_browser() and self.current_browser().back())
        self.toolbar.forward_btn.clicked.connect(lambda: self.current_browser() and self.current_browser().forward())
        self.toolbar.reload_btn.clicked.connect(lambda: self.current_browser() and self.current_browser().reload())

    def current_browser(self):
        return self.tabs.currentWidget()

    def add_new_tab(self, qurl, title="Новая вкладка"):
        browser = QWebEngineView()
        browser.setUrl(qurl)

        index = self.tabs.addTab(browser, title)
        self.tabs.setCurrentIndex(index)

        browser.urlChanged.connect(lambda q: self.on_url_changed(q, browser))
        browser.titleChanged.connect(lambda t: self.on_title_changed(t, browser))
        browser.loadProgress.connect(self.on_load_progress)

    def on_url_changed(self, qurl, browser):
        if self.tabs.currentWidget() == browser:
            self.toolbar.url_bar.setText(qurl.toString())
            url_str = qurl.toString()
            if url_str not in ["about:blank", ""] and (not self.history or self.history[-1] != url_str):
                self.history.append(url_str)

    def on_title_changed(self, title, browser):
        index = self.tabs.indexOf(browser)
        if index != -1:
            display_title = (title[:20] + "..") if len(title) > 20 else title
            self.tabs.setTabText(index, display_title)

    def on_load_progress(self, p):
        self.progress_bar.setValue(p)
        self.progress_bar.setVisible(p < 100)

    def navigate_to_url(self, text):
        text = text.strip()
        if not text: return

        if "." in text and " " not in text:
            url = text if text.startswith("http") else "https://" + text
        else:
            url = f"www.google.com{text}"

        if self.current_browser():
            self.current_browser().setUrl(QUrl(url))

    def sync_ui_with_tab(self, index):
        if index != -1:
            browser = self.tabs.widget(index)
            self.toolbar.url_bar.setText(browser.url().toString())

    def close_tab(self, index):
        if self.tabs.count() > 1:
            self.tabs.removeTab(index)
        else:
            self.add_new_tab(QUrl("https://google.com"))
            self.tabs.removeTab(index)

    def toggle_theme(self):
        self.current_theme = "light" if self.current_theme == "dark" else "dark"
        self.apply_styles()
        # SYNCHRONIZATION ICONS:
        self.toolbar.update_theme_icon(self.current_theme)

    def apply_styles(self):
        self.setStyleSheet(get_styles(self.current_theme))

    def show_history_window(self, pos):
        dlg = QDialog(self)
        dlg.setWindowTitle("История")
        dlg.setMinimumWidth(400)
        layout = QVBoxLayout(dlg)
        list_w = QListWidget()
        list_w.addItems(reversed(self.history[-100:])) # Last 100
        list_w.itemDoubleClicked.connect(lambda i: (self.add_new_tab(QUrl(i.text())), dlg.close()))
        layout.addWidget(list_w)
        dlg.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("Nexus Browser")
    window = ModernBrowser()
    window.show()
    sys.exit(app.exec())
