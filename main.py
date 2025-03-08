from vigenere import vig
print('\tВыберите язык:')
language = int(input('(1) Русский / (2) Английский: '))
text = input('Текст: ').upper()
key = input('Ключ: ').upper()
shft = int(input('Введите сдвиг алфавита (число): '))
print('\tВыберите действие:')
flag = int(input('(1) Зашифровать / (2) Расшифровать: '))

res = vig(text, key, shft, flag, language)
print(res)
