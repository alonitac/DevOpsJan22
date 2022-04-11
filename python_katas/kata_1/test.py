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
    """
    1 Katas
    """

    def daft_funk(self):
        lyrics=['one', 'more', 'time']
        self.assertEqual(questions.words_concatenation(lyrics), 'one more time')

    def bob_marley(self):
        lyrics=["don't", 'worry', 'about', 'a', 'thing,', 'cause', 'every', 'little', 'thing', 'is', 'gonna', 'be', 'allright']
        self.assertEqual(questions.words_concatenation(lyrics), "don't worry about a thing, cause every little thing is gonna be alright")

    def dolly_parton(self):
        lyrics=["working", "9", "to", "5"]
        self.assertEqual(questions.words_concatenation(lyrics), 'working 9 to 5')

    def queen(self):
        lyrics=['we', 'are', 'the', 'champions', 'my', 'friend']
        self.assertEqual(questions.words_concatenation(lyrics), 'we are the champions my friend')

        pass


class TestReverseWordsConcatenation(unittest.TestCase):
    """
    1 Katas
    """

    def reverse_original_example(self):
        lst = ['take', 'me', 'home']
        self.assertEqual(questions.reverse_words_concatenation(lst), "home me take")

    def reverse_empty_list(self):
        lst = []
        self.assertEqual(questions.reverse_words_concatenation(lst), "")

    def reverse_one_string(self):
        lst = ['me']
        self.assertEqual(questions.reverse_words_concatenation(lst), "me")

    def reverse_same_strings(self):
        lst = ['me', 'me', 'me']
        self.assertEqual(questions.reverse_words_concatenation(lst), "me me me")

class TestIsUniqueString(unittest.TestCase):
    """
    2 Katas
    """

    def test_sample(self):
        some_str = ('MynameIsmMax')
        self.assertEqual(questions.is_unique_string(some_str), False)
        some_str = ('aNuke')
        self.assertEqual(questions.is_unique_string(some_str), True)
        some_str = ('IAmDeath')
        self.assertEqual(questions.is_unique_string(some_str), True)
        pass



class TestListDiff(unittest.TestCase):
    """
    1 Katas
    """
    def test_sample(self):
        def list_diff(elements):
            ret = []
            for i in elements:
                if len(ret) == 0:
                    ret.append(None)
                    prev = i
                else:
                    ret.append(i - prev)
                    prev = i
            return ret

        print(list_diff([1, 8, 9, 20, 5]))
        [None, 1, 1, 3, 4]
        print(list_diff([1, 5, 0, 4, 1, 1, 1]))
        [None, 4, -5, 4, -3, 0, 0]
        pass

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

    def easy_peasy(self):
        nums = [10, 20, 30]
        self.assertEqual(questions.bad_average(nums), 20)

    def fractions(self):
        nums = [0.5, 2, 9.5]
        self.assertEqual(questions.bad_average(nums), 4)

    def zeros(self):
        nums = [0, 3, 0]
        self.assertEqual(questions.bad_average(nums), 1)

    def fractions_in_answer(self):
        nums = [1, 1, 1]
        self.assertEqual(questions.bad_average(nums), 1/3)

    def mistake(self):
        nums = [10, 20, 30]
        self.assertEqual(questions.bad_average(nums), 30)

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

    def test_sample(self):
        dict = {"Yuval": 23, "alex": 59}
        self.assertEqual(questions.print_dict_as_table(dict) ,"")
        dict = {"i Am ": "Death" }
        self.assertEqual(questions.print_dict_as_table(dict) ,"")
        dict = {"Hello ": "World" }
        self.assertEqual(questions.print_dict_as_table(dict) ,"")
        pass


class TestMergeDicts(unittest.TestCase):
    """
    1 Katas
    """

    def test_sample(self):
        def Merge(dict2, dict1):
            return (dict1.update(dict2))

        dict1 = {1, 2, 3, 4}
        dict2 = {5, 6, 7, 8}

        print(Merge(dict2, dict1))

        print(dict1)
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
