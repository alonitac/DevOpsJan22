def valid_parentheses(s):
    """
    3 Kata

    This function gets a string containing just the characters '(', ')', '{', '}', '[' and ']',
    and determines if the input string is valid.

    An input string is valid if:
        Open brackets must be closed by the same type of brackets.
        Open brackets must be closed in the correct order.

    e.g.
    s = '[[{()}](){}]'  -> True
    s = '[{]}'          -> False
    """
    while True:
        if '()' in s:
            s = s.replace('()', '')
        elif '{}' in s:
            s = s.replace('{}', '')
        elif '[]' in s:
            s = s.replace('[]', '')
        else:
            return not s

def fibonacci_fixme(n):
    """
    2 Kata

    A Fibonacci sequence is the integer sequence of 1, 1, 2, 3, 5, 8, 13....
    The first two terms are 1 and 1. All other terms are obtained by adding the preceding two terms.

    This function should return the n'th element of fibonacci sequence. As following:

    fibonacci_fixme(1) -> 1
    fibonacci_fixme(2) -> 1
    fibonacci_fixme(3) -> 2
    fibonacci_fixme(4) -> 3
    fibonacci_fixme(5) -> 5

    But it doesn't (it has some bad lines in it...)
    You should (1) correct the for statement and (2) swap two lines, so that the correct fibonacci element will be returned
    """
    a = 0
    b = 1
    for i in range(n):
        tmp = a + b
        a = b
        b = tmp
    return a


def most_frequent_name(file_path):
    """
    2 Kata

    This function gets a path to a file containing names (name in each line)
    The function should return the most frequent name in the file

    You can assume file_path exists in the file system

    :param file_path: str - absolute or relative file to read names from
    :return: str - the mose frequent name. If there are many, return one of them
    """
    mfile = open(file_path)
    data = mfile.readlines()
    my_dict = {}
    for name in data:
        my_dict[name] = data.count(name)
    num = sorted(my_dict.items(), key=lambda x: x[1])
    return num[-1][0]


def files_backup(dir_path):
    """
    3 Kata

    This function gets a path to a directory and generated a .gz file containing all the files the directory contains
    The backup .gz file name should be in the form:

    'backup_<dir_name>_<yyyy-mm-dd>.tar.gz'

    Where <dir_name> is the directory name (only the directory, not the full path given in dir_path)
    and <yyyy-mm-dd> is the date e.g. 2022-04-10

    You can assume dir_path exists in the file system

    :param dir_path: string - path to a directory
    :return: str - the backup file name
    """
    import tarfile
    from datetime import date
    todays_date = str(date.today())
    tar = tarfile.open('backup' + '_' + dir_path + '_' + todays_date + '.tar.gz', 'w:gz')
    tar.add(dir_path)
    file_name = tar.name.split('\\')[-1]
    tar.close()
    return file_name


def replace_in_file(file_path, text, replace_text):
    """
    2 Kata

    This function gets a path of text file, it replaces all occurrences of 'text' by 'replace_text'.
    The function saves the replaces content on the same path (overwrites the file's content)

    You MUST check that file_path exists in the file system before you try to open it

    :param file_path: relative or absolute path to a text file
    :param text: text to search
    :param replace_text: text to replace with
    :return: None
    """
    from pathlib import Path
    if Path(file_path).exists():
        file_read = Path(file_path)
        file_text = file_read.read_text()
        file_text = file_text.replace(text, replace_text)
        file_read.write_text(file_text)

    return None


def json_configs_merge(*json_paths):
    """
    2 Kata

    This function gets an unknown number of paths to json files (represented as tuple in json_paths argument)
    it reads the files content as a dictionary, and merges all of them into a single dictionary,
    in the same order the files have been sent to the function!

    :param json_paths:
    :return: dict - the merges json files
    """
    import json
    files = json_paths
    merg_dict = {}
    for file in files:
        with open(file, 'r+') as f:
            merg_dict.update(json.load(f))
    return merg_dict


def monotonic_array(lst):
    """
    1 Kata

    This function returns True/False if the given list is monotonically increased or decreased

    :param lst: list of numbers (int, floats)
    :return: bool: indicating for monotonicity
    """
    num = 0
    if lst[0] > lst[-1]:
        for num in range(len(lst)-1):
            if lst[num] >= lst[num+1]:
                num += 1
            else:
                return False
        return True
    else:
        for num in range(len(lst)-1):
            if lst[num] <= lst[num+1]:
                num += 1
            else:
                return False
        return True


