import string
def csrd(el, cod):
    s = string.ascii_uppercase
    let = s.find(el)
    chg = s.find(cod)

    ns = ''
    ns += s[(let - chg)%len(s)]
    return ns
