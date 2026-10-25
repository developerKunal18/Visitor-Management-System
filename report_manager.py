from datetime import datetime
from storage import load_visitors
from config import DATE_FORMAT


def daily_report():
    visitors = load_visitors()
    today = datetime.now().strftime(DATE_FORMAT)

    todays_visitors = [
        visitor for visitor in visitors
        if visitor.get("check_in", "").startswith(today)
    ]

    checked_out = sum(
        1 for visitor in todays_visitors
        if visitor.get("status") == "Checked Out"
    )

    checked_in = sum(
        1 for visitor in todays_visitors
        if visitor.get("status") == "Checked In"
    )

    print("\n========== DAILY VISITOR REPORT ==========")
    print(f"Date                  : {today}")
    print(f"Total visitors today  : {len(todays_visitors)}")
    print(f"Currently checked in  : {checked_in}")
    print(f"Checked out           : {checked_out}")

    if todays_visitors:
        print("\nVisitor details:")

        for visitor in todays_visitors:
            print(
                f"{visitor.get('visitor_id')} | "
                f"{visitor.get('name')} | "
                f"{visitor.get('purpose')} | "
                f"{visitor.get('status')}"
            )

    print("=" * 42)


def department_report():
    visitors = load_visitors()

    if not visitors:
        print("No visitor records available.")
        return

    counts = {}

    for visitor in visitors:
        department = visitor.get("department", "Unknown")
        counts[department] = counts.get(department, 0) + 1

    print("\n--- Visitors by Department ---")

    for department, count in sorted(counts.items()):
        print(f"{department}: {count}")

    print(f"Total visitor records: {len(visitors)}")