def matrix_avg(mat, rows=None):
    """
    2 Kata

    This function gets a 3*3 matrix (list of 3 lists) and returns the average of all elements
    The 'rows' optional argument (with None as default) indicating which rows should be included in the average calculation

    :param mat: 3*3 matrix
    :param rows: list of unique integers in the range [0, 2] and length of maximum 3
    :return: int - the average values
    """
    op = 0
    num = 0
    if not rows:
        for lst in mat:
            num += sum(lst)
            op += len(lst)
        return num / op
    else:
        for lst in rows:
            num += sum(mat[lst])
            op += len(mat[lst])
        return num / op


def merge_sorted_lists(l1, l2):
    """
    1 Kata

    This function gets two sorted lists (each one of them is sorted)
    and returns a single sorted list combining both of them.

    Try to be as efficient as you can (hint - don't use Python's built in sort() or sorted() functions)

    :param l1: list of integers
    :param l2: list of integers
    :return: list: sorted list combining l1 and l2
    """
    num1 = 0
    num2 = 0
    i = 0
    num2_len = len(l2) - 1
    while l2[i] < l1[num1]:
        l1.insert(num1, l2[i])
        i += 1


def longest_common_substring(str1, str2):
    """
    4 Kata

    This functions gets two strings and returns their longest common substring

    e.g. for
    str1 = 'Introduced in 1991, The Linux kernel is an amazing software'
    str2 = 'The Linux kernel is a mostly free and open-source, monolithic, modular, multitasking, Unix-like operating system kernel.'

    The returned value would be 'The Linux kernel is a'
    since it's the longest string contained both in str1 and str2

    :param str1: str
    :param str2: str
    :return: str - the longest common substring
    """
    answer = ''
    len1, len2 = len(str1), len(str2)
    for i in range(len1):
        match = ''
        for j in range(len2):
            if i + j < len1 and str1[i + j] == str2[j]:
                match += str2[j]
            else:
                if len(match) > len(answer):
                    answer = match
                match = ''
    return answer


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
    new_list = ''
    num = 0
    while str1[num] == str2[num]:
        new_list += str1[num]
        num += 1

    return new_list


def rotate_matrix(mat):
    """
    2 Kata

    This function gets a matrix n*m (list of m lists of length n) and rotate the matrix clockwise
    e.g.
    for [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]] which represent the matrix

    1   2   3
    4   5   6
    7   8   9
    10  11  12

    The output should be:
    [[10, 7, 4, 1], [11, 8, 5, 2], [12, 9, 6, 3]]

    10  7   4   1
    11  8   5   2
    12  9   6   3

    :param mat:
    :return: list of lists - rotate matrix
    """
    rotated = []
    x = len(mat)
    i = len(mat[x - 1])
    flag = 0
    while i > 0:
        loop = x - 1
        temp = []
        for n in range(x):
            temp.append(mat[loop][flag])
            loop -= 1
            n += 1
        rotated.append(temp)
        flag += 1
        i -= 1
    return rotated


def is_valid_email(mail_str):
    """
    3 Kata

    This function returns True if the given mail is in the form:
    (username)@(domainname)

    Where
    * (username) must start with digit or an English character, and can contains only 0-9 a-z A-Z . or _
    * (domainname) is a real, existed domain - one that resolves to an actual ip address

    Hint: use socket.gethostbyname() to resolve a DNS in Python code

    :param mail_str: mail to check
    :return: bool: True if it's a valid mail (otherwise either False is returned or the program can crash)
    """
    import socket
    user = 0
    dom = 0
    new_list = mail_str.split('@')
    if new_list[0].startswith('_'):
        return False
    if not new_list[0].isalnum() and '._' in new_list[0]:
        user = 0
    else:
        user = 1
    ip4_add = socket.gethostbyname(new_list[1])
    if ip4_add:
        dom = 1
    if user == 1 and dom == 1:
        return True
    else:
        return False


