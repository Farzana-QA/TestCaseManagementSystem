
import unittest

from models.test_case import TestCase
from services.test_case_service import TestCaseService


class TestTestCaseService(unittest.TestCase):

    def setUp(self):
        self.service = TestCaseService()

    def test_service_starts_with_empty_list(self):
        self.assertEqual(self.service.get_test_cases(), [])

    def test_add_test_case(self):
        test_case = TestCase(
            "Login Test",
            "Enter valid username and password.",
            "User successfully logs in."
        )

        self.service.add_test_case(test_case)

        self.assertEqual(len(self.service.get_test_cases()), 1)

    def test_add_multiple_test_cases(self):
        test_case1 = TestCase(
            "Login Test",
            "Enter valid credentials.",
            "Login successful."
        )

        test_case2 = TestCase(
            "Logout Test",
            "Click the logout button.",
            "User is logged out."
        )

        self.service.add_test_case(test_case1)
        self.service.add_test_case(test_case2)

        self.assertEqual(len(self.service.get_test_cases()), 2)


if __name__ == "__main__":
    unittest.main()
