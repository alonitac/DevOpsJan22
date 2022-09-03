import re

from python_katas.kata_3.utils import open_img, save_img
import requests   # to be used in simple_http_request()

ISO_FORMAT = '%Y-%m-%dT%H:%M:%SZ'


def knapsack(items, knapsack_limit=50):
    l = {}
    marklist = sorted(items.items(), key=lambda x:x[0] )
    sortdict = dict(marklist)
    count=0
    sds=int(knapsack_limit)
    for key,value in sortdict,items():
        count += value[0]

        if count <= sds:
            l.update({key:value})
        if count > knapsack_limit:
            break
    print(l)


def time_me(func):
    """
    2 Kata

    Given func - a pointer to sime function which can be executed by func()
    Return the number of time it took to execute the function. Since execution time may vary from time to time,
    execute func 100 time and return the mean

    :param func:
    :return:
    """
    return None


def youtube_download(video_id):
    import youtube_dl
    def youtube_download(video_id):
        ydl_opts = {}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([f'https://www.youtube.com/watch?v={video_id}'])

from datetime import datetime, timedelta
ISO_FORMAT = '%Y-%M-%DT%H:%M:%$Z'
def tasks_scheduling(tasks):
    start=datetime.now()
    end=start + timedelta(minutes=5)
    endf=datetime.now()

    for s in tasks:
        start +=timedelta(minutes=5)
        end +=timedelta(minutes=+ 5)
        print(start,s,end)

tasks_scheduling(['task1 ' , 'task2 2 ', 'task3 ', 'task 4 '])


import networkx as nx
def valid_dag(edges):
    g = nx.DiGraph()
    g.add_edges_from(edges)
    res=nx.is_directed_acyclic_graph(g)
    return res

print(valid_dag([('a' , 'b'), ('a' , 'c'), ('a' , 'd'), ('a' , 'e'), ('b' , 'd'), ('c' , 'd'), ('c' , 'e')]))

from PIL import Image, ImageFilter

def rotate_img(img_filename):
    def rotate_img(img_filename):
        imageObject = Image.open(rf"/home/ami-porat/Pictures{img_filename}")
        degree_flippedImage = imageObject.transpose(Image.ROTATE_90)
        degree_flippedImage.save(rf"/home/ami-porat/Pictures/rotated_{img_filename}")
        rotate_img("dog.png")


def img_blur(img_filename):
    def img_blur(img_filename):
        imageObject = Image.open(rf"/home/ami-porat/Pictures{img_filename}.png")
        blurImage = imageObject.filter(ImageFilter.BoxBlur(15))
        blurImage.save(rf"/home/ami-porat/Pictures{img_filename}_blur.png")
        img_blur('dog')
    image = open_img(img_filename)


def apache_logs_parser(apache_single_log):
    regex = '([(\d\.)]+) - - \[(.*?)\] "(.*?)" (\d+) - "(.*?)" "(.*?)"'
    print(re.Match(regex,apache_single_log).groups())
    date, level, pid, tid, client_ip, log = ..., ..., ..., ..., ..., ...
    return date, level, pid, tid, client_ip, log

apache_logs_parser('172.16.8.3 - - ')

import requests as requests
def simple_http_request():
    def simple_http_request():
        x = "https://api.binance.com/api/v3/exchangeInfo"
        data=requests.get(x)
        det=data.json()
        print(det)


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


if __name__ == '__main__':
    import time
    from random import random
    from datetime import datetime

    print('\nknapsack\n--------------------')
    res = knapsack({
        'book': (3, 2),
        'television': (4, 3),
        'table': (6, 1),
        'scooter': (5, 4)
    }, knapsack_limit=8)
    print(res)

    print('\ntime_me\n--------------------')
    time_took = time_me(lambda: time.sleep(5 + random()))
    print(time_took)

    print('\nyoutube_download\n--------------------')
    youtube_download('Urdlvw0SSEc')

    print('\ntasks_scheduling\n--------------------')
    tasks = tasks_scheduling([
        (datetime.strptime('2022-01-01T13:00:00Z', ISO_FORMAT), datetime.strptime('2022-01-01T14:00:00Z', ISO_FORMAT)),
        (datetime.strptime('2022-01-01T13:00:00Z', ISO_FORMAT), datetime.strptime('2022-01-01T14:30:00Z', ISO_FORMAT)),
        (datetime.strptime('2022-01-01T11:00:00Z', ISO_FORMAT), datetime.strptime('2022-01-01T16:00:00Z', ISO_FORMAT)),
        (datetime.strptime('2022-01-01T14:00:00Z', ISO_FORMAT), datetime.strptime('2022-01-01T14:05:00Z', ISO_FORMAT)),
        (datetime.strptime('2022-01-01T12:00:00Z', ISO_FORMAT), datetime.strptime('2022-01-01T13:30:00Z', ISO_FORMAT)),
        (datetime.strptime('2022-01-01T10:00:00Z', ISO_FORMAT), datetime.strptime('2022-01-01T10:10:00Z', ISO_FORMAT))
    ])
    print(tasks)

    print('\nvalid_dag\n--------------------')

    # valid
    print(valid_dag([('a', 'b'), ('a', 'c'), ('a', 'd'), ('a', 'e'), ('b', 'd'), ('c', 'd'), ('c', 'e')]))

    # invalid
    print(valid_dag([('a', 'b'), ('c', 'a'), ('a', 'd'), ('a', 'e'), ('b', 'd'), ('c', 'd'), ('c', 'e')]))

    print('\nrotate_img\n--------------------')
    rotate_img('67203.jpeg')

    print('\nimg_blur\n--------------------')
    img_blur('67203.jpeg')

    print('\napache_logs_parser\n--------------------')
    date, level, pid, tid, client_ip, log = apache_logs_parser('[Fri Sep 09 10:42:29.902022 2011] [core:error] [pid 35708:tid 4328636416] [client 72.15.99.187] File does not exist: /usr/local/apache2/htdocs/favicon.ico')
    print(date, level, pid, tid, client_ip, log)

    print('\nsimple_http_request\n--------------------')
    info = simple_http_request()

    print('\nSortedDict\n--------------------')
    s_dict = SortedDict()
    s_dict['a'] = None
    s_dict['t'] = None
    s_dict['h'] = None
    s_dict['q'] = None
    s_dict['b'] = None
    print(s_dict.items())

    print('\nCacheList\n--------------------')
    c_list = CacheList(5)
    c_list.append(1)
    c_list.append(2)
    c_list.append(3)
    c_list.append(4)
    c_list.append(5)
    c_list.append(6)
    print(c_list)
