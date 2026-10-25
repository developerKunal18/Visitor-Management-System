from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
VISITORS_FILE = DATA_DIR / "visitors.json"

DATE_FORMAT = "%Y-%m-%d"
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

VISITOR_STATUSES = ("Checked In", "Checked Out")
