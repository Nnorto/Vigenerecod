import strings
def csrdeng(el, cod, shft):
    """
    Алгоритм для декодирования английских символов
    :param el: Символ который необходимо расшифровать.
    :param cod: Ключ по которому осуществляется сдвиг.
    :return: Вернёт расшифрованный символ.
    """
    s = strings.ENGALF
    let = s.find(el)
    chg = s.find(cod)

    if el not in s:
        ns = cod
    else:
        ns = s[(let - chg) % len(s) - (shft % len(s))]
    return ns

def csrdru(el, cod, shft):
    """
    Алгоритм для декодирования русских символов
    :param el: Символ который необходимо расшифровать.
    :param cod: Ключ по которому осуществляется сдвиг.
    :return: Вернёт расшифрованный символ.
    """
    s = strings.RUALF
    let = s.find(el)
    chg = s.find(cod)

    if el not in s:
        ns = cod
    else:
        ns = s[(let - chg) % len(s) - (shft % len(s))]
    return ns
