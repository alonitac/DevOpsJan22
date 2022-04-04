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

    boolean = False

# 0 to 3 is prime numbers
    if num > 3:
        # check if num is exactly divisible by any number from 2 to num - 1
        for i in range(2, num-1):
            if (num % i) == 0:
              boolean = True
              break

    if boolean==True:
        print(num, "is not a prime number")
        return False
    else:
      print(num, "is a prime number")
      return True

prime_number(15)
'''






