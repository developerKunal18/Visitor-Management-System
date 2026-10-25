import json
from config import DATA_DIR, VISITORS_FILE


def initialize_storage():
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    if not VISITORS_FILE.exists():
        with VISITORS_FILE.open("w", encoding="utf-8") as file:
            json.dump([], file, indent=4)


def load_visitors():
    initialize_storage()

    try:
        with VISITORS_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            print("Warning: Visitor data must be a JSON list.")
            return []

        return data

    except (json.JSONDecodeError, OSError) as error:
        print(f"Error reading visitor data: {error}")
        return []


def save_visitors(visitors):
    initialize_storage()

    with VISITORS_FILE.open("w", encoding="utf-8") as file:
        json.dump(visitors, file, indent=4, ensure_ascii=False)
