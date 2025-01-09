import string


def csr(el, cod):
    """
    :param el: Символ который необходимо зашифровать.
    :param cod: Ключ по которому осуществляется сдвиг.
    :return: Вернёт зашифрованный символ.
    """
    s = string.ascii_uppercase
    let = s.find(el)
    chg = s.find(cod)
    ns = ''
    if el not in s:
        ns = cod
    else:
        ns = s[(let + chg) % len(s)]
    return ns
