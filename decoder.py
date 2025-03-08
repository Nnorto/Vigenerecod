import strings
def csrdeng(el, cod, start):
    """
    Алгоритм для декодирования английских символов
    :param el: Символ который необходимо расшифровать.
    :param cod: Ключ по которому осуществляется сдвиг.
    :return: Вернёт расшифрованный символ.
    """
    s = strings.ENGALF
    shift = s.find(start)
    let = s.find(el)
    chg = s.find(cod)

    if el not in s:
        ns = cod
    else:
        ns = s[(let - chg - shift) % len(s)]
    return ns

def csrdru(el, cod, start):
    """
    Алгоритм для декодирования русских символов
    :param el: Символ который необходимо расшифровать.
    :param cod: Ключ по которому осуществляется сдвиг.
    :return: Вернёт расшифрованный символ.
    """
    s = strings.RUALF
    shift = s.find(start)
    let = s.find(el)
    chg = s.find(cod)

    if el not in s:
        ns = cod
    else:
        ns = s[(let - chg - shift) % len(s)]
    return ns
