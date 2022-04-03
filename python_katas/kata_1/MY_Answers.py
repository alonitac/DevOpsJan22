'''
elements_for_function = [-1,2,3,4,5,6]
def sum_of_element(elements):
    s = 0

    for num in elements:
        s = s + num

    print(s)
sum_of_element(elements_for_function)
'''

any_word = 'doing'
count_char = len(any_word)
print('Length of your word is ',len(any_word))
if  count_char >= 3:
    any_word = any_word + ('ing')
    print(any_word)
#elif count_char < 3:
#    print(any_word)
elif any_word[-3:] == 'ing':
    print('Three last characters is ing ')
    print(any_word + 'ly')
elif count_char < 3:
    print(any_word)