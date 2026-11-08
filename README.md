# Test Case Management System

## 1. Project Description

The Test Case Management System is a simple Python console application.

The application allows users to register test cases and display all registered test cases.

Each test case contains three fields:
- Title
- Description
- Expected Result

The application uses an in-memory list to store test cases while the program is running. No database is used.

## 2. Features

The application provides the following features:

- Register a new test case.
- Display all registered test cases.
- Validate that all fields are entered.
- Navigate through a menu.
- Exit the application.

## 3. Project Structure

```text
TestCaseManagementSystem/
│
├── models/
│   └── test_case.py
│
├── services/
│   └── test_case_service.py
│
├── dialogs/
│   └── test_case_menu_dialog.py
│
├── tests/
│   └── test_test_case_service.py
│
├── diagrams/
│   ├── class_diagram.puml
│   ├── activity_diagram.puml
│   └── sequence_diagram.puml
│
├── main.py
└── README.md
```

## 4. How to Run the Application

Make sure Python is installed.

Open a terminal in the project folder and run:

```bash
python main.py
```

The application displays a menu with three options:

1. Register Test Case
2. Display Test Cases
0. Exit

## 5. How to Run Unit Tests

The project uses Python's built-in unittest framework.

Open a terminal in the project folder and run:

```bash
python -m unittest discover -s tests -v
```

The tests check that:
- The service starts with an empty list.
- A test case can be added.
- Multiple test cases can be stored.

## 6. Design Reflection

The application is divided into separate classes with different responsibilities.

**TestCase**

Represents one test case and contains its title, description and expected result.

**TestCaseService**

Manages the test cases. It handles adding and retrieving test cases.

**TestCaseMenuDialog**

Handles user interaction, menu options and input.

**main.py**

Starts the application and connects the service with the menu dialog.

This structure makes the application easier to understand, maintain and test.

The service is separated from the user interface, which makes it possible to test the central functionality independently.

The application uses an in-memory list, so registered test cases are only available while the application is running. The data is not saved permanently.

## 7. UML Diagrams

The project includes three UML diagrams:

- Class Diagram – shows the classes and their relationships.
- Activity Diagram – shows the application's workflow.
- Sequence Diagram – shows how the user and application components interact.

The diagrams describe the design of the application and support the implementation.
