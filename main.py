
from services.test_case_service import TestCaseService
from dialogs.test_case_menu_dialog import TestCaseMenuDialog


def main():
    test_case_service = TestCaseService()

    test_case_menu_dialog = TestCaseMenuDialog(test_case_service)

    test_case_menu_dialog.show_menu()


if __name__ == "__main__":
    main()
