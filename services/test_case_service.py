
from models.test_case import TestCase


class TestCaseService:
    def __init__(self):
        self.test_cases: list[TestCase] = []

    def add_test_case(self, test_case: TestCase):
        self.test_cases.append(test_case)

    def get_test_cases(self) -> list[TestCase]:
        return self.test_cases.copy()
