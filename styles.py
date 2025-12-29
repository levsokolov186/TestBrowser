def get_styles(theme='dark'):
    if theme == 'dark': # dark theme
        return """
        QMainWindow, QTabWidget::pane { background-color: #1a1a2e; color: #e5e5e5; }
        QToolBar { background-color: #16213e; border-bottom: 1px solid #0f1a3a; padding: 5px; spacing: 8px; }
        /* Вкладки */
        QTabBar::tab { background-color: #16213e; color: #e5e5e5; padding: 8px 20px; border: 1px solid #0f1a3a; border-top-left-radius: 5px; border-top-right-radius: 5px; margin-right: 2px; }
        QTabBar::tab:selected { background-color: #1a1a2e; border-bottom-color: #1a1a2e; }

        QLineEdit { background-color: #232946; border: 1px solid #4a4e69; border-radius: 16px; padding: 6px 15px; font-size: 14px; color: #e5e5e5; }
        QLineEdit:focus { border: 1px solid #0078d4; background-color: #2a315e; }
        QPushButton#NavButton { background-color: #232946; color: #e5e5e5; border: none; border-radius: 14px; padding: 6px 10px; font-size: 16px; min-width: 28px; }
        QPushButton#NavButton:hover { background-color: #0f3460; }
        QDialog { background-color: #1a1a2e; border: 1px solid #4a4e69; }
        QListWidget { background-color: #1a1a2e; border: none; color: #e5e5e5; }
        QListWidget::item:selected { background-color: #0078d4; color: white; }
        /* Прогресс-бар */
        QProgressBar { border: 1px solid #0078d4; border-radius: 5px; text-align: center; background-color: #1a1a2e; color: white; margin: 0px 5px 5px 5px; }
        QProgressBar::chunk { background-color: #0078d4; }
        """
    else:  # light theme
        return """
        QMainWindow, QTabWidget::pane { background-color: #f0f0f0; color: #333; }
        QToolBar { background-color: #fff; border-bottom: 1px solid #ddd; padding: 5px; spacing: 8px; }
        QTabBar::tab { background-color: #eee; color: #333; padding: 8px 20px; border: 1px solid #ccc; border-top-left-radius: 5px; border-top-right-radius: 5px; margin-right: 2px;}
        QTabBar::tab:selected { background-color: #fff; border-bottom-color: #fff; }

        QLineEdit { background-color: #eee; border: 1px solid #ccc; border-radius: 16px; padding: 6px 15px; font-size: 14px; color: #333; }
        QLineEdit:focus { border: 1px solid #0078d4; background-color: #fff; }
        QPushButton#NavButton { background-color: #e0e0e0; color: #333; border: none; border-radius: 14px; padding: 6px 10px; font-size: 16px; min-width: 28px; }
        QPushButton#NavButton:hover { background-color: #d0d0d0; }
        QDialog { background-color: #fff; border: 1px solid #ccc; }
        QListWidget { background-color: #fff; border: none; color: #333; }
        QListWidget::item:selected { background-color: #0078d4; color: white; }
        QProgressBar { border: 1px solid #0078d4; border-radius: 5px; text-align: center; background-color: #f0f0f0; color: black; margin: 0px 5px 5px 5px; }
        QProgressBar::chunk { background-color: #0078d4; }
        """

