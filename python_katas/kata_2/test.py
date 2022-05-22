import unittest
from python_katas.kata_2 import questions
from python_katas.utils import unittest_runner


testers = ['elkan316',
           'JohnSchiff',
           'Haimr101',
           'danielmalka14',
           'Gershoz',
           'Ddady1',
           'yosefdudi',
           'kostalubarsky']


# elkan316
class TestValidParentheses(unittest.TestCase):
    """
    3 Katas
    """

    def test_sample(self):
        # your code here
        pass


# Haimr101
class TestFibonacciFixme(unittest.TestCase):
    """
    2 Katas
    """

    def test_fib(self):
        self.assertEqual(questions.fibonacci_fixme(5), 5)
        self.assertEqual(questions.fibonacci_fixme(6), 8)


# JohnSchiff
class TestMostFrequentName(unittest.TestCase):
    """
    2 Katas
    """

    def test_sample(self):
        self.assertEqual(questions.most_frequent_name('test_names.txt'), 'c')


# danielmalka14
class TestFilesBackup(unittest.TestCase):
    """
    3 Katas
    """

    def test_sample(self):
        # your code here
        pass


# Gershoz
class TestReplaceInFile(unittest.TestCase):
    """
    2 Katas
    """

    def test_sample(self):
        # your code here
        pass


# Ddady1
class TestJsonConfigsMerge(unittest.TestCase):
    """
    2 Katas
    """

    def test_jason_files(self):
        paths = ('local.jason', 'default.jason')
        self.assertEqual(questions.json_configs_merge('jpg.json', 'student.json'), {
            "id": "0001",
            "type": "donut",
            "name": "Cake",
            "image":
                {
                    "url": "images/0001.jpg",
                    "width": 200,
                    "height": 200
                },
            "thumbnail":
                {
                    "url": "images/thumbnails/0001.jpg",
                    "width": 32,
                    "height": 32
                },
        },
        {
            "student": [

                {
                    "id": "01",
                    "name": "Tom",
                    "lastname": "Price"
                },

                {
                    "id": "02",
                    "name": "Nick",
                    "lastname": "Thameson"
                }
                       ]
        }

                         )


# yosefdudi
class TestMonotonicArray(unittest.TestCase):
    """
    1 Katas
    """

    def test_sample(self):
        # your code here
        pass


# kostalubarsky
class TestMatrixAvg(unittest.TestCase):
    """
    2 Katas
    """

    def test_sample(self):
        # your code here
        pass


# elkan316
class TestMergeSortedLists(unittest.TestCase):
    """
    1 Katas
    """

    def test_sample(self):
        # your code here
        pass


# Haimr101
class TestLongestCommonSubstring(unittest.TestCase):
    """
    4 Katas
    """

    def test_sample(self):
        # your code here
        pass


# JohnSchiff
class TestLongestCommonPrefix(unittest.TestCase):
    """
    1 Katas
    """

    def test_sample(self):
        # your code here
        pass


# danielmalka14
class TestRotateMatrix(unittest.TestCase):
    """
    2 Katas
    """

    def test_sample(self):
        # your code here
        pass


# Gershoz
class TestIsValidEmail(unittest.TestCase):
    """
    3 Katas
    """

    def test_sample(self):
            self.assertEqual(questions.str_compression(''), '')
            self.assertEqual(questions.str_compression('AABBCC'), 'A2B2C2')
            self.assertEqual(questions.str_compression('AAABCCDDDDD'), 'A3B1C2D5')
            # your code here
            pass


# Ddady1
class TestPascalTriangle(unittest.TestCase):
    """
    3 Katas
    """

    def test_sample(self):
        # your code here
        pass


# yosefdudi
class TestListFlatten(unittest.TestCase):
    """
    2 Katas
    """

    def test_sample(self):
        # your code here
        pass


# kostalubarsky
class TestStrCompression(unittest.TestCase):
    """
    2 Katas
    """

    def test_sample(self):
            self.assertEqual(questions.str_compression(''), '')
            self.assertEqual(questions.str_compression('AABBCC'), ['A',2,'B',2,'C',2])
            self.assertEqual(questions.str_compression('AAABCCDDDDD'), ['A',3,'B',1,'C',2,'D',5])
            # your code here
            pass




# Haimr101
class TestStrongPass(unittest.TestCase):
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
