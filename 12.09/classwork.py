def palindrome(string):
    return string == string[:: -1]


def exp(string: str):
    return string.split(".")[1]

def tiimee(num: int):
    days = num // (60 * 60 * 24)
    num %= 60 * 60 * 24
    hours = num // (60 * 60)
    num %= 60 * 60
    minutes = num // 60
    num %= 60 
    seconds = num
    return f'{days}:{hours}:{minutes}:{seconds}'

def nofn(chislo):
    n = str(chislo)
    stroka = n + ' + ' + n * 2 + ' + ' + n * 3 + ' = '
    summa = int(n) + int(n * 2) + int(n * 3)
    return stroka, summa

print(tiimee(123467))
