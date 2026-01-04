def get_styles(theme='dark'):
    palettes = {
        'dark':     {'bg': '#05070a', 'toolbar': '#0f172a', 'btn': '#1e293b', 'text': '#f8fafc', 'accent': '#38bdf8'},
        'arctic':   {'bg': '#f8fafc', 'toolbar': '#ffffff', 'btn': '#f1f5f9', 'text': '#0f172a', 'accent': '#0284c7'},
        'gold':     {'bg': '#0c0a05', 'toolbar': '#1a160d', 'btn': '#332b1a', 'text': '#fffbeb', 'accent': '#f59e0b'},
        'matrix':   {'bg': '#000000', 'toolbar': '#001100', 'btn': '#002200', 'text': '#00FF00', 'accent': '#008800'},
        'sakura':   {'bg': '#fff5f7', 'toolbar': '#ffebee', 'btn': '#fce4ec', 'text': '#880e4f', 'accent': '#ec407a'},
        'midnight': {'bg': '#1a1a2e', 'toolbar': '#16213e', 'btn': '#0f3460', 'text': '#e94560', 'accent': '#e94560'}
    }
    c = palettes.get(theme, palettes['dark'])
    return f"""
        QMainWindow, QDialog, QWidget {{ background-color: {c['bg']}; color: {c['text']}; font-family: 'Segoe UI'; }}
        QToolBar {{ background-color: {c['toolbar']}; border-bottom: 2px solid {c['accent']}44; padding: 6px; spacing: 8px; }}
        QPushButton {{ background-color: {c['btn']}; border-radius: 12px; padding: 8px; color: {c['text']}; border: 1px solid rgba(255,255,255,0.1); }}
        QPushButton:hover {{ background-color: {c['accent']}; color: white; }}
        QLineEdit {{ background-color: rgba(128,128,128,0.1); border-radius: 14px; padding: 10px; color: {c['text']}; border: 1px solid transparent; }}
        QLineEdit:focus {{ border: 1px solid {c['accent']}; }}
        QTabBar::tab {{ background: transparent; padding: 12px 25px; color: {c['text']}; opacity: 0.6; }}
        QTabBar::tab:selected {{ background: {c['btn']}; border-radius: 12px; opacity: 1; border-bottom: 3px solid {c['accent']}; }}
        QListWidget {{ background: rgba(0,0,0,0.2); border-radius: 15px; border: 1px solid {c['accent']}22; }}
    """
