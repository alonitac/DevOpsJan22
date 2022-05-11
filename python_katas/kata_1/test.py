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
        self.assertEqual(questions.verbing(test_word), "gamingly")

    def test_ing(self):
        test_word = 'ing'
        self.assertEqual(questions.verbing(test_word), "ingly")

    def test_in(self):
        test_word = 'cartin'
        self.assertEqual(questions.verbing(test_word), "cartining")


class TestWordsConcatenation(unittest.TestCase):
    """
    1 Katas
    """

    def test_daft_funk(self):
        lyrics=['one', 'more', 'time']
        self.assertEqual(questions.words_concatenation(lyrics), 'one more time')

    def test_bob_marley(self):
        lyrics=["don't", 'worry', 'about', 'a', 'thing,', 'cause', 'every', 'little', 'thing', 'is', 'gonna', 'be', 'alright']
        self.assertEqual(questions.words_concatenation(lyrics), "don't worry about a thing, cause every little thing is gonna be alright")

    def test_dolly_parton(self):
        lyrics=["working", "9", "to", "5"]
        self.assertEqual(questions.words_concatenation(lyrics), 'working 9 to 5')

    def test_queen(self):
        lyrics=['we', 'are', 'the', 'champions', 'my', 'friend']
        self.assertEqual(questions.words_concatenation(lyrics), 'we are the champions my friend')



class TestReverseWordsConcatenation(unittest.TestCase):
    """
    1 Katas
    """

    def test_reverse_original_example(self):
        lst = ['take', 'me', 'home']
        self.assertEqual(questions.reverse_words_concatenation(lst), "home me take")

    def test_reverse_empty_list(self):
        lst = []
        self.assertEqual(questions.reverse_words_concatenation(lst), "")

    def test_reverse_one_string(self):
        lst = ['me']
        self.assertEqual(questions.reverse_words_concatenation(lst), "me")

    def test_reverse_same_strings(self):
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




class TestListDiff(unittest.TestCase):
    """
    1 Katas
    """
    def test_sample(self):
        test_list = [1, 5, 0, 4, 1, 1, 1]
        expected = [None, 4, -5, 4, -3, 0, 0]
        result = questions.list_diff(test_list)
        self.assertEqual(result, expected)

    def test_empty(self):
        test_list = []
        expected = []
        self.assertEqual(questions.list_diff(test_list), expected)

    def test_one(self):
        test_list = [1]
        expected = [None]
        self.assertEqual(questions.list_diff(test_list), expected)

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
    def test_pal1True(self):
        num = 1441
        self.assertTrue(questions.palindrome_num(num), "the num is palindrome but you return False")

    def test_pal2True(self):
        num = 11
        self.assertTrue(questions.palindrome_num(num), "the num is palindrome but you return False")

    def test_pal1False(self):
        num = 113
        self.assertFalse(questions.palindrome_num(num),"the num is not palindrome but you return True")

    def test_pal1Zero(self):
        num = 0
        self.assertTrue(questions.palindrome_num(num)," 0 is palindrom num but you return False")


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

    def test_easy_peasy(self):
        self.assertEqual(questions.bad_average(10, 20, 30), 20)

    def test_zeros(self):
        self.assertEqual(questions.bad_average(0, 3, 0), 1)

    def test_fractions_in_answer(self):
        self.assertEqual(questions.bad_average(1, 1, 1), 1)

    def test_mistake(self):
        self.assertNotEqual(questions.bad_average(10, 20, 30), 30)


class TestBestStudent(unittest.TestCase):
    """
    1 Katas
    """

    def test_best_student_original_example(self):

        dict1 = {
            "Ben": 78,
            "Hen": 88,
            "Natan": 99,
            "Efraim": 65,
            "Rachel": 95
        }
        self.assertEqual(questions.best_student(dict1), 'Natan')

    def test_best_student_over_grades(self):
        dict1 = {
            "Ben": 178,
            "Hen": 188,
            "Natan": 299,
            "Efraim": 365,
            "Rachel": -95
        }
        self.assertEqual(questions.best_student(dict1), 'Efraim')

    def test_best_student_same_gardes(self):
        dict1 = {
            "Ben": 88,
            "Hen": 88,
            "Natan": 88,
            "Efraim": 88,
            "Rachel": 88
        }
        self.assertEqual(questions.best_student(dict1), 'Ben')

    def test_best_student_float_grades(self):
        dict1 = {
            "Ben": 7.5,
            "Hen": 8,
            "Natan": 9,
            "Efraim": 5.5,
            "Rachel": 9.1
        }
        self.assertEqual(questions.best_student(dict1), 'Rachel')


class TestPrintDictAsTable(unittest.TestCase):
    """
    1 Katas
    """


    def test_DictTable(self):
        resutls =''
        dict = {"Yuval": 23, "alex": 59}
        for key, value in dict.items():
            resutls += ("{:<10} {:<10}".format(key, value) + "\n")
        self.assertEqual(questions.print_dict_as_table(dict), resutls)



class TestMergeDicts(unittest.TestCase):
    """
    1 Katas
    """

    def test_basic(self):
        dict1 = {'a': 5, 'b': 2}
        dict2 = {'c': 5, 'd': 2}

        expected_dict = {'a': 5, 'b': 2, 'c': 5, 'd': 2}
        result = questions.merge_dicts(dict1, dict2)
        self.assertEqual(result, expected_dict)

    def test_one_empty(self):
        dict1 = {'a': 5, 'b': 2}
        dict2 = {}

        expected_dict = {'a': 5, 'b': 2}

        self.assertEqual(questions.merge_dicts(dict1, dict2), expected_dict)

    def test_both_empty(self):
        dict1 = {}
        dict2 = {}

        expected_dict = {}

        self.assertEqual(questions.merge_dicts(dict1, dict2), expected_dict)

    def test_common_key(self):
        dict1 = {'a': 5, 'b': 2}
        dict2 = {'a': 7, 'd': 2}

        expected_dict = {'a': 7, 'b': 2, 'd': 2}

        self.assertEqual(questions.merge_dicts(dict1, dict2), expected_dict)

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

    def test_1(self):
        string = "hey my friend"
        self.assertEqual(questions.caesar_cipher(string), "khb pb iulhqg")

    def test_2(self):
        string = "Learn python code"
        self.assertEqual(questions.caesar_cipher(string), "Ohduq sbwkrq frgh")

    def test_3(self):
        string = "Fly Me To The Moon"
        self.assertEqual(questions.caesar_cipher(string), "Iob Ph Wr Wkh Prrq")


class TestSumOfDigits(unittest.TestCase):
    """
    1 Katas
    """

    def test_1(self):
        num = "546312"
        self.assertEqual(questions.sum_of_digits(num), 21)
    def test_2(self):
        num = "123456789"
        self.assertEqual(questions.sum_of_digits(num), 45)


if __name__ == '__main__':
    import inspect
    import sys
    unittest_runner(inspect.getmembers(sys.modules[__name__], inspect.isclass))
