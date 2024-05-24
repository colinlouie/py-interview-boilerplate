import unittest

from interview.question import Question

class TestInterview(unittest.TestCase):

    def test_question(self):
        question = Question()
        self.assertEqual("hello", question.foo())

if __name__ == '__main__':
    unittest.main()
