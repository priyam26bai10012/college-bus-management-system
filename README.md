# College Bus Management System

A beginner-friendly Python command-line project for managing college students, buses, routes, bus allocations, attendance, and reports.

## Features

- Student Management
- Bus Management
- Route Management
- Student Bus Allocation
- Daily Attendance
- Bus Occupancy Reports
- Route-wise Student Reports
- Student Bus Details
- Attendance Summary
- JSON-based data storage
- Input validation and error handling
- Basic unit tests

## Technologies Used

- Python 3
- JSON
- Python standard library
- unittest

No external Python packages are required.

## Project Structure

```text
college-bus-management/
├── main.py
├── student.py
├── bus.py
├── route.py
├── allocation.py
├── attendance.py
├── reports.py
├── file_manager.py
├── validators.py
├── data/
│   ├── students.json
│   ├── buses.json
│   ├── routes.json
│   ├── allocations.json
│   └── attendance.json
├── tests/
│   └── test_project.py
├── README.md
└── statement.md
```

## Requirements

Python 3.8 or newer is recommended.

Check your Python installation:

```bash
python --version
```

On some Windows installations, use:

```bash
py --version
```

## Installation

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Make sure Python 3 is installed.
4. No external dependencies need to be installed.

## Run the Project

From the project root:

```bash
python main.py
```

On Windows, if `python` does not work:

```bash
py main.py
```

The program opens a terminal menu:

```text
1. Student Management
2. Bus Management
3. Route Management
4. Bus Allocation
5. Attendance
6. Reports
7. Exit
```

## Suggested First-Time Workflow

1. Add a few students.
2. Add one or more buses with capacities.
3. Add routes and stops.
4. Assign students to buses and routes.
5. Mark attendance.
6. Open Reports to view the stored information.

## Data Storage

The project stores information in JSON files inside the `data` folder.

The files are:

- `students.json`
- `buses.json`
- `routes.json`
- `allocations.json`
- `attendance.json`

The application creates/updates these files automatically.

## Testing

Run the unit tests from the project root:

```bash
python -m unittest discover -s tests -v
```

On Windows:

```bash
py -m unittest discover -s tests -v
```

## Error Handling

The application validates:
- Empty required fields
- Numeric IDs
- Positive bus capacities
- Duplicate student roll numbers
- Duplicate bus numbers
- Duplicate route names
- Missing students, buses, and routes
- Full buses
- Invalid attendance status
- Invalid JSON/data-file situations

## Limitations

This is a local command-line academic project. It does not provide:
- GPS/live bus tracking
- Online payments
- Login/authentication
- Web or mobile interface
- Cloud database

## Future Enhancements

Possible future improvements include:
- User login and role-based access
- SQLite database
- GPS/live bus tracking
- Online fee/payment records
- Web dashboard
- Automated notifications
- Exporting reports to CSV/PDF

## Student Details

- **Name:** Priyam Motwani
- **Registration Number:** 26BAI10012
- **Branch:** B.Tech - CSE(AI & ML)
- **Semester:** Fall Semester (2026-2027)

## Author

Priyam Motwani
