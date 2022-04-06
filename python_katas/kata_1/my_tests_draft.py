import unittest
from python_katas.kata_1 import questions
from python_katas.utils import unittest_runner

    def test_2_chars(self):
        self.assertEqual(questions.verbing('by'), 'by')

    def test_ing_ending(self):
        self.assertEqual(questions.verbing('by'), 'by')

    def test_some_word(self):
        self.assertEqual(questions.verbing('by'), 'by')