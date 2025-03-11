from caesar import *
from cycletext import *
from decoder import *


def vig(text, k, f, shift, language):
    key = cycl(text, k)
    ns = ''
    flag = f
    startalf = shift
    if flag == 1:
        if language == 1:
            for i in range(len(text)):
                ns += csrru(text[i], key[i], startalf)
        else:
            for i in range(len(text)):
                ns += csreng(text[i], key[i], startalf)
    else:
        if language == 1:
            for i in range(len(text)):
                ns += csrdru(text[i], key[i], startalf)
        else:
            for i in range(len(text)):
                ns += csrdeng(text[i], key[i], startalf)
    return ns
