import string
import random

def rand_strok(num):
    new_str = ''
    for i in range(num):
        new_str += random.choice(string.ascii_letters)
    return new_str

def str(n_stroka):
    b = 0; l = 0
    for i in n_stroka:
        if i.isupper():
            b +=1
        else:
            l += 1
    print(n_stroka)
    if b > l:
        print('Больше букв в верхнем регистре')
    elif b < l:
        print('Больше букв в нижнем регистре')
    else:
        print('Заглавных и строчных букв одинаково')

def rand_list_strok(num1, num2):
    llist = [''] * num1
    for i in range(num1):
        for ii in range(num2):
            llist[i] += random.choice(string.ascii_letters)
    return llist

def str_list(spisok):
    bb = 0; ll = 0; oo = 0
    for i in range(len(spisok)):
        b = 0; l = 0
        for ii in range(len(spisok[i])):
            if spisok[i][ii].isupper():
                b +=1
            else:
                l += 1
        if b > l:
            bb +=1
        elif b < l:
            ll += 1
        else:
            oo += 1
    b_pr = bb / (bb + ll + oo) * 100
    l_pr = ll / (bb + ll + oo) * 100
    o_pr = oo / (bb + ll + oo) * 100
    print(spisok)
    print('Процент строк, где заглавных букв больше: ', b_pr, '%', sep = '')
    print('Процент строк, где строчных букв больше: ', l_pr, '%', sep = '')
    print('Процент строк, где их одинаково: ', o_pr, '%', sep = '')

a = rand_strok(10)
str(a)
aa = rand_list_strok(17, 10)
str_list(aa)