

from models.test_case import TestCase
from services.test_case_service import TestCaseService


class TestCaseMenuDialog:
    def __init__(self, service: TestCaseService):
        self.service = service

    def add_test_case_menu(self):
        print("\n### REGISTER TEST CASE ###")

        title = input("Title: ").strip()
        description = input("Description: ").strip()
        expected_result = input("Expected Result: ").strip()

        if not title or not description or not expected_result:
            print("All fields are required.")
            return

        test_case = TestCase(title, description, expected_result)
        self.service.add_test_case(test_case)

        print("Test case registered successfully.")

    def list_test_cases_menu(self):
        print("\n### REGISTERED TEST CASES ###")

        test_cases = self.service.get_test_cases()

        if not test_cases:
            print("No test cases have been registered.")
            return

        for number, test_case in enumerate(test_cases, start=1):
            print(f"\nTest Case {number}")
            print(f"Title: {test_case.title}")
            print(f"Description: {test_case.description}")
            print(f"Expected Result: {test_case.expected_result}")

    def show_menu(self):
        while True:
            print("\n### TEST CASE MANAGEMENT SYSTEM ###")
            print("1. Register Test Case")
            print("2. Display Test Cases")
            print("0. Exit")

            choice = input("Choose an option: ").strip()

            match choice:
                case "1":
                    self.add_test_case_menu()
                case "2":
                    self.list_test_cases_menu()
                case "0":
                    print("The application is closing.")
                    break
                case _:
                    print("Invalid choice. Please try again.")

