def droot(x):
    x = int(x)
    assert x >= 0
    if x > 9:
        return droot(x/10 + x%10)
    else:
        return x

