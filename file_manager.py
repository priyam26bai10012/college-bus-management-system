import json
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")


def load_data(filename):
    path = os.path.join(DATA_DIR, filename)
    if not os.path.exists(path):
        return []
    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []


def save_data(filename, data):
    os.makedirs(DATA_DIR, exist_ok=True)
    path = os.path.join(DATA_DIR, filename)
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def get_next_id(data):
    if not data:
        return 1
    return max(item["id"] for item in data) + 1
