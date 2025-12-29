from PyQt6.QtWidgets import QToolBar, QPushButton, QLineEdit
from PyQt6.QtCore import pyqtSignal, QPoint


class BrowserToolBar(QToolBar):
    url_entered = pyqtSignal(str)
    show_history_requested = pyqtSignal(QPoint)
    toggle_theme_requested = pyqtSignal()
    new_tab_requested = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setObjectName("MainToolbar")
        self.setMovable(False)
        self.setFloatable(False)

        self.back_btn = QPushButton("←")
        self.back_btn.setObjectName("NavButton")

        self.forward_btn = QPushButton("→")
        self.forward_btn.setObjectName("NavButton")

        self.reload_btn = QPushButton("↻")
        self.reload_btn.setObjectName("NavButton")

        self.history_btn = QPushButton("🕒")
        self.history_btn.setObjectName("NavButton")
        self.history_btn.clicked.connect(self._emit_history)

        self.url_bar = QLineEdit()
        self.url_bar.setPlaceholderText("Введите запрос или URL...")
        self.url_bar.returnPressed.connect(self.emit_url)

        self.theme_btn = QPushButton("🌙")
        self.theme_btn.setObjectName("NavButton")
        self.theme_btn.clicked.connect(self.toggle_theme_requested.emit)

        self.new_tab_btn = QPushButton("+")
        self.new_tab_btn.setObjectName("NavButton")
        self.new_tab_btn.clicked.connect(self.new_tab_requested.emit)

        # Order of elements
        self.addWidget(self.back_btn)
        self.addWidget(self.forward_btn)
        self.addWidget(self.reload_btn)
        self.addSeparator()
        self.addWidget(self.url_bar)
        self.addWidget(self.history_btn)
        self.addWidget(self.theme_btn)
        self.addWidget(self.new_tab_btn)

    def _emit_history(self):
        pos = self.history_btn.mapToGlobal(QPoint(0, self.history_btn.height()))
        self.show_history_requested.emit(pos)

    def emit_url(self):
        self.url_entered.emit(self.url_bar.text())

    def update_theme_icon(self, theme):
        self.theme_btn.setText("☀️" if theme == "light" else "🌙")
