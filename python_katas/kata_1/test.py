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

    def test_two_char(self):
        test_word = 'mu'
        self.assertEqual(questions.verbing(test_word), "mu")

    def test_gaming(self):
        test_word = 'gaming'
        self.assertEqual(questions.verbing(test_word), "gamly")

    def test_ing(self):
        test_word = 'ing'
        self.assertEqual(questions.verbing(test_word), "ly")

    def test_in(self):
        test_word = 'cartin'
        self.assertEqual(questions.verbing(test_word), "cartining")


class TestWordsConcatenation(unittest.TestCase):
    def test1(self):
        l = ["let's", "play", "game"]
        self.assertEqual(questions.words_concatenation(l), "let's play game")

    def test2(self):
        l = ["I", "am", "a", "student", "in", "INT", "College"]
        self.assertEqual(questions.words_concatenation(l), "I am a student in INT College")

    def test3(self):
        l = ["My", "Car", "", "is", "skoda"]
        self.assertEqual(questions.words_concatenation(l), "My Car  is skoda")

    """
    1 Katas
    """


class TestReverseWordsConcatenation(unittest.TestCase):

    def test_play(self):
        l = ["let's", "play", "game"]
        self.assertEqual(questions.reverse_words_concatenation(l), "game play let's")

    def test_student(self):
        l = ["I", "am", "a", "student", "in", "INT", "College"]
        self.assertEqual(questions.reverse_words_concatenation(l), "College INT in student a am I")

    def test_skoda(self):
        l = ["My", "Car", "", "is", "skoda"]
        self.assertEqual(questions.reverse_words_concatenation(l), "skoda is  Car My")

    """
    1 Katas
    """


class TestIsUniqueString(unittest.TestCase):
    """
    2 Katas
    """

    def test_unic1(self):
        string = "asdqwezxc"
        self.assertTrue(questions.is_unique_string(string), "is unique string")

    def test_unic2(self):
        string = "aaasasssdqwezxc"
        self.assertFalse(questions.is_unique_string(string), "string is not unique")

    def test_unic3(self):
        string = ""
        self.assertTrue(questions.is_unique_string(string), "empty string")


class TestListDiff(unittest.TestCase):
    """
    1 Katas
    """

    def test_sample(self):
        l = [1, 2, 3, 4, 7, 11]
        self.assertEqual(questions.list_diff(l), [None, 1, 1, 1, 3, 4])


class TestPrimeNumber(unittest.TestCase):
    """
    1 Katas
    """

    def test_sample(self):
        # your code here
        pass


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

    def test_Pair1(self):
        men = {'Ben': 34, 'Ronaldo': 37, 'Ancelotti': 62}
        women = {'Yasmin': 22, 'Inbar': 18, 'Angelina': 52}
        self.assertEqual(questions.pair_match(men, women), ('Ancelotti', 'Angelina'))

    def test_Pair2(self):
        men = {'Roi': 65, 'Eran': 82, 'Ido': 20}
        women = {'Sivan': 70, 'Orly': 18, 'Neta': 65}
        self.assertEqual(questions.pair_match(men, women), ('Roi', 'Neta'))


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

    def test_sample(self):
        # your code here
        pass


class TestPrintDictAsTable(unittest.TestCase):
    """
    1 Katas
    """

    def test_sample(self):
        # your code here
        pass


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

    def test_sample(self):
        # your code here
        pass


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
