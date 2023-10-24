def multiplicative_inverse(e: int, phi: int) -> int:
    """
    Euclid's extended algorithm for finding the multiplicative
    inverse of two numbers.
    >>> multiplicative_inverse(7, 40)
    23
    """
    d = 0
    for  d in range(1,max(e,phi)):
        if (d*e)%phi == 1:
            res1 = d
    res = 0
    while (e % phi != 0):
        res = e % phi
        e = phi
        phi = res
    if phi == 1:
        return res1