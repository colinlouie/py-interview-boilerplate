# Standard libraries.
import unittest

# Third-party libraries.
import pytest

# Internal libraries.
from interview.question import Question


class TestInterview(unittest.TestCase):

    def test_question(self):
        question = Question()
        self.assertEqual(str(3), question.foo())

    @pytest.mark.skip(reason="no need for database right now")
    def test_database_connection(self):
        question = Question()
        self.assertEqual(1, question.database_connection())


if __name__ == "__main__":
    unittest.main()
