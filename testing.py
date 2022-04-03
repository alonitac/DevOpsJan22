from collections import Counter


def unique_exp_check(string_check):
    """
    This function checks if the string received contains only unique strings, using counter.
    :param string_check:
    :return:True or False
    """

    # Counting frequency
    freq = Counter(string_check)

    if (len(freq)) == len(string_check):
        return True
    else:
        return False


str_check = "abcd"
my_list = [1, 2, 3, 4, 5, 6]
print("Does the string/list - '" + str_check + "' contain unique chars/index only: " + str(unique_exp_check(str_check)))
print("Does the string/list - '" + str(my_list) + "' contain unique chars/index only: " + str(unique_exp_check(my_list)))


def word_testing(str_exp):
    """

    This function receives text(string), checks if the string length is less than 3 characters,and returns the string
    Else it adds the "ing" to the end of the string and then returns it.
    :param str_exp: text
    :return: returns the result string
    """
    word_len = len(str_exp)
    #print(word_len)
    #print(str_exp[-3:word_len])
    if (word_len >= 3) & (str_exp[-3:word_len] != "ing"):
        result = "The string has been updated(added 'ing' at the end): " + str_exp + "ing"
    else:
        result = "The string has no changes since it may not be equal or above 3 characters or it may already be 'ing': " + str_exp
    return result


word = "ing"
print(word_testing(word))
