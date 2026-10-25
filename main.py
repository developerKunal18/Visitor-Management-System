from storage import initialize_storage
from visitor_manager import (
    register_visitor,
    list_visitors,
    search_visitor,
    check_out_visitor,
    list_checked_in_visitors,
    edit_visitor_details
)
from report_manager import daily_report, department_report
from utils import pause


def show_menu():
    print("\n" + "=" * 42)
    print("       VISITOR MANAGEMENT SYSTEM")
    print("=" * 42)
    print("1. Register New Visitor")
    print("2. View All Visitors")
    print("3. Search Visitor")
    print("4. Check Out Visitor")
    print("5. View Currently Checked-In Visitors")
    print("6. Edit Visitor Details")
    print("7. Daily Visitor Report")
    print("8. Department-Wise Report")
    print("0. Exit")
    print("=" * 42)


def main():
    initialize_storage()

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            register_visitor()
            pause()

        elif choice == "2":
            list_visitors()
            pause()

        elif choice == "3":
            search_visitor()
            pause()

        elif choice == "4":
            check_out_visitor()
            pause()

        elif choice == "5":
            list_checked_in_visitors()
            pause()

        elif choice == "6":
            edit_visitor_details()
            pause()

        elif choice == "7":
            daily_report()
            pause()

        elif choice == "8":
            department_report()
            pause()

        elif choice == "0":
            print("Thank you for using Visitor Management System!")
            break

        else:
            print("Invalid choice. Please select a valid option.")
            pause()


if __name__ == "__main__":
    main()
