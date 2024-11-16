from vigenere import vig
text = input('Текст: ').upper()
key = input('Ключ: ').upper()
print('\tВыберите действие')
flag = int(input('(1) Зашифровать / (2) Расшифровать: '))

res = vig(text, key, flag)
print(res)