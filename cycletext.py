def cycl(t, k):
    text = t.upper()
    k = k.upper()

    ns = k * (len(text)//len(k))

    for i in range((len(text)//len(k)) * len(k), len(text)):
        ns += k[i % len(k)]
    return ns
