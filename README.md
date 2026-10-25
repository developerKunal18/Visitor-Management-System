# Visitor Management System

A simple, menu-driven Visitor Management System developed using Python. The application helps offices register visitors, track check-in and check-out times, search visitor records, and generate reports.

## Features

- Register new visitors with automatic visitor IDs
- Record visitor name, phone number, purpose, department, and person to meet
- Check visitors in and out
- Search by visitor ID, name, or phone number
- View all visitors and currently checked-in visitors
- Edit visitor details
- Generate daily visitor reports
- Generate department-wise reports
- Store data in a JSON file
- Use a simple command-line interface

## Technologies Used

- Python
- JSON
- Python Standard Library

## Project Structure

```text
Visitor-Management-System/
├── main.py
├── config.py
├── storage.py
├── visitor_manager.py
├── report_manager.py
├── utils.py
├── requirements.txt
├── .gitignore
├── README.md
└── data/
    └── visitors.json
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Visitor-Management-System.git
```

### 2. Open the project directory

```bash
cd Visitor-Management-System
```

### 3. Run the application

Python 3.10 or later is recommended.

```bash
python main.py
```

No external packages are required.

## How to Use

1. Select **Register New Visitor** to record a visitor.
2. Save the visitor ID displayed after registration.
3. Use **Search Visitor** to find a visitor's details.
4. Select **Check Out Visitor** when the visitor leaves.
5. View currently checked-in visitors to see who is still inside.
6. Generate daily or department-wise reports as required.

## Data Storage

Visitor records are stored in `data/visitors.json`. The application creates this file automatically if it does not exist.

**Note:** This is a basic educational project. It does not include user authentication, database integration, or concurrent-user support.

## Learning Outcomes

- Python functions and modules
- Lists and dictionaries
- JSON file handling
- Input validation
- Date and time handling
- Searching and filtering records
- Basic reporting

## Future Improvements

- Add a graphical user interface
- Integrate MySQL or SQLite
- Add administrator login
- Export reports to CSV or PDF
- Add visitor photo capture and ID verification

## Author

Python Project Challenge 

## License

This project is available for educational and personal learning purposes.
