import unittest
from python_katas.kata_1 import questions
from python_katas.utils import unittest_runner


testers = ['dorondollev',
           'danielbar0101',
           'DustyMadDude',
           'Amitpoz',
           'netanalm',
           'AlexeyMihaylovDev',
           'xXxARLxXx']


class TestSumOfElements(unittest.TestCase):
    """
    1 Katas
    """

    def sum_of_element(elements):
        return sum(elements)

    def test_empty_list(self):
        lst = []
        self.assertEqual(questions.sum_of_element(lst), 0)


    def test_integers_list(self):
        lst = [1, 2, 3, 4, 5]
        self.assertEqual(questions.sum_of_element(lst), 15)

    def test_negative_numbers(self):
        lst = [1, -6, 7, 0, 99]
        self.assertEqual(questions.sum_of_element(lst), 101)

    def test_all_zeros(self):
        lst = [0] * 50000
        self.assertEqual(questions.sum_of_element(lst), 0)


class TestVerbing(unittest.TestCase):
    """
    1 Katas
    """

    def test_sample(self):
        # your code here
        pass


class TestWordsConcatenation(unittest.TestCase):
    """
    1 Katas
    """

    def test_sample(self):
        # your code here
        pass


class TestReverseWordsConcatenation(unittest.TestCase):
    """
    1 Katas
    """

    def reverse_original_example(self):
        lst = ['take', 'me', 'home']
        self.assertEqual(questions.reverse_words_concatenation(lst), 0)

    def reverse_empty_list(self):
        lst = []
        self.assertEqual(questions.reverse_words_concatenation(lst), 0)

    def reverse_one_string(self):
        lst = ['me']
        self.assertEqual(questions.reverse_words_concatenation(lst), 0)

    def reverse_same_strings(self):
        lst = ['me', 'me', 'me']
        self.assertEqual(questions.reverse_words_concatenation(lst), 0)


class TestIsUniqueString(unittest.TestCase):
    """
    2 Katas
    """

    def test_sample(self):
        # your code here
        pass


class TestListDiff(unittest.TestCase):
    """
    1 Katas
    """




class TestPrimeNumber(unittest.TestCase):
    """
    1 Katas
    """

    def test_prime_1(self):
        number = 7
        self.assertEqual(questions.prime_number(number), True)

    def test_prime_2(self):
        number = 17
        self.assertEqual(questions.prime_number(number), True)

    def test_prime_3(self):
        number = 13
        self.assertEqual(questions.prime_number(number), True)

    def test_not_prime_1(self):
        number = 1
        self.assertEqual(questions.prime_number(number), False)

    def test_not_prime_2(self):
        number = -20
        self.assertEqual(questions.prime_number(number), False)

    def test_not_prime_3(self):
        number = 2.4
        self.assertEqual(questions.prime_number(number), False)


class TestPalindromeNum(unittest.TestCase):
    """
    1 Katas
    """

    def test_sample(self):
        # your code here
        pass


class TestPairMatch(unittest.TestCase):
    """
    3 Katas
    """

    def test_sample(self):
        # your code here
        pass


class TestBadAverage(unittest.TestCase):
    """
    1 Katas
    """

    def test_sample(self):
        # your code here
        pass


class TestBestStudent(unittest.TestCase):
    """
    1 Katas
    """

    def best_student_original_example(self):

        dict1 = {
            "Ben": 78,
            "Hen": 88,
            "Natan": 99,
            "Efraim": 65,
            "Rachel": 95
        }
        self.assertEqual(questions.best_student(lst), 0)

    def best_student_over_grades(self):
        dict1 = {
            "Ben": 178,
            "Hen": 188,
            "Natan": 299,
            "Efraim": 365,
            "Rachel": -95
        }
        self.assertEqual(questions.best_student(lst), 0)

    def best_student_same_gardes(self):
        dict1 = {
            "Ben": 88,
            "Hen": 88,
            "Natan": 88,
            "Efraim": 88,
            "Rachel": 88
        }
        self.assertEqual(questions.best_student(lst), 0)

    def best_student_float_grades(self):
        dict1 = {
            "Ben": 7.5,
            "Hen": 8,
            "Natan": 9,
            "Efraim": 5.5,
            "Rachel": 9.1
        }
        self.assertEqual(questions.best_student(lst), 0)


class TestPrintDictAsTable(unittest.TestCase):
    """
    1 Katas
    """


class TestMergeDicts(unittest.TestCase):
    """
    1 Katas
    """

    def test_sample(self):
        # your code here
        pass


class TestSevenBoom(unittest.TestCase):
    """
    1 Katas
    """

    def test_if_contains_7(self):
        n = 7
        self.assertEqual(questions.seven_boom(n), [7])

    def test_if_modulo_7(self):
        n = 30
        self.assertEqual(questions.seven_boom(n), [7, 14, 17, 21, 27, 28])

class TestCaesarCipher(unittest.TestCase):
    """
    1 Katas
    """

    def test_sample(self):
        # your code here
        pass


class TestSumOfDigits(unittest.TestCase):
    """
    1 Katas
    """

    def test_sample(self):
        # your code here
        pass


if __name__ == '__main__':
    import inspect
    import sys
    unittest_runner(inspect.getmembers(sys.modules[__name__], inspect.isclass))
