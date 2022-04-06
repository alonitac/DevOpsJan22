'''
#elements_for_function = [-1,2,3,4,5,6]
def sum_of_element(elements):
    s = 0

    for num in elements:
        s = s + num

    return s
sum_of_element(elements_for_function[1,2,3,4,5])
print(s)
'''
import math
from random import random

'''
def verbing(word):

    count_char = len(word)
    print('Length of your word is',len(word), 'characters')
    if word[-3:]=='ing':
            print('Three last characters is ing ')
            word = word + 'ly'
    elif count_char >= 3:
            word = word + ('ing')
    elif count_char < 3:
            return word
    return word
verb ='fud'
print(verbing(verb))
'''


'''
def words_concatenation(words):
    if words==[]:
        print('Your list is empty,BYE')
        return None
    else:
        concat_string = ' '.join(words)
        print(concat_string)
words_concatenation(['take','me'])
'''

'''
def reverse_words_concatenation(words):
    if words==[]:
        print('Your list is empty,BYE')
        return None
    else:
        concat_string = ' '.join(words)
        words = concat_string.reverse()
        print(words)
    return words
reverse_words_concatenation(['take','me'])
'''

'''
def is_unique_string(some_str):
  for a in range(len(some_str)):
    for b in range(a + 1,len(some_str)):
      if(some_str[a] == some_str[b]):
        print('False')
        return False
  print('True')
  return True
is_unique_string('12341')
'''

'''
def list_diff(elements): !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    i = elements[0]-elements[0]
    j = elements
    print(i)
    #for i in elements:
     #   print(j-i)

list_diff([1,15,20,30])
'''

'''
def prime_number(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
              print(num, "is not a prime number")
              return False

        print(num, "is prime number")
        return True
prime_number(3)

'''        
'''
def palindrome_num(num):
'''






'''
def bad_average(a, b, c):
    avg =  (a + b + c ) / 3
    print(avg)
    return (a+b+c) / 3
bad_average(2, 100, 10)
'''


'''
def merge_dicts(dict1,dict2):
    dict1 = dict1 | dict2
    print(dict1)
    return dict1
merge_dicts({'a': 1},{'b' : 2})
'''

