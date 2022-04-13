import unittest
from python_katas.kata_1 import questions
from python_katas.utils import unittest_runner


class TestVerbing(unittest.TestCase):

    def test_2_chars(self):
        self.assertEqual(questions.verbing('do'), 'do')

    def test_ly_ending(self):
        self.assertEqual(questions.verbing('doing'), 'doingly')

    def test_ing_ending(self):
        self.assertEqual(questions.verbing('laugh'), 'laughing')

    def test_empty(self):
        self.assertEqual(questions.verbing(''), '')

class TestPairMatch(unittest.TestCase):

    def test_pair(self):
        men = {"John": 21, "Abraham": 44, "Ben": 34}
        women = {"July": 19, "Kim": 51, "Elinor": 48}
        self.assertEqual(questions.pair_match(men, women), ('John', 'July'))
