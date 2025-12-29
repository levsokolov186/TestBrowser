import json
import os

BOOKMARKS_FILE = 'bookmarks.json'

def load_bookmarks():
    if os.path.exists(BOOKMARKS_FILE):
        try:
            with open(BOOKMARKS_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []

def save_bookmarks(bookmarks):
    with open(BOOKMARKS_FILE, 'w', encoding='utf-8') as f:
        json.dump(bookmarks, f, ensure_ascii=False, indent=4)

def add_bookmark(title, url):
    bookmarks = load_bookmarks()
    if not any(b['url'] == url for b in bookmarks):
        bookmarks.append({'title': title, 'url': url})
        save_bookmarks(bookmarks)
