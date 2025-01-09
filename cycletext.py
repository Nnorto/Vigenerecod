def cycl(text, key):
    """
    Эта функция нужна для циклического наложения ключа Виженера на текст пользователя.
    :param text: Текст, который будет зашифрован.
    :param key: Ключ.
    :return: Строка с ключом длиной как у t
    """
    text = text.upper()
    key = key.upper()
    ns = ''
    count = 0
    for i in range(len(text)):
        if not text[i].isalpha():
            ns += text[i]
        else:
            ns += key[count]
            count += 1
            if count == len(key):
                count = 0
    return ns