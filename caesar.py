import strings


def csreng(el, cod, shift):
    """
    Алгоритм для кодирования английских символов
    :param el: Символ который необходимо зашифровать.
    :param cod: Ключ по которому осуществляется сдвиг.
    :param shift: Сдвиг, который отвечает за начало алфавита
    :return: Вернёт зашифрованный символ.
    """
    s = strings.ENGALF
    let = s.find(el)
    chg = s.find(cod)
    if el not in s:
        ns = cod
    else:
        ns = s[(let + chg + shift) % len(s)]
    return ns
def csrru(el, cod, shift):
    """
    Алгоритм для кодирования русских символов
    :param el: Символ который необходимо зашифровать.
    :param cod: Ключ по которому осуществляется сдвиг.
    :param shift: Сдвиг, который отвечает за начало алфавита
    :return: Вернёт зашифрованный символ.
    """
    s = strings.RUALF
    let = s.find(el)
    chg = s.find(cod)
    if el not in s:
        ns = cod
    else:
        ns = s[(let + chg + shift) % len(s)]
    return ns
