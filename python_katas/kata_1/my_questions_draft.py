Q1

s = 0
elements = [-64, -8, -8, 16, 32]
for num in elements:
    if not elements or all(isinstance(num, str) for num in elements):
        quit()
    elif isinstance(num, int):
        s += num
print(s)
----------------------------------------------------------------------------------------

Q2

word = 'doing'
word_original = word
length = len(word)
# If I want to catch all "iNG/Ing/INg" options uncomment the next line
# word = word.lower()

if length >= 3 and word.endswith('ing'):
    print(word_original + "ly")
elif length >= 3 and not word.endswith('ing'):
    print(word_original + "ing")
else:
    print(word_original)


----------------------------------------------------------------------------------------

Q3 - GO OVER

words = ['take', 'me', 'home']
words = ' '.join(words)
print(words)

----------------------------------------------------------------------------------------

Q4 - GO OVER

words = ['take', 'me', 'home']
words = ' '.join(words[::-1])
print(words)

----------------------------------------------------------------------------------------

Q5







----------------------------------------------------------------------------------------
Q6

My_List = [1,-2]
My_List.reverse()
My_List2 = []
MyLeng = -len(My_List)
for i in My_List:
    My_List2.append((My_List[MyLeng] - My_List[MyLeng + 1]))
    MyLeng += 1
    if MyLeng == -1 :
        My_List2.append(None)
        break
My_List2.reverse()
print(My_List2)
----------------------------------------------------------------------------------------

couple (1)

men = {"John": 20, "Bill": 10, "Abraham": 45}
women = {"July": 18, "Kim": 26, "lili": 15}

#if (min(men, key=men.get)) and (min(women, key=women.get)):
#    a = min(men, key=men.get), min(women, key=women.get)

#print(a)
#print(type(a))

couple (2)

for (key, value) in men.items():
    if value == min(men.values()):
        for (key2, value) in women.items():
            x = key, key2
        print(x)


couple (3)

men = {"John": 20, "Bill": 10, "Abraham": 45, "Danny": 45}
women = {"July": 18, "Kim": 26, "lili": 15}

max_key = None
max_val = None
max_key1 = None
max_val1 = None

for key, val in men.items():
    if max_val is None or val < max_val:
        max_val = val
        max_key = key
    for key1, val1 in women.items():
        if max_val1 is None or val1 < max_val1:
            max_val1 = val1
            max_key1 = key1

print(max_key, max_val)
print(max_key1, max_val1)
couple = max_key, max_key1
print(type(couple))
print(couple)


couple (4-draft)

men = {"John": 20, "Abraham": 45, "ELI": 45}
women = {"July": 19, "Kim": 44, "ELI2": 52}
couple = None
new_dict = {}

min_age_diff = None

for k, v in men.items():
    for k1, v1 in women.items():
        if min_age_diff is None or abs(v1 - v) <= min_age_diff:
            min_age_diff = abs(v1-v)
            couple = k, k1
            print(couple)


last question - sum of digits (1)

aaa = '888'
lst = [int(a) for a in str(aaa)]
suma = 0
for i in range(len(lst)):
    suma = suma + (lst[i])

print(suma)

(7 boom)

def seven_boom(n):
    list_boom = []
    for i in range(0, n + 1):
        if '7' in str(i) or i % 7 == 0:
            list_boom.append(x)
    return list_boom

print(seven_boom(14))



#def seven_boom(n):
#    list_boom = []
#    for i in range(0, n + 1):
#        if ('7' in str(i) or i % 7 == 0) and i != 0:
#            list_boom.append(i)
#    return list_boom

#print(seven_boom(14))


#for x in range(0, 100):
#    if '7' in str(x) or x % 7 == 0:
#        print(x)

(best student (question))

grades = {
        "Ben": 78,
        "Hen": 88,
        "Natan": 99,
        "Efraim": 65,
        "Rachel": 95
    }
for (key, value) in grades.items():
    if value == max(grades.values()):
        x = key
        print(x)


(bad avergae question)

def bad_average(a, b, c):
    """
    1 Kata

    This function gets 3 numbers and calculates the average.
    There is a mistake in the following implementation, you are required to fix it

    :return:
    """
    return (a + b + c) / 3


print(bad_average(155,-15,-15))


(Unique string question - improvement)

def is_unique_string(some_str):
    """
    2 Kata

    Given a string, the function returns True if all characters in the string are unique, False otherwise

    e.g
    'abcd' -> True
    'aaabcd' -> False
    '' -> True      (empty string)

    :param some_str:
    :return: bool
    """

    if len(set(list(some_str))) != len(list(some_str)):
        return False
    else:
        return True


print(is_unique_string(''))


print as table (question (1))

#def print_dict_as_table(some_dict):
grades = {
        "Ben": 78,
        "Hen": 88,
        "Natan": 99,
        "Efraim": 65,
        "Rachel": 95
    }
new_grades = {}
#print(new_grades)
#new_grades.update({1: [5]})
#print(new_grades)
i=0
for k, v in grades.items():
    new_grades.update({i: [k, v]})
    i += 1

#print(new_grades)
print("{:<7} {:<10}".format('Key', 'Value'))
print('-------------')

for k, v in new_grades.items():
    Key, Value, = v
    print("{:<7} {:<10}".format(Key, Value))

grades = {
        "Ben": 78,
        "Hen": 88,
        "Natan": 99,
        "Efraim": 65,
        "Rachel": 95
    }

print("{:<7} {:<10}".format('Key', 'Value'), '\n'"-------------")
for key, value in grades.items():
    print(f'{key:8}{value}')

print as table (question (2))

grades = {
        "Ben": 78,
        "Hen": 88,
        "Natan": 99,
        "Efraim": 65,
        "Rachel": 95
    }

print("{:<7} {:<10}".format('Key', 'Value'), '\n'"-------------")
for key, value in grades.items():
    print(f'{key:8}{value}')


merge dictionaries (question

dict1 = {'a': 1, 'b': 5}
dict2 = {'b': 9, 'a': 3, 'c': 8}
dict1 = dict1 | dict2
print(dict1)





Ceser Cipher (QUESTION)

def cesar(text, key):
    if key == 0:
        return text
    else:
        #text = text.replace("á", chr(97)).replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")\
        #.replace("Á", "A").replace("É", "E").replace("Í", "I").replace("Ó", "O").replace("Ú", "U")\
        #.replace("ñ", "n").replace("Ñ", "N")
        cipher = ""
        for x in range(len(text)):
            if text[x].isalpha():  # only shifting letters
                if text[x].islower():  # lowercase
                    cipher += chr((ord(text[x]) - 97 + key) % 26 + 97)
                else:  # uppercase
                    cipher += chr((ord(text[x]) - 65 + key) % 26 + 65)
            else:
                cipher += text[x]
        return cipher

print(cesar("Fly Me To The Moon", 3))