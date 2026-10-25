import json
from config import DATA_DIR, VISITORS_FILE


def initialize_storage():
    """Create the data folder and JSON file if missing."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    if not VISITORS_FILE.exists():
        save_visitors([])


def load_visitors():
    """Load visitor records from JSON."""
    initialize_storage()

    try:
        with VISITORS_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)

        return data if isinstance(data, list) else []

    except (json.JSONDecodeError, OSError):
        print("Warning: Could not read visitor data.")
        return []


def save_visitors(visitors):
    """Save visitor records to JSON."""
    initialize_storage()

    with VISITORS_FILE.open("w", encoding="utf-8") as file:
        json.dump(visitors, file, indent=4, ensure_ascii=False)
