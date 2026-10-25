from datetime import datetime
from storage import load_visitors, save_visitors
from utils import get_text, get_phone, current_datetime


def generate_visitor_id(visitors):
    """Generate the next visitor ID."""
    highest_id = 0

    for visitor in visitors:
        visitor_id = visitor.get("visitor_id", "")

        if visitor_id.startswith("VIS"):
            try:
                number = int(visitor_id[3:])
                highest_id = max(highest_id, number)
            except ValueError:
                continue

    return f"VIS{highest_id + 1:04d}"


def register_visitor():
    visitors = load_visitors()

    print("\n--- Register Visitor ---")

    name = get_text("Enter visitor name: ")
    phone = get_phone()
    purpose = get_text("Enter purpose of visit: ")
    person_to_meet = get_text("Person to meet: ")
    department = get_text("Enter department: ")

    visitor = {
        "visitor_id": generate_visitor_id(visitors),
        "name": name,
        "phone": phone,
        "purpose": purpose,
        "person_to_meet": person_to_meet,
        "department": department,
        "check_in": current_datetime(),
        "check_out": None,
        "status": "Checked In"
    }

    visitors.append(visitor)
    save_visitors(visitors)

    print("\nVisitor registered successfully.")
    print(f"Visitor ID: {visitor['visitor_id']}")
    print(f"Name: {visitor['name']}")
    print(f"Check-in time: {visitor['check_in']}")


def display_visitor(visitor):
    print("-" * 45)
    print(f"Visitor ID    : {visitor.get('visitor_id', '')}")
    print(f"Name          : {visitor.get('name', '')}")
    print(f"Phone         : {visitor.get('phone', '')}")
    print(f"Purpose       : {visitor.get('purpose', '')}")
    print(f"Person to Meet: {visitor.get('person_to_meet', '')}")
    print(f"Department    : {visitor.get('department', '')}")
    print(f"Check-in      : {visitor.get('check_in', '')}")
    print(f"Check-out     : {visitor.get('check_out') or 'Not checked out'}")
    print(f"Status        : {visitor.get('status', '')}")


def list_visitors():
    visitors = load_visitors()

    print("\n--- All Visitors ---")

    if not visitors:
        print("No visitor records found.")
        return

    for visitor in visitors:
        display_visitor(visitor)

    print("-" * 45)
    print(f"Total visitors: {len(visitors)}")


def search_visitor():
    visitors = load_visitors()

    if not visitors:
        print("No visitor records available.")
        return

    keyword = input(
        "Enter visitor ID, name, or phone number: "
    ).strip().lower()

    if not keyword:
        print("Please enter a search value.")
        return

    results = [
        visitor for visitor in visitors
        if keyword in visitor.get("visitor_id", "").lower()
        or keyword in visitor.get("name", "").lower()
        or keyword in visitor.get("phone", "").lower()
    ]

    if not results:
        print("No matching visitors found.")
        return

    print(f"\nFound {len(results)} matching visitor(s).")

    for visitor in results:
        display_visitor(visitor)


def check_out_visitor():
    visitors = load_visitors()

    visitor_id = input("Enter visitor ID to check out: ").strip().upper()

    if not visitor_id:
        print("Visitor ID cannot be empty.")
        return

    for visitor in visitors:
        if visitor.get("visitor_id", "").upper() == visitor_id:
            if visitor.get("status") == "Checked Out":
                print("This visitor has already checked out.")
                return

            visitor["check_out"] = current_datetime()
            visitor["status"] = "Checked Out"
            save_visitors(visitors)

            print("Visitor checked out successfully.")
            print(f"Visitor: {visitor.get('name', '')}")
            print(f"Check-out time: {visitor['check_out']}")
            return

    print("Visitor ID not found.")


def list_checked_in_visitors():
    visitors = load_visitors()

    active_visitors = [
        visitor for visitor in visitors
        if visitor.get("status") == "Checked In"
    ]

    print("\n--- Visitors Currently Inside ---")

    if not active_visitors:
        print("No visitors are currently checked in.")
        return

    for visitor in active_visitors:
        display_visitor(visitor)

    print(f"\nCurrently inside: {len(active_visitors)}")


def edit_visitor_details():
    visitors = load_visitors()
    visitor_id = input("Enter visitor ID to edit: ").strip().upper()

    for visitor in visitors:
        if visitor.get("visitor_id", "").upper() == visitor_id:
            print("Leave a field blank to keep its current value.")

            name = input(f"Name [{visitor['name']}]: ").strip()
            purpose = input(f"Purpose [{visitor['purpose']}]: ").strip()
            person = input(
                f"Person to meet [{visitor['person_to_meet']}]: "
            ).strip()
            department = input(
                f"Department [{visitor['department']}]: "
            ).strip()

            if name:
                visitor["name"] = name
            if purpose:
                visitor["purpose"] = purpose
            if person:
                visitor["person_to_meet"] = person
            if department:
                visitor["department"] = department

            save_visitors(visitors)
            print("Visitor details updated successfully.")
            return

    print("Visitor ID not found.")
