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
    concat_string = ' '.join(words)
    print(concat_string)
words_concatenation(['take','me','home','now'])
'''







