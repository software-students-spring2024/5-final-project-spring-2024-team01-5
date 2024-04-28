# pylint: disable=missing-final-newline,missing-module-docstring,import-error
import pytest
from functions import *

class Tests:
    """
    This class contains test cases for the functions.
    """

    @staticmethod
    def test_sanity_check():
        """
        Test case to check the sanity of the testing framework.
        """
        expected = True
        actual = True
        assert actual == expected


    def test_calculate_GPA_empty(self):
        assert calculate_GPA([]) == 0

    def test_calculate_GPA_single_course(self):
        assert calculate_GPA([['A', '4']]) == 4.0

    def test_calculate_GPA_multiple_courses(self):
        courses = [['A', '4'], ['B', '2'], ['B-', '4']]
        expected_gpa = (4.0*4 + 3.0*2 + 2.7*4) / 10
        assert round(calculate_GPA(courses), 3) == expected_gpa

    def test_calculate_final_exam_grade(self):
        assert calculate_final_exam_grade(75, 30, 80) == pytest.approx(91.6667, 0.1)

    def test_calculate_final_exam_grade_exact_target(self):
        assert calculate_final_exam_grade(80, 30, 80) == pytest.approx(80, 0.1)


