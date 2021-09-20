from random import choice
import string


def rand_str(length):
    letters = list(string.ascii_letters)
    s = ''
    for _ in range(length):
        s += choice(letters)
    return s


def score_letters(str):
    upper_count = 0
    lower_count = 0
    for i in str:
        if i.isupper():
            upper_count += 1
        else:
            lower_count += 1
    if upper_count > lower_count:
        return 1
    elif upper_count == lower_count:
        return 2
    else:
        return 0


def array_of_strings(length, count_strings):
    return [rand_str(length) for _ in range(count_strings)]

print(score_letters(rand_str(10)))