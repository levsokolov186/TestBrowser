from PyQt6.QtWidgets import *
from PyQt6.QtCore import QUrl


class SettingsWindow(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.browser = parent
        self.setWindowTitle("Nexus Settings Dashboard")
        self.setFixedSize(800, 600)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        self.tabs = QTabWidget()
        layout.addWidget(self.tabs)

        # Profile Tab
        self._add_profile_tab()

        # Secured Data Tabs
        if self.browser.current_user:
            self._add_data_tab("Bookmarks", "bookmarks", "⭐")
            self._add_data_tab("History", "history", "🕒")

        # Appearance Tab
        self._add_appearance_tab()

    def _add_profile_tab(self):
        tab = QWidget()
        l = QVBoxLayout(tab)
        if not self.browser.current_user:
            self.u_input = QLineEdit(placeholderText="Username")
            self.p_input = QLineEdit(placeholderText="Password")
            self.p_input.setEchoMode(QLineEdit.EchoMode.Password)

            btn_box = QHBoxLayout()
            btn_login = QPushButton("Login")
            btn_reg = QPushButton("Register")

            btn_login.clicked.connect(self.handle_login)
            btn_reg.clicked.connect(self.handle_register)

            btn_box.addWidget(btn_login)
            btn_box.addWidget(btn_reg)
            l.addWidget(QLabel("### Cloud Sync Profile"))
            l.addWidget(self.u_input)
            l.addWidget(self.p_input)
            l.addLayout(btn_box)
        else:
            l.addWidget(QLabel(f"### Welcome, {self.browser.current_user['username']}!"))
            btn_logout = QPushButton("Logout")
            btn_logout.clicked.connect(self.logout)
            l.addWidget(btn_logout)
        self.tabs.addTab(tab, "Profile")

    def _add_data_tab(self, name, table, icon):
        tab = QWidget()
        l = QVBoxLayout(tab)
        list_w = QListWidget()
        data = self.browser.db.get_user_data(self.browser.current_user['id'], table)
        for entry in data:
            item = QListWidgetItem(f"{icon} {entry['title']}")
            item.setToolTip(entry['url'])
            list_w.addItem(item)
        list_w.itemDoubleClicked.connect(self.open_link)
        l.addWidget(QLabel(f"Double-click to open {name.lower()} in a new tab:"))
        l.addWidget(list_w)
        self.tabs.addTab(tab, name)

    def _add_appearance_tab(self):
        tab = QWidget()
        l = QGridLayout(tab)
        themes = ['dark', 'arctic', 'gold', 'matrix', 'sakura', 'midnight']
        for idx, theme in enumerate(themes):
            btn = QPushButton(theme.upper())
            btn.clicked.connect(lambda ch, t=theme: self.browser.update_theme(t))
            l.addWidget(btn, idx // 3, idx % 3)
        self.tabs.addTab(tab, "Appearance")

    def handle_login(self):
        user = self.browser.db.login_user(self.u_input.text(), self.p_input.text())
        if user:
            self.browser.current_user = user
            self.accept()
        else:
            QMessageBox.warning(self, "Nexus", "Login failed!")

    def handle_register(self):
        if self.browser.db.register_user(self.u_input.text(), self.p_input.text()):
            QMessageBox.information(self, "Nexus", "Registered successfully! Now Login.")
        else:
            QMessageBox.critical(self, "Nexus", "Username already taken!")

    def open_link(self, item):
        self.browser.add_new_tab(QUrl(item.toolTip()))
        self.accept()

    def logout(self):
        self.browser.current_user = None
        self.accept()
