from caesar import csr
from cycletext import cycl
from decoder import csrd


def vig(text, k, f):
    key = cycl(text, k)
    ns = ''
    flag = f
    if flag == 1:
        for i in range(len(text)):
            ns += csr(text[i], key[i])
    else:
        for i in range(len(text)):
            ns += csrd(text[i], key[i])
    return ns
