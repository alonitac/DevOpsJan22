from python_katas.kata_3.utils import open_img, save_img
import requests   # to be used in simple_http_request()


def knapsack(items, knapsack_limit=50):
    """
    5 Kata

    Consider a thief gets into a home to rob and he carries a knapsack.
    There are fixed number of items in the home — each with its own weight and value —
    Jewelry, with less weight and highest value vs tables, with less value but a lot heavy.
    To add fuel to the fire, the thief has an old knapsack which has limited capacity.
    Obviously, he can’t split the table into half or jewelry into 3/4ths. He either takes it or leaves it

    Given a set of items, dict of tuples representing the (weight, value), determine the items to include in a collection
    so that the total weight is less than or equal to a given limit and the total value is as large as possible.

    :param items: dict of tuples e.g. {"bed": (100, 15), "iphone13": (1, 1500)}
    :param knapsack_limit:
    :return: set of items
    """
    pass


def time_me(func):
    """
    2 Kata

    Given func - a pointer to sime function which can be executed by func()
    Return the number of time it took to execute the function. Since execution time may vary from time to time,
    execute func 100 time and return the mean

    :param func:
    :return:
    """
    pass


def youtube_download(video_id):
    """
    3 Kata

    Youtube video url is in the form https://www.youtube.com/watch?v=<video id>
    This function get a youtube video id and downloads this video to the local fs

    hint: https://www.bogotobogo.com/VideoStreaming/YouTube/youtube-dl-embedding.php

    :param video_id: str
    :return: None
    """
    from youtube_dl import YoutubeDL

    pass


def tasks_scheduling(tasks):
    """
    5 Kata

    Consider a list of n tasks (tuples), each has starting and ending time (datetime object), as following:
    [(s_1, e_1), (s_2, e_2), ..., (s_n, e_n)]
    where s_* and e_* are Python datetime objects

    Only one task can be performed every time.
    This function returns the index of tasks to perform such the total completed tasks is as large as possible

    :param: tasks: list of tuple (start, end) while start and end are datetime objects
    :return: list of tasks indexes to perform
    """
    pass


def valid_dag(edges):
    """
    5 Kata

    Given a DAG (https://en.wikipedia.org/wiki/Directed_acyclic_graph) in the form:
    [('a', 'b'), ('a', 'c'), ('a', 'd'), ('a', 'e'), ('b', 'd'), ('c', 'd'), ('c', 'e')]

    where a, b, c, d, e are vertices and ('a', 'b') etc... are edges
    This function determine whether the graph is a valid DAG

    :param edges: list of tuples of string 'a', 'b'....
    :return: bool - True if and only if it is a valid DAG
    """
    pass


def rotate_img(img_filename):
    """
    3 Kata

    Rotates image clockwise

    :param img_filename: image file path (png or jpeg)
    :return: None, the rotated image should be saved as 'rotated_<original image filename>'
    """
    image = open_img(img_filename)

    pass  # use rotate_matrix from previous kata 2 or implement....

    save_img(rotated_img, f'rotated_{img_filename}')


def img_blur(img_filename):
    """
    4 Kata

    Blurs an image (every pixel is an average of its nearest neighbors)

    :param img_filename: image file path (png or jpeg)
    :return: None, the rotated image should be saved as 'rotated_<original image filename>'
    """
    image = open_img(img_filename)

    pass  # use matrix_avg from previous kata 2 or implement....

    save_img(blured_img, f'blured_{img_filename}')


def apache_logs_parser(apache_single_log):
    """
    3 Kata

    Parses apache log (see format here https://httpd.apache.org/docs/2.4/logs.html)
    e.g.
    [Fri Sep 09 10:42:29.902022 2011] [core:error] [pid 35708:tid 4328636416] [client 72.15.99.187] File does not exist: /usr/local/apache2/htdocs/favicon.ico

    the parsed log data should be:
    date (datetime object), level (str), pid (int), thread_id (int), client_ip (str), log (str)

    Hint: use regex

    :param apache_single_log: str
    :return: parsed log data as tuple
    """
    return date, level, pid, tid, client_ip, log


def simple_http_request():
    """
    2 Kata

    This function returns Binance market data JSON by performing a simple HTTP request to '/api/v3/exchangeInfo' endpoint

    Hint: use requests.get(...)
    Hint: Binance api docs https://binance-docs.github.io/apidocs/spot/en/#market-data-endpoints

    :return: json of market exchange information
    """
    pass


class SortedDict(dict):
    """
    8 Kata

    Implement SortedDict class which is a regular Python dictionary,
    but the keys are maintained in sorted order

    Usage example:
    x = SortedDict()

    x['banana'] = 'ccc'
    x['apple'] = 'aaa'
    x['orange'] = 'bbb'

    list(x.keys())
    >> ['apple', 'banana', 'orange']

    list(x.values())
    >> ['aaa', 'ccc', 'bbb']

    list(x.items())
    >> [('apple', 'aaa'), ('banana', 'ccc'), ('orange', 'bbb')]
    """

    def __init__(self):
        super().__init__()
        pass

    def __setattr__(self, key, value):
        pass

    def items(self):
        raise NotImplemented()

    def values(self):
        raise NotImplemented()

    def keys(self):
        raise NotImplemented()


class CacheList(list):
    """
    8 Kata

    Implement CacheList class which is a regular Python list,
    but it holds the last n elements only (old elements will be deleted)

    Usage example:
    x = CacheList(3)

    x.append(1)
    x.append(2)
    x.append(3)

    print(x)
    >> [1, 2, 3]

    x.append(1)
    print(x)
    >> [2, 3, 1]

    x.append(1)
    print(x)
    >> [3, 1, 1]
    """
    def __init__(self, cache_size=5):
        super().__init__()
        pass

    def append(self, element):
        pass