def pascal_triangle(lines):
    """
    3 Kata

    This function gets an integer representing the number of lines to print in a Pascal Triangle
    e.g. For n = 10 then following would be printed

                 1
                1 1
               1 2 1
              1 3 3 1
             1 4 6 4 1
           1 5 10 10 5 1
         1 6 15 20 15 6 1
        1 7 21 35 35 21 7 1
      1 8 28 56 70 56 28 8 1
    1 9 36 84 126 126 84 36 9 1

    You are allowed to print the numbers not in a triangle shape:
    1
    1 1
    1 2 1
    1 3 3 1
    1 4 6 4 1
    1 5 10 10 5 1
    1 6 15 20 15 6 1
    1 7 21 35 35 21 7 1
    1 8 28 56 70 56 28 8 1
    1 9 36 84 126 126 84 36 9 1

    :param lines: int
    :return: None
    """
    for i in range(1, lines + 1):
        pas = 1
        for j in range(1, i + 1):
            print(pas, end=' ')
            pas = pas * (i - j) // j
        print()


def list_flatten(lst):
    """
    2 Kata

    This function gets a list of combination of integers or nested lists
    e.g.
    [1, [], [1, 2, [4, 0, [5], 6], [5, 4], 34, 0], [3]]

    The functions should return a flatten list (including all nested lists):
    [1, 1, 2, 4, 0, 5, 6, 5, 4, 34, 0, 3]

    :param lst: list of integers of another list
    :return: flatten list
    """
    flat_list = []
    for sublist in lst:
        if type(sublist) is not list:
            flat_list.append(sublist)
        else:
            for num in sublist:
                flat_list.append(num)

    print(flat_list)


def str_compression(text):
    """
    2 Kata

    This function gets a text (string) and returns a list representing the compressed form of the text.
    e.g.
    text = 'aaaaabbcaasbbgvccf'

    The output will be:
    ['a', 5, 'b', 2, 'c', 'a', 2, 's', 1, 'b', 2, 'g', 'v', 'c', 2, 'f']

    Since 'a' appears 5 times in consecutively, 'b' 2 times etc...
    Note that sequences of length 1 don't necessarily have the number 1 after the character (like 'c' before 'a')

    :param text: str
    :return: list representing the compressed form of the string
    """
    '''new_dic = {}
    new_list = []
    for let in text:
        if let in new_dic:
            new_dic[let] += 1
        else:
            new_dic[let] = 1
    for key, value in new_dic.items():
        temp = [key, value]
        new_list.append(temp)
    return new_list'''
    new_lst = []
    num = 0
    flag = 0
    if text == '':
        text = []
        return text
    for tmp in range(len(text)):
        if tmp > 0:
            flag = 1
        if text[tmp] == text[tmp - flag]:
            num += 1
        else:
            if num > 1:
                new_lst.append(num)
            new_lst.append(text[tmp])
            num = 1
    return new_lst





def strong_pass(password):
    """
    1 Kata

    A password is considered strong if it satisfies the following criteria:
    1) Its length is at least 6.
    2) It contains at least one digit.
    3) It contains at least one lowercase English character.
    4) It contains at least one uppercase English character.
    5) It contains at least one special character. The special characters are: !@#$%^&*()-+

    This function returns True if the given password is strong enough
    """
    if len(password) < 6:
        return False
    digit = False
    lower = False
    upper = False
    spec = False

    for i in password:
        if i.isdigit():
            digit = True
        elif i.islower():
            lower = True
        elif i.isupper():
            upper = True
        elif not i.isidentifier():
            spec = True
    if digit and lower and upper and spec:
        return True
    else:
        return False


if __name__ == '__main__':
    print('\nvalid_parentheses:\n--------------------')
    print(valid_parentheses('[[{()}](){}]'))

    print('\nfibonacci_fixme:\n--------------------')
    print(fibonacci_fixme(6))

    print('\nmost_frequent_name:\n--------------------')
    print(most_frequent_name('names.txt'))

    print('\nfiles_backup:\n--------------------')
    print(files_backup('files_to_backup'))

    print('\nreplace_in_file:\n--------------------')
    print(replace_in_file('mnist-predictor.yaml', '{{IMG_NAME}}', 'mnist-pred:0.0.1'))

    #print('\njson_configs_merge:\n--------------------')
    print(json_configs_merge('jpg.json', 'student.json'))

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
