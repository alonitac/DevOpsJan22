import tarfile
from importlib.resources import path


def valid_parentheses(s):
    stack = []
    for char in s:
      if not stack:
          continue
      if char in '([{':
          stack.append(char)
      elif not stack:
          top = stack.pop(-1)
          if top == "(" and char != ")":
              return False
          if top == "[" and char != "]":
              return False
          if top == "{" and char != "}":
              return False
          else:
              return False
    return True

    # count=0
    # ans = False
    # for i in s:
    #     if i == "(" or i == "{" or i == "[":
    #         count += 1
    #     elif i == ")" or i == "}" or i == "]":
    #         count -= 1
    #     if count < 1:
    #         return ans
    # if count == 0:
    #     return not ans
    # return ans


def fibonacci_fixme(n):
    nterms = n
    n1, n2 = 1, 1
    count = 0
    print("Fibonacci sequence")
    while count < nterms+1:
            print(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1


count = {}
file_path = "/home/ami.txt"
def most_frequent_name(file_path):
    f = open(file_path,"r")
    for n in f:
        if not n in count:
            count[n] = 1
        else:
            count[n] +=1
    maxval = max(count, key=count.get)
    f.close()
    return print(maxval)

from os import path
import datetime
import tarfile


dir_path = "/home/ami-porat"
date=datetime.date.today()
date=date.strftime("%d-%m-%y")
def files_backup(dir_path):
    new_name=dir_path.split(r"/")
    new_name=new_name[1]
    file = f"backup_{new_name}_{date}"
    tar = tarfile.TarFile.gzopen(f"{file}.gz" , mode="w", compresslevel=9)
    tar.add(dir_path, arcname="project1")
    tar.close()

from pathlib import Path
import re
file_path = input('HI , type a file path : ')
x = Path(file_path)
if x.is_file():
    file_path = x
else:
    print('file not found')
    exit(1)
text = input('what text you wont to replace ? : ')
replace_text = input ('what do you to replace it with ? : ')

def replace_in_file(file_path, text, replace_text):
    data=x.read_text()
    data=data.replace(text,replace_text)
    x.write_text(data)
    return None
replace_in_file(file_path, text, replace_text)


def json_configs_merge(*json_paths):
    """
    2 Kata

    This function gets an unknown number of paths to json files (represented as tuple in json_paths argument)
    it reads the files content as a dictionary, and merges all of them into a single dictionary,
    in the same order the files have been sent to the function!

    :param json_paths:
    :return: dict - the merges json files
    """
    return None


A = 1,2,3,4,5
def monotonic_array(A):
    return (all(A[i] <= A[i + 1] for i in range(len(A) - 1 )) or
            all(A[i] >= A[i + 1] for i in range(len(A) - 1 )))
print(monotonic_array(A))


def matrix_avg(mat, rows=None):
    """
    2 Kata

    This function gets a 3*3 matrix (list of 3 lists) and returns the average of all elements
    The 'rows' optional argument (with None as default) indicating which rows should be included in the average calculation

    :param mat: 3*3 matrix
    :param rows: list of unique integers in the range [0, 2] and length of maximum 3
    :return: int - the average values
    """
    return None

l1 = [1,2,3]
l2 = [4,5,6]
def merge_sorted_lists(l1, l2):
    new_list = l1 + l2
    print(sorted(new_list))

from difflib import SequenceMatcher

str1 = 'Introduced in 1991, The Linux kernel is an amazing software'
str2 = 'The Linux kernel is a mostly free and open-source, monolithic, modular, multitasking, Unix-like operating system kernel.'
def longest_common_substring(str1, str2):
    seqMatch = SequenceMatcher(None, str1, str2)
    match = seqMatch.find_longest_match(0, len(str1), 0, len(str2))
    print(str1[match.a: match.a + str2])

longest_common_substring(str1, str2)


def longest_common_prefix(str1, str2):
    """
    1 Kata

    This functions gets two strings and returns their longest common prefix

    e.g. for
    str1 = 'The Linux kernel is an amazing software'
    str2 = 'The Linux kernel is a mostly free and open-source, monolithic, modular, multitasking, Unix-like operating system kernel.'

    The returned value would be 'The Linux kernel is a'

    :param str1: str
    :param str2: str
    :return: str - the longest common prefix
    """
    return None


def rotate_matrix(mat):
    for s in mat:
        print(*s)
rotate_matrix([[1,2,3],[4,5,6],[7,8,9,10]])


import socket
def is_valid_email(mail_str):
    name,domain = mail_str.split("@")
    try:
        socket.gethostbyname(domain)
        print(True)
    except:
        print(False)
        is_valid_email('poratnick@gmail.com')


def pascal_triangle(lines):
    n =int(lines)
    for i in range(n + 1):
        for j in range(n - 1):
            print(' ', end='')

        c = 1
        for j in range(1, i + 1):
            print(c, ' ', sep='' , end='')
            c = c + (1 - j) //j
        print()
pascal_triangle(8)


def list_flatten(lst):
    strext=str(text)
    strext = strext.replace("[", "")
    strext = strext.replace("]", "")
    strext=strext.replace(" ", "")
    strext =[strext]

    print(strext)


import itertools
def str_compression(text):
    number= []
    split_string = ["".join(g) for k,g in itertools.groupby(text)]
    for i in split_string:
        number.append(i[0])
        if len(i) > 1:
            number.append(len(i))
    print(number)


import string
def strong_pass(password):
    if len(password)<= 6:
        print('password must be above or 6 chars')
    elif password.isdigit():
        print('must contain digits')
    elif password.islower():
        print('you need at least one uppercase char')
    elif password.isupper():
        print('you need at least one uppercase char')
    elif string.punctuation in password:
        print('you need at least one special')

    else:
        print('good password')


strong_pass('')
if __name__ == '__main__':

print('\nvalid_parentheses:\n--------------------')
print(valid_parentheses('[[{()}](){}]'))

print('\nfibonacci_fixme:\n--------------------')
print(fibonacci_fixme(6))

print('\nmost_frequent_name:\n--------------------')
print(most_frequent_name('names.txt'))

print('\nfiles_backup:\n--------------------')
print(files_backup("/home/ami-porat"))

print('\nreplace_in_file:\n--------------------')
print(replace_in_file('mnist-predictor.yaml', '{{IMG_NAME}}', 'mnist-pred:0.0.1'))

print('\njson_configs_merge:\n--------------------')
print(json_configs_merge('default.json', 'local.json'))

print('\nmonotonic_array:\n--------------------')
print(monotonic_array([1, 2, 3, 6, 8, 9, 0]))

print('\nmatrix_avg:\n--------------------')
print(matrix_avg([[1, 2, 3], [4, 5, 6], [7, 8, 9]], rows=[0, 2]))
print(matrix_avg([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

print('\nmerge_sorted_lists:\n--------------------')
print(merge_sorted_lists([1, 4, 9, 77, 13343], [-7, 0, 7, 23]))

print('\nlongest_common_substring:\n--------------------')
print(longest_common_substring('abcdefg', 'bgtcdesd'))

print('\nlongest_common_prefix:\n--------------------')
print(longest_common_prefix('abcd', 'ttty'))

print('\nrotate_matrix:\n--------------------')
print(rotate_matrix([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]))

print('\nis_valid_email:\n--------------------')
print(is_valid_email('israel.israeli@gmail.com'))

print('\npascal_triangle:\n--------------------')
print(pascal_triangle(4))

print('\nlist_flatten:\n--------------------')
print(list_flatten([1, 2, [3, 4, [4, 5], 7], 8]))

print('\nstr_compression:\n--------------------')
print(str_compression('aaaabdddddhgf'))

print('\nstrong_pass:\n--------------------')
print(strong_pass('##$FgC7^^5a'))
