from vigenere import vig
from strings import *
from random import randrange
print('\tВыберите язык:')
language = int(input('(1) Русский / (2) Английский: '))
text = input('Текст: ').upper()
key = input('Ключ: ').upper()
print('\tВыберите действие:')
flag = int(input('(1) Зашифровать / (2) Расшифровать: '))
if flag == 1:
    if language == 1:
        shift = randrange(0, 33)
        res = vig(text, key, flag, shift, language)
        print(res)
        print(f'Ваш дополнительный ключ: {RUALF[shift]}', 'Просим вас делиться им только с собеседником', sep='\n')
    else:
        shift = randrange(0, 26)
        res = vig(text, key, flag, shift, language)
        print(res)
        print(f'Ваш дополнительный ключ: {ENGALF[shift]}', 'Просим вас делиться им только с собеседником', sep='\n')
else:
    shift = input('Введите начало алфавита: ').upper()
    res = vig(text, key, flag, shift, language)
    print(res)