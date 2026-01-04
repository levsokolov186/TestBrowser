import json, os

def load_local_config():
    if os.path.exists("config.json"):
        with open("config.json", "r") as f: return json.load(f)
    return {"theme": "dark"}

def save_local_config(config):
    with open("config.json", "w") as f: json.dump(config, f)

def prepare_url(text):
    text = text.strip()
    if "." in text and " " not in text:
        return text if text.startswith("http") else "https://" + text
    return f"www.google.com{text}"
