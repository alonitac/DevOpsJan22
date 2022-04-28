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
def list_diff(elements):
    length=len(elements)-1
    diff=[None]
    
    for i in range(length):
        diff.append(elements[i+1]-elements[i])
    print(diff)
    return diff
list_diff([1,15,20,30,5])
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
    temp=num
    rev=0
    while(num>0):
        dig=num%10
        rev=rev*10+dig
        num=num//10
    if(temp==rev):
        print("The number is a palindrome!")
        return True
    else:
        print("The number isn't a palindrome!")
        return False
palindrome_num(1211)
'''


'''
def bad_average(a, b, c):
    avg =  (a + b + c ) / 3
    print(avg)
    return (a+b+c) / 3
bad_average(2, 100, 10)
'''
'''
def print_dict_as_table(some_dict):    
    print("{:<15} {:<15} ".format('Key', 'Value'))
    print('-----           ------')
    for key, value in some_dict.items():
        name = key
        score = value
        print("{:<15} {:<15} ".format(name, score))
print_dict_as_table({'Ben':78,'Natan':45,'David':100,'gggggggggg':50})
'''

'''
def merge_dicts(dict1,dict2):
    dict1 = dict1 | dict2
    print(dict1)
    #return dict1
merge_dicts({'a': 1},{'b' : 2})
'''

'''
def sum_of_digits(digits_str):
   sum=0
   for digit in digits_str:
       sum+=int(digit)
   print(sum)
   return sum
sum_of_digits('00033')
'''

'''
def seven_boom(end_number):
    booms = []
    n = 1

    while n <= end_number:
        if (n % 7 == 0) or ('7' in str(n)):
            booms.append(n)
        n += 1
    print(booms)
seven_boom(50)
'''

'''
def best_student(grades):
    sort_by_score=sorted(grades.items(), key=lambda x: x[1],reverse=True)
    print(sort_by_score)
    print(sort_by_score[0][0])
    return sort_by_score[0][0]

best_student({
        "Ben": 78,
        "Hen": 88,
        "Natan": 99,
        "Efraim": 65,
        "Rachel": 95 })
'''

'''
text=input("enter string \n")
a_char=text[0]
new_text=text[1:].replace(a_char,'e')
print(a_char+new_text)
'''

'''
text='aaaa'
length=len(text)//2
print(length)
print(text[length:] + text[length:].upper())
'''

'''
import numpy as np

list=[1,2,3,4,1,2,1,2,5]
y=np.array(list)
print(y>2)

x = ["a", "b", "c"]
x[1]
print(x)

np_x = np.array(x)
np_x[1]
print(np_x)
'''





#KATA_2
'''
def valid_parentheses(s):
    empty_list=[]
    brackets = {'}':'{',']':'[',')':'('}
    for char in s:
        if char in brackets:
            if empty_list and empty_list[-1] == brackets[char]:
                empty_list.pop()
            else:
                return False
        else:
            empty_list.append(char)
    return True if not empty_list else False
valid_parentheses('{}[](){[}]')
'''

'''
#Fibonachi

a = 0
b = 1
for i in range(6):
    tmp = a + b
    a = b
    b = tmp

    print(a)
'''

#def monotonic_array(lst):
a=[3,2,1,0]
(all(a[i] <= a[i + 1] for i in range(len(a) - 1)) or
all(a[i] >= a[i + 1] for i in range(len(a) - 1)))




#monotonic_array([1,2,3,4,5,1])
