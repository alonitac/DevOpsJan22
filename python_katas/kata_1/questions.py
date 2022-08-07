def sum_of_element(elements):
    s = 0
    for num in elements:
        s = s + num

    return s


def verbing(word):
    word_len = len(word)
    if word_len >= 3:
        if 'ing' in word[-3:]:
            result = word + 'ly'
        else:
            result = word + 'ing'
    else:
        result = word

    return result


def words_concatenation(words):
    result = ''
    for word in words:
        result += word + ' '
    return result[:-1]


def reverse_words_concatenation(words):
    words.reverse()
    result = ''
    for word in words:
        result += word + ' '
    return result[:-1]


def is_unique_string(some_str):
    unique_string = ''
    for word in some_str:
        if len(set(some_str)) == len(list(some_str)):
            return True
        else:
            pass
    return False


def list_diff(elements):
    x = [None]
    if len(elements) == 0:
        return []
    else:
        for i in range(1, len(elements)):
            x.append(elements[i] - elements[i - 1])

        return x


def prime_number(num):
    if not isinstance(num, int):

        return False

    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
            return True
    else:
        return False


def palindrome_num(num):
    x = str(num)
    if x[::-1] == x:
        return True
    else:
        return False


def pair_match(men, women):
    age_min = 99999
    names_min = ("a", "b")

    for key, value in men.items():
        for w_key, w_value in women.items():

            d_keys = (key, w_key)
            age_diff = abs(value - w_value)
            if age_min > age_diff:
                names_min = d_keys
                age_min = age_diff

    return names_min


def bad_average(a, b, c):
    num = (a, b, c)
    sum_num = 0
    for t in num:
        sum_num = sum_num + t

    avg = sum_num / len(num)

    return avg


def best_student(grades):
    grade_max = -1
    names_max = None
    for name, value in grades.items():
        if value > grade_max:
            grade_max = value
            names_max = name

    return names_max


def print_dict_as_table(some_dict):
    for n,e in some_dict.items():
        print(f"{n}     {e}")

print('key    value \n'
      '--------------')

print_dict_as_table(some_dict)

def merge_dicts(dict1, dict2):
    return dict1 | dict2


def seven_boom(n):
    list_booms = []
    while n > 0:
        if n % 7 == 0 or ('7' in str(n)):
            list_booms.append(n)
        n -= 1
    list_booms.reverse()

    return list_booms


def caesar_cipher(str_to_encrypt):
    text=str_to_encrypt
    cipher=""
    for x in range(len(text)):
            if test[x].isalpha():
                    if text[x].islower(): # lowercase
                            cipher += chr((ord(text[x]) - 97 + 3)% 26 + 97)
                    else: # uppercase
                            cipher += chr((ord(text[x]) - 65 + 3) % 26 + 65)
            else:
                    cipher += text[x]
    return cihper

# shift = 3
#     output = []
#     for c in str_to_encrypt:
#         if c == " ":
#             z = c
#         else:
#             z = ord(c) + shift
#             if z > 90:
#                 z += 7
#             z = z % 122
#             if z < 68:
#                 z += 65
#             z = chr(z)
#         output.append(z)
#
#     output = "".join(output)
#     return output


def sum_of_digits(digits_str):
    l=0
    for i in digits_str:
            s=int(i)
            l +=s
    return (l)

    output = 0
    for val in digits_str:
        output += int(val)

    return output

if __name__ == '__main__':

    print('\nsum_of_element:\n--------------------')
    print(sum_of_element([1, 2, 3, 4, 5, 6]))

    print('\nverbing:\n--------------------')
    print(verbing('walk'))
    print(verbing('swimming'))
    print(verbing('do'))

    print('\nwords_concatenation:\n--------------------')
    print(words_concatenation(['take', 'me', 'home']))

    print('\nreverse_words_concatenation:\n--------------------')
    print(reverse_words_concatenation(['take', 'me', 'home']))

    print('\nis_unique_string:\n--------------------')
    print(is_unique_string('aasdssdsederd'))
    print(is_unique_string('12345tgbnh'))

    print('\nlist_diff:\n--------------------')
    print(list_diff([1, 2, 3, 8, 77, 0]))

    print('\nprime_number:\n--------------------')
    print(prime_number(5))
    print(prime_number(22))

    print('\npalindrome_num:\n--------------------')
    print(palindrome_num(12221))
    print(palindrome_num(577))

    print('\npair_match:\n--------------------')
    print(pair_match(
        {
            "John": 20,
            "Abraham": 45
        },
        {
            "July": 18,
            "Kim": 26
        }
    ))

    print('\nbad_average:\n--------------------')
    print(bad_average(1, 2, 3))

    print('\nbest_student:\n--------------------')
    print(best_student({
        "Ben": 78,
        "Hen": 88,
        "Natan": 99,
        "Efraim": 65,
        "Rachel": 95
    }))

    print('\nprint_dict_as_table:\n--------------------')
    print(print_dict_as_table({
        "Ben": 78,
        "Hen": 88,
        "Natan": 99,
        "Efraim": 65,
        "Rachel": 95
    }))

    print('\nmerge_dicts:\n--------------------')
    print(merge_dicts({'a': 1}, {'b': 2}))

    print('\nseven_boom:\n--------------------')
    print(seven_boom(30))

    print('\ncaesar_cipher:\n--------------------')
    print(caesar_cipher('Fly Me To The Moon'))

    print('\nsum_of_digits:\n--------------------')
    print(sum_of_digits('1223432'))

