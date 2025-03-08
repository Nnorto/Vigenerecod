import strings


def csreng(el, cod, shft):
    """
    Алгоритм для кодирования английских символов
    :param el: Символ который необходимо зашифровать.
    :param cod: Ключ по которому осуществляется сдвиг.
    :return: Вернёт зашифрованный символ.
    """
    s = strings.ENGALF
    let = s.find(el)
    chg = s.find(cod)
    if el not in s:
        ns = cod
    else:
        ns = s[(let + chg) % len(s) + (shft % len(s))]
    return ns
def csrru(el, cod, shft):
    """
    Алгоритм для кодирования русских символов
    :param el: Символ который необходимо зашифровать.
    :param cod: Ключ по которому осуществляется сдвиг.
    :return: Вернёт зашифрованный символ.
    """
    s = strings.RUALF
    let = s.find(el)
    chg = s.find(cod)
    if el not in s:
        ns = cod
    else:
        ns = s[(let + chg) % len(s) + (shft % len(s))]
    return ns
